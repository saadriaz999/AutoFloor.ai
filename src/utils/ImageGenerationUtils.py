import io
import requests
from PIL import Image
from src.utils import Constants, ProjectUtils


def make_final_prompt(bedrooms, bathrooms, garage, kitchen, prompt):
    final_prompt = f'this floor plan has {bedrooms} and {bathrooms} bathrooms'
    if garage:
        final_prompt += ' and garage'
    if kitchen:
        final_prompt += ' and kitchen'

    return final_prompt


def generate_floor_plan(prompt):
    payload = {"inputs": prompt}
    response = requests.post(Constants.API_URL, headers=Constants.HEADERS, json=payload)

    # Check the content type of the response
    content_type = response.headers.get('Content-Type')
    print(f"Content-Type: {content_type}")

    # If the content is JSON, print it out
    if 'application/json' in content_type:
        print(response.json())
    else:
        # If the content is not JSON, assume it's image bytes
        image_bytes = response.content

        # Print the first few bytes for debugging
        print(image_bytes[:100])

        # Load the image bytes using PIL and display/save it
        try:
            image = Image.open(io.BytesIO(image_bytes))
            path = ProjectUtils.get_save_image_path('')
            image.save(path)
        except Exception as e:
            print(f"Error: {e}")
