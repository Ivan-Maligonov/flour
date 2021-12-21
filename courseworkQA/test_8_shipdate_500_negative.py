import requests
import pytest



         # создаём свой заказ shipDate_500_negative (Postman)

            # shipDate так как создаём сами, то "случайно" делаем ощибку
def test_shipDate_500_negative():
    urlPost = "https://petstore.swagger.io/v2/store/order/"
    request = {}
    request['id'] = ""
    request['petId'] = "28112021"
    request['quantity'] = "60000000"
    request['shipDate'] = "2018-10-335T12:23:18.202Z"
    request['status'] = "stolen"
    request['complete'] = "True"
    print("request", request)

    conclusionPOST = requests.post(urlPost, json=request)
    print("conclusionPOST", conclusionPOST.json())

              # Проверяем, что вернулся не пустой id
    assert conclusionPOST.json()['id'] is not None
             # Проверяем, что статус заказа ответа совпало с статусом заказа запроса
    assert conclusionPOST.json()['status'] == request['status']


    # тест посыпался, заказ не создаётся, так как shipDate не корректная дата
    # ошибка 500