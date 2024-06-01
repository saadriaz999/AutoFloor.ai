import google.generativeai as genai

from src.utils import Constants


def load_gemini_embedding():
    genai.configure(api_key=Constants.GEMINI_API_KEY)

    model = genai.GenerativeModel('gemini-pro')
    return model


def gemini_embedding(user_input):
    embedding = genai.embed_content(
        model="models/embedding-001",
        content=user_input,
        task_type="RETRIEVAL_QUERY"
    )

    return embedding['embedding']


# the below two functions are general purpose functions that can be used to load and run any embedding model


def load_embedding_model(model_name='gemini'):
    if model_name == 'gemini':
        model = load_gemini_embedding()

    return model


def create_embedding(input, model=None, model_name='gemini'):
    if model_name == 'gemini':
        embedding = gemini_embedding(input)

    return embedding
