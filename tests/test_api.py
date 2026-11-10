import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

pytestmark = pytest.mark.api


def test_get_single_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert len(response.json()) == 100


def test_create_post():
    new_post = {"title": "My test", "body": "Hello", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201
    assert response.json()["title"] == "My test"


def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200


def test_post_not_found():
    response = requests.get(f"{BASE_URL}/posts/99999")
    assert response.status_code == 404