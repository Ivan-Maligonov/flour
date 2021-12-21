import requests
import pytest



         # создаём свой заказ order_Russian (Postman)
def test_order_POST_rus_status():
    urlPost = "https://petstore.swagger.io/v2/store/order/"
    request = {}
    request['id'] = "2525"
    request['petId'] = "28112021"
    request['quantity'] = "1000"
    request['shipDate'] = "2021-11-28T12:23:18.202Z"
    request['status'] = "Местный"
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

    while conclusionPOST.json()['status'] == request['status']:
        print("ОШИБКА!!! В базе заложенны статусы [placed, approved, delivered]")
        break
    assert conclusionPOST.json()['status'] == ['placed', 'approved', 'delivered']

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

   #удаляем созданный ранее заказ del_order_Russian Postman
def test_Delete_POST_rus_status():
    urlDel = "https://petstore.swagger.io/v2/store/order/" + str(order['id'])
    print("urlDel = ", urlDel)
    conclusionDel = requests.delete(urlDel)
    print("conclusion DEL= ", conclusionDel.json())

    while conclusionDel.status_code == 200:
        print("Всё отлично")
        break
    else:
        conclusionDel = requests.delete(urlDel)
        print("Повторяем")
        print("conclusion DEL= ", conclusionDel.json())
    assert conclusionDel.json()['code'] == 200
    assert conclusionDel.json()['message'] == '2525'



  # проверяем после удаления
def test_get_after_del():
    urlGet = "https://petstore.swagger.io/v2/store/order/" + str(order['id'])
    print("urlGet = ", urlGet)
    conclusionGet = requests.get(urlGet)
    print("conclusion Get= ", conclusionGet.json())

    assert conclusionGet.json()['message'] == "Order not found"
