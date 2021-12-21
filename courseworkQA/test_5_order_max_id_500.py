import requests
import pytest

         # создаём свой заказ order_max_id_500 (Postman)
         # В ходе тестирования был вычеслен максимальный id, а именно было замеченно, что автоматически присваивается посттоянно один и тот же, и к нему добавили +1
         # по итогу наш id 9223372036854775808

def test_order_max_id_500():
    urlPost = "https://petstore.swagger.io/v2/store/order/"
    request = {}
    request['id'] = "9223372036854775808"
    request['petId'] = "28112021"
    request['quantity'] = "1000"
    request['shipDate'] = "2021-11-28T12:23:18.202Z"
    request['status'] = "Местный"
    request['complete'] = "True"
    print("request", request)

    conclusionPOST = requests.post(urlPost, json=request)
    print("conclusionPOST", conclusionPOST.json())


              # Проверяем, что вернулся не пустой id
    assert conclusionPOST.json()['id'] is not None
             # Проверяем, что статус заказа ответа совпало с статусом заказа запроса
    assert conclusionPOST.json()['status'] == request['status']

  # тест завален, ошибка 500
