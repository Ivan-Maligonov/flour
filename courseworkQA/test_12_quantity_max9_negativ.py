import requests
import pytest


         # создаём свой заказ quantity_max9_negativ (Postman)

def test_quantity_max9_negativ():
    urlPost = "https://petstore.swagger.io/v2/store/order/"
    request = {}
    request['id'] = "2"
    request['petId'] = "28112021"
    request['quantity'] = "11666666666"
    request['shipDate'] = "2021-11-28T12:23:18.202Z"
    request['status'] = "stolen"
    request['complete'] = "True"
    print("request", request)

    conclusionPOST = requests.post(urlPost, json=request)
    print("conclusionPOST", conclusionPOST.json())


              # Проверяем, что вернулся не пустой id
    assert conclusionPOST.json()['id'] is not None
             # Проверяем, что количество заказа ответа совпало с количеством заказа запроса
    assert conclusionPOST.json()['quantity'] == request['quantity']

 # Как мы видим данный заказ не был создан, так как максимальная длинна значения quantity составляет 10 знаков, у нас 11
 # код 500 и в Postman