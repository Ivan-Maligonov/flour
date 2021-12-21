import requests
import pytest



         # создаём свой заказ petID_400_negative (Postman)

            # petID прописываем буквами
def test_petID_400_negative():
    urlPost = "https://petstore.swagger.io/v2/store/order/"
    request = {}
    request['id'] = "33"
    request['petId'] = "BUBA"
    request['quantity'] = "60000000"
    request['shipDate'] = "2021-11-28T12:23:18.202Z"
    request['status'] = "stolen"
    request['complete'] = "True"
    print("request", request)

    conclusionPOST = requests.post(urlPost, json=request)
    print("conclusionPOST", conclusionPOST.json())

              # Проверяем, что вернулся не пустой id
    assert conclusionPOST.json()['id'] is not None
             # Проверяем, что статус заказа ответа совпало с статусом заказа запроса
    assert conclusionPOST.json()['status'] == request['status']


    # тест посыпался, заказ не создаётся, так как petID может быть только числовым значением
    # при этом в Postman ошибка 400, тут 500