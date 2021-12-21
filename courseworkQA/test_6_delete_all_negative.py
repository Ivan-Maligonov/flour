import requests
import pytest



         # создаём свой заказ delete_all_(negative) (Postman)

def test_delete_all_negative():
    urlPost = "https://petstore.swagger.io/v2/store/order/"
    request = {}
    print("request", request)

    conclusionPOST = requests.post(urlPost, json=request)
    print("conclusionPOST", conclusionPOST.json())
    global order
    order = conclusionPOST.json()

              # Проверяем, что вернулся не пустой id
    assert conclusionPOST.json()['id'] is not None


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

  # В ответе видим, что id сгенерирован автоматически, а так же создались поля 'petId': 0, 'quantity': 0, 'complete': False
  # Проблема такого заказа, что он будет лишь мешать в реально базе данных, пустышка на которую нужно тратить время