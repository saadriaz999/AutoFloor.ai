import json
from qdrant_client.models import Distance

from utils import ProjectUtils, DatabaseUtils, EmbeddingUtils


def load_pubmed_dataset():
    path = ProjectUtils.load_floorplan_labels()
    with open(path, 'r') as file:
        data = json.load(file)

    return data


if __name__ == '__main__':

    # loading embedding models
    GEMINI_EMBEDDING_MODEL_NAME = 'gemini'
    GEMINI_EMBEDDING_MODEL = EmbeddingUtils.load_embedding_model(GEMINI_EMBEDDING_MODEL_NAME)

    # save vectors of preprocessed dataset created by gemini api
    DatabaseUtils.create_and_store_embeddings(
        GEMINI_EMBEDDING_MODEL, GEMINI_EMBEDDING_MODEL_NAME, Distance.COSINE, 'gemini-cosine')
    print('Saved gemini vectors in database (distance_metric = cosine similarity)')
