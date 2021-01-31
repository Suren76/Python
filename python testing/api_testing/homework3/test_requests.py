import pytest
import requests

@pytest.mark.skip
class TestGetRequests:
    def test_list_users(self):
        get_req = requests.get('https://reqres.in/api/users?page=2')
        get_req_json = get_req.json()
        assert get_req.status_code == 200
        assert get_req_json['page'] == 2
        assert len(get_req_json['data']) == get_req_json['per_page']

    def test_single_user(self):
        get_req = requests.get('https://reqres.in/api/users/2')
        get_req_json = get_req.json()
        assert get_req.status_code == 200
        assert get_req_json['data']['id'] == 2
        assert get_req_json['data']["first_name"] == "Janet"
        assert get_req_json['data']["last_name"] == "Weaver"

    def test_single_user_not_found(self):
        get_req = requests.get('https://reqres.in/api/users/23')
        get_req_json = get_req.json()
        assert get_req.status_code == 404
        assert get_req_json == {}

    def test_list_resource(self):
        get_req = requests.get('https://reqres.in/api/unknown')
        get_req_json = get_req.json()
        assert get_req.status_code == 200
        assert get_req_json['page'] == 1
        assert len(get_req_json['data']) == get_req_json['per_page']

    def test_single_resource(self):
        get_req = requests.get('https://reqres.in/api/unknown/2')
        get_req_json = get_req.json()
        assert get_req.status_code == 200
        assert get_req_json['data']['id'] == 2
        assert get_req_json['data']["name"] == "fuchsia rose"
        assert get_req_json['data']["year"] == 2001

    def test_single_resource_not_found(self):
        get_req = requests.get('https://reqres.in/api/unknown/23')
        get_req_json = get_req.json()
        assert get_req.status_code == 404
        assert get_req_json == {}

    def test_delayed_response(self):
        get_req = requests.get('https://reqres.in/api/users?delay=3')
        get_req_json = get_req.json()
        assert get_req.status_code == 200
        assert get_req_json['page'] == 1
        assert len(get_req_json['data']) == get_req_json['per_page']
        assert get_req_json['data'][0]['id'] == 1


class TestPostRequests:
    def test_create(self):
        post_req = requests.post('https://reqres.in/api/users?page=2', json={"name": "morpheus", "job": "leader"})
        post_req_json = post_req.json()
        print(post_req_json)
        assert post_req.status_code == 201
        assert post_req_json["name"] == "morpheus"
        assert post_req_json["job"] == "leader"

    def test_register_successful(self):
        post_req = requests.post('https://reqres.in/api/users?page=2',
                                 json={"email": "eve.holt@reqres.in", "password": "pistol"},
                                 headers={'Authorization': 'access_token QpwL5tke4Pnpja7X4'})
        post_req_json = post_req.json()
        print(post_req_json)
        assert post_req.status_code == 200

    def test_register_unsuccessful(self):
        post_req = requests.post('https://reqres.in/api/users?page=2', json={"email": "sydney@fife"})
        post_req_json = post_req.json()
        print(post_req_json)
        assert post_req.status_code == 404
        assert post_req_json["error"] == "Missing password"

