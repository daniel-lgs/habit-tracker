# When you see the comment 'PYOD' it means 'Provide your own data'

import requests
from datetime import date

date_today = date.today()
date_today = date_today.strftime("%Y%m%d")

USERNAME = ""  # PYOD
TOKEN = ""  # PYOD
GRAPHID = ""  # PYOD

date_to_update = ""  # PYOD
date_to_delete = ""  # PYOD

# Pixela endpoints
CREATE_USER = "https://pixe.la/v1/users"
CREATE_GRAPH = f"https://pixe.la/v1/users/{USERNAME}/graphs"
CREATE_PIXEL = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}"
UPDATE_PIXEL = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}/{date_to_update}"
DELETE_PIXEL = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}/{date_to_delete}"


def create_user():
    register_params = {
        "token": USERNAME,
        "username": TOKEN,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    response = requests.post(url=CREATE_USER, json=register_params)
    print(response.text)


def create_graph():
    graph_params = {
        "id": "",  # PYOD
        "name": "",  # PYOD
        "unit": "",  # PYOD
        "type": "",  # PYOD
        "color": ""  # PYOD
    }
    headers = {
        "X-USER-TOKEN": TOKEN
    }
    response = requests.post(url=CREATE_GRAPH, json=graph_params, headers=headers)
    print(response.text)


def create_pixel():
    pixel_params = {
        "date": date_today,
        "quantity": input("Enter the quantity: ")
    }
    headers = {
        "X-USER-TOKEN": TOKEN
    }
    response = requests.post(url=CREATE_PIXEL, json=pixel_params, headers=headers)
    print(response.text)


def update_pixel():
    update_params = {
        "quantity": input("Enter the quantity: ")
    }
    headers = {
        "X-USER-TOKEN": TOKEN
    }
    response = requests.put(url=UPDATE_PIXEL, json=update_params, headers=headers)
    print(response.text)


def delete_pixel():
    headers = {
        "X-USER-TOKEN": TOKEN
    }
    response = requests.delete(url=DELETE_PIXEL, headers=headers)
    print(response.text)
