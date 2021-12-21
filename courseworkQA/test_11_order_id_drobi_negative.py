import requests
import pytest


# создаём свой заказ order_2.2_negative (Postman), order_2.9_negative (Postman), order_5,5_(negative 400) (Postman)

 # присваиваем id дробное значение через точку

def test_order_id_2_2_negative():
    urlPost = "https://petstore.swagger.io/v2/store/order/"
    request = {}
    request['id'] = "2.2"                               # order_2.2_negative (Postman)
    request['petId'] = "5"
    request['quantity'] = "6"
    request['shipDate'] = "2021-11-25T12:23:18.202Z"
    request['status'] = "stolen"
    request['complete'] = "True"
    print("request", request)

    conclusionPOST = requests.post(urlPost, json=request)
    print("conclusionPOST", conclusionPOST.json())

    # Проверяем, что вернулся не пустой id
    assert conclusionPOST.json()['id'] is not None

     # Видим что тест провален и ошибка 500, что забавно т.к. в Postman, данный тест проходит
    # и все не целые значения округляются до наименьшего целого, т.е. в данном случае id было бы равно 2


def test_order_2_9_negative():
        urlPost = "https://petstore.swagger.io/v2/store/order/"
        request = {}
        request['id'] = "2.9"                                            # order_2.9_negative (Postman)
        request['petId'] = "5"
        request['quantity'] = "6"
        request['shipDate'] = "2021-11-25T12:23:18.202Z"
        request['status'] = "stolen"
        request['complete'] = "True"
        print("request", request)

        conclusionPOST = requests.post(urlPost, json=request)
        print("conclusionPOST", conclusionPOST.json())

        # Проверяем, что вернулся не пустой id
        assert conclusionPOST.json()['id'] is not None

        # Видим что тест провален и ошибка 500, что забавно т.к. в Postman, данный тест проходит
        # и все не целые значения округляются до наименьшего целого, т.е. в данном случае id было бы равно 2


# присваиваем id дробное значение через запятаю
def test_order_id_5_5_negative():
    urlPost = "https://petstore.swagger.io/v2/store/order/"
    request = {}
    request['id'] = "5,5"                                           # order_5,5_(negative 400)
    request['petId'] = "5"
    request['quantity'] = "6"
    request['shipDate'] = "2021-11-25T12:23:18.202Z"
    request['status'] = "stolen"
    request['complete'] = "True"
    print("request", request)

    conclusionPOST = requests.post(urlPost, json=request)
    print("conclusionPOST", conclusionPOST.json())

    # Проверяем, что вернулся не пустой id
    assert conclusionPOST.json()['id'] is not None
     # ошибка 500, видим, что тест сыпется, т.к. значение id должно быть целочисленным,
    # но в Postman приходит ошибка 400


# присваиваем petid дробное значение через точку

def test_order_petid_drobi_negative():
    urlPost = "https://petstore.swagger.io/v2/store/order/"
    request = {}
    request['id'] = "7"                               # order_2.2_negative (Postman)
    request['petId'] = "4.7"
    request['quantity'] = "6"
    request['shipDate'] = "2021-11-25T12:23:18.202Z"
    request['status'] = "stolen"
    request['complete'] = "True"
    print("request", request)

    conclusionPOST = requests.post(urlPost, json=request)
    print("conclusionPOST", conclusionPOST.json())

    # Проверяем, что вернулся не пустой id
    assert conclusionPOST.json()['id'] is not None

     # Видим что тест провален и ошибка 500, что забавно т.к. в Postman, данный тест проходит
    # и все не целые значения округляются до наименьшего целого, т.е. в данном случае petID было бы равно 4


# присваиваем quantity дробное значение через точку
def test_order_quantity_drobi_negative():
    urlPost = "https://petstore.swagger.io/v2/store/order/"
    request = {}
    request['id'] = "7"                               # order_2.2_negative (Postman)
    request['petId'] = "5"
    request['quantity'] = "8.2"
    request['shipDate'] = "2021-11-25T12:23:18.202Z"
    request['status'] = "stolen"
    request['complete'] = "True"
    print("request", request)

    conclusionPOST = requests.post(urlPost, json=request)
    print("conclusionPOST", conclusionPOST.json())

    # Проверяем, что вернулся не пустой id
    assert conclusionPOST.json()['id'] is not None

     # Видим что тест провален и ошибка 500, что забавно т.к. в Postman, данный тест проходит
    # и все не целые значения округляются до наименьшего целого, т.е. в данном случае quantity было бы равно 8