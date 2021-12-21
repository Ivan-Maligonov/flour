import requests
import pytest



         # создаём свой заказ order_id_-2_negative (Postman)

            # присваиваем id отрицательное значение

def test_order_id_negative():
    urlPost = "https://petstore.swagger.io/v2/store/order/"
    request = {}
    request['id'] = "-2"
    request['petId'] = "28112021"
    request['quantity'] = "60000000"
    request['shipDate'] = "2021-11-25T12:23:18.202Z"
    request['status'] = "stolen"
    request['complete'] = "True"
    print("request", request)

    conclusionPOST = requests.post(urlPost, json=request)
    print("conclusionPOST", conclusionPOST.json())
    global order
    order = conclusionPOST.json()

    # Проверяем, что вернулся не пустой id
    assert conclusionPOST.json()['id'] is not None
    # Проверяем, что статус заказа ответа совпало с статусом заказа запроса
    assert conclusionPOST.json()['status'] == request['status']

    while conclusionPOST.json()['id'] != request['id']:
        print("Значение ID созднанного объекта не соответствует заданному параметру")
        break

    assert conclusionPOST.json()['id'] == request['id']

    # наблюдаем что отризацельное значение ID приравневается к его отсутствию и данный параметр генерируется автоматически

def test_get_order():
    urlGet = "https://petstore.swagger.io/v2/store/order/" + str(order['id'])
    print("urlGet = ", urlGet)
    conclusionGet = requests.get(urlGet)
    print("conclusion Get= ", conclusionGet.json())

    while conclusionGet.status_code == 200:
        print("Всё отлично")
        break
    else:
        conclusionGet = requests.get(urlGet)
        print("Повторяем")
        print("conclusion Get= ", conclusionGet.json())
    assert conclusionGet.json()['id'] == order['id']
    assert conclusionGet.json()['status'] == order['status']

   