import requests
import pytest

 # смотрим список статусов заказов
def test_checking_the_leftovers_get_positive():
    url = "https://petstore.swagger.io/v2/store/inventory/"
    response = requests.get(url)
    print(response.json())