import requests


def test_list_users():
    get_req = requests.get('https://reqres.in/api/users?page=2')
    get_req_json = get_req.json()
    assert get_req.status_code == 200
    print(get_req_json['id'])