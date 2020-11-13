import requests

def test_check_status_code_equals_200():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    assert r.status_code == 200


def test_get_check_content_type_equals_json():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(response.headers)
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

def test_get_check_title_for_first():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    body = response.json()
    assert body[0]['title'] == 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'

def test_get_check_return_all_records():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    body = response.json()
    assert len(body) == 100