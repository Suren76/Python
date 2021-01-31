import requests


def test_put():
    req_before = requests.put('https://reqres.in/api/users/2')
    put_req = requests.put('https://reqres.in/api/users/2', json={"name": "morpheus", "job": "zion resident"})
    put_req_json = put_req.json()
    #print(put_req_json, "\n")
    assert put_req.status_code == 200
    assert put_req_json != req_before.json()
    assert put_req_json["name"] == "morpheus"
    assert put_req_json["job"] == "zion resident"


def test_delete():
    req_before = requests.get('https://reqres.in/api/users/2')
    delete_req = requests.delete('https://reqres.in/api/users/2')
    delete_req_data = delete_req.text
    assert delete_req.status_code == 204
    assert delete_req_data != req_before.json()
    assert delete_req_data == ''
