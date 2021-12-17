import requests
import pytest

def test_DZ_post():
   # Создаём
    urlPost = "https://petstore.swagger.io/v2/pet"
    request = {}
    request['id'] = "14122021"
    request['name'] = "Buba"
    request['category'] = {}
    request['category']['id'] = "212021"
    request['category']['name'] = "domovoy"
    request['photoUrls'] = ['photoBuba']
    request['tags'] = [{}]
    request['tags'][0]["id"] = 25
    request['tags'][0]["name"] = "tadDomovoy"
    request['status'] = "sold"
    print("request", request)

    conclusionPOST = requests.post(urlPost, json=request)

    print("response", conclusionPOST.json())
    # Проверяем, что вернулся не пустой id
    assert conclusionPOST.json()['id'] is not None
    # Проверяем, что имя ответа совпало с именем запроса
    assert conclusionPOST.json()['name'] == request['name']

   # проверяем

    urlGet = "https://petstore.swagger.io/v2/pet/" + str(conclusionPOST.json()['id'])
    print("urlGet = ", urlGet)
    conclusionGet = requests.get(urlGet)
    print("conclusion Get= ", conclusionGet.json())

    assert conclusionGet.json()['id'] == conclusionPOST.json()['id']
    assert conclusionGet.json()['name'] == request['name']

   # Удаляем
    urlDel = "https://petstore.swagger.io/v2/pet/" + str(conclusionPOST.json()['id'])
    print("urlDel = ", urlDel)
    conclusionDel = requests.delete(urlDel)
    print("conclusion DEL= ", conclusionDel.json())

    assert conclusionDel.json()['code'] == 200

    urlGet = "https://petstore.swagger.io/v2/pet/" + str(conclusionPOST.json()['id'])
    print("urlGet = ", urlGet)
    conclusionGet = requests.get(urlGet)
    print("conclusion Get= ", conclusionGet.json())
    assert conclusionGet.json()['message'] == "Pet not found"