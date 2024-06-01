import pathlib

from src.utils import EmbeddingUtils, ChatbotUtils, DatabaseUtils


def retrieval(user_input, collection_name='gemini-cosine', top_k=2):
    embedding_model = EmbeddingUtils.load_embedding_model()
    user_input_embedding = EmbeddingUtils.create_embedding(user_input, embedding_model)

    database_client = DatabaseUtils.create_db_connection()
    search_result = database_client.search(
        collection_name=collection_name,
        query_vector=user_input_embedding
    )

    search_result = search_result[:top_k]

    return search_result


def generation(search_result):

    image_1 = {
        'mime_type': 'image/png',
        'data': pathlib.Path('cookie.png').read_bytes()
    }
    image_2 = {
        'mime_type': 'image/png',
        'data': pathlib.Path('cookie.png').read_bytes()
    }

    prompt = "Using the images given, give me a similar floor plan with stairs added to some empty area. The output should be a json with the corrdinates of each room."

    chatbot_model = ChatbotUtils.load_chatbot()
    response = ChatbotUtils.use_chatbot([image_1, image_2, prompt], chatbot_model)

    print(response.text)
