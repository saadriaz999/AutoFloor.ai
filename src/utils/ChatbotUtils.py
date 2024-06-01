import google.generativeai as genai

from src.utils import Constants


def load_gemini_chatbot():
    genai.configure(api_key=Constants.GEMINI_API_KEY)

    model = genai.GenerativeModel('gemini-pro-vision')
    return model 


def gemini_chatbot(content, model):
    response = model.generate_content(content)

    return response.text


# the below two functions are general purpose functions that can be used to load and run any chatbot based model


def load_chatbot(model_name='gemini'):
    if model_name == 'gemini':
        model = load_gemini_chatbot()

    return model


def use_chatbot(content, model, model_name='gemini'):
    if model_name == 'gemini':
        response = gemini_chatbot(content, model)
        print('Generated image - easy')
    return response
