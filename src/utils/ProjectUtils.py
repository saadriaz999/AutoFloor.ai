import os
import json
import pathlib


def get_root_dir_path():
    return pathlib.Path(__file__).parent.parent.parent.resolve()


def load_floorplan_labels():
    path = os.path.join(get_root_dir_path(), 'data', 'image_captions', 'labels.json')
    with open(path, 'r') as file:
        data = json.load(file)

    return data


def get_annotated_images_dir_path():
    return os.path.join(get_root_dir_path(), 'data', 'annotated_images')


def get_embeddings_path(model_id):
    return os.path.join(get_root_dir_path(), 'data', 'embeddings', f'embeddings_{model_id}.json')


def get_save_image_path(x):
    return os.path.join(get_root_dir_path(), 'src', 'static', 'images', 'current', f'current_image{x}.jpg')
