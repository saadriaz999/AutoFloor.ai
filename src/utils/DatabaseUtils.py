import json
from qdrant_client import QdrantClient, models
from qdrant_client.models import VectorParams
from qdrant_client.models import PointStruct

from src.utils import Constants, ProjectUtils, EmbeddingUtils


def create_db_connection():
    """Establishes a connection to the QDRant Vector database and return a
    client to communicate with the database"""
    
    client = QdrantClient(url=Constants.QDRANT_DATABASE_CONNECTION_STRING)
    return client


def create_and_store_embeddings(model, model_name, distance_metric, collection_name):
    """Creates embedding of dataset for given model and stores in database"""

    data = ProjectUtils.load_floorplan_labels()

    embedding_size = Constants.COLLECTIONS[collection_name]['embedding_size']
    model_id = Constants.COLLECTIONS[collection_name]['model_id']
    path = ProjectUtils.get_embeddings_path(model_id)

    ids = []
    vectors = []
    points = []
    for i, (key, value) in enumerate(data.items()):
        vector = EmbeddingUtils.create_embedding(value, model, model_name)
        vectors.append(vector)
        ids.append(key)

        payload = {'caption': value}
        points.append(PointStruct(id=key, payload=payload, vector=vector))

        if i == 10:
            break

    vector_dictionary = {key: value for key, value in zip(ids, vectors)}

    database_client = create_db_connection()
    try:
        database_client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=embedding_size, distance=distance_metric),
            optimizers_config=models.OptimizersConfigDiff(indexing_threshold=0),
            shard_number=4
        )
    except:
        pass

    database_client.upload_points(
        collection_name=collection_name,
        wait=True,
        points=points
    )

    database_client.update_collection(
        collection_name=collection_name,
        optimizer_config=models.OptimizersConfigDiff(indexing_threshold=20000),
    )

    with open(path, "w") as json_file:
        json.dump(vector_dictionary, json_file)
