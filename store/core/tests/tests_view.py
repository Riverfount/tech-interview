import json

from django.test import Client
from django.urls import reverse
from pytest import fixture

client = Client()


# Tests Views for the Level 1 of the Tech Interview


@fixture
def payload_level1():
    return {
        "articles": [
            {"id": 1, "name": "water", "price": 100},
            {"id": 2, "name": "honey", "price": 200},
            {"id": 3, "name": "mango", "price": 400},
            {"id": 4, "name": "tea", "price": 1000},
        ],
        "carts": [
            {
                "id": 1,
                "items": [
                    {"article_id": 1, "quantity": 6},
                    {"article_id": 2, "quantity": 2},
                    {"article_id": 4, "quantity": 1},
                ],
            },
            {"id": 2, "items": [{"article_id": 2, "quantity": 1}, {"article_id": 3, "quantity": 3}]},
            {"id": 3, "items": []},
        ],
    }


@fixture
def result_level1():
    return {"carts": [{"id": 1, "total": 2000}, {"id": 2, "total": 1400}, {"id": 3, "total": 0}]}


def test_level1_status_code_ok(payload_level1):
    """Checks if the endpoint responds 200 Ok"""
    response = client.post(reverse('level1'), json.dumps(payload_level1), content_type="application/json")
    assert response.status_code == 200


def test_level1_works_properly(payload_level1, result_level1):
    """Checks if the endpoint returns correctly"""
    response = client.post(reverse('level1'), json.dumps(payload_level1), content_type="application/json")
    assert json.loads(response.getvalue().decode('utf-8')) == result_level1


def test_level1_raise_error_method_not_allowded():
    expected = [{"Error": {"Message": "Method not allowed"}}]
    response = client.get(reverse('level1'), content_type='application/json')
    assert json.loads(response.getvalue().decode('utf-8')) == expected


def test_leve1_returns_correct_error_message_when_payload_is_empty():
    """Checks the message error if payload was forgoten"""
    payload = {}
    expected = [{"Error": {"Message": "The payload is not present on the request."}}]
    resp = client.post(reverse('level1'), json.dumps(payload), content_type="application/json")

    assert json.loads(resp.getvalue().decode('utf-8')) == expected


def test_leve1_returns_correct_error_message_when_payload_no_have_articles():
    """Checks the message error if payload doesn't have the articles"""
    payload = {"carts": [{"id": 1, "total": 2000}]}
    expected = [{"Error": {"Message": "The follow keys ('articles',) were not present on payload."}}]
    resp = client.post(reverse('level1'), json.dumps(payload), content_type="application/json")

    assert json.loads(resp.getvalue().decode('utf-8')) == expected


def test_leve1_returns_correct_error_message_when_payload_no_have_carts():
    """Checks the message error if payload doesn't have the carts"""
    payload = {"articles": [{"id": 1, "name": "water", "price": 100}]}
    expected = [{"Error": {"Message": "The follow keys ('carts',) were not present on payload."}}]
    resp = client.post(reverse('level1'), json.dumps(payload), content_type="application/json")

    assert json.loads(resp.getvalue().decode('utf-8')) == expected


# Tests Views for the Level 2 of the Tech Interview


@fixture
def payload_level2():
    return {
        "articles": [
            {"id": 1, "name": "water", "price": 100},
            {"id": 2, "name": "honey", "price": 200},
            {"id": 3, "name": "mango", "price": 400},
            {"id": 4, "name": "tea", "price": 1000},
        ],
        "carts": [
            {
                "id": 1,
                "items": [
                    {"article_id": 1, "quantity": 6},
                    {"article_id": 2, "quantity": 2},
                    {"article_id": 4, "quantity": 1},
                ],
            },
            {"id": 2, "items": [{"article_id": 2, "quantity": 1}, {"article_id": 3, "quantity": 3}]},
            {"id": 3, "items": []},
        ],
        "delivery_fees": [
            {"eligible_transaction_volume": {"min_price": 0, "max_price": 1000}, "price": 800},
            {"eligible_transaction_volume": {"min_price": 1000, "max_price": 2000}, "price": 400},
            {"eligible_transaction_volume": {"min_price": 2000, "max_price": None}, "price": 0},
        ],
    }


@fixture
def result_level2():
    return {"carts": [{"id": 1, "total": 2000}, {"id": 2, "total": 1800}, {"id": 3, "total": 800}]}


def test_level2_status_code_ok(payload_level2):
    """Checks if the endpoint responds 200 Ok"""
    response = client.post(reverse('level2'), json.dumps(payload_level2), content_type="application/json")
    assert response.status_code == 200


def test_level2_works_properly(payload_level2, result_level2):
    """Checks if the endpoint returns correctly"""
    response = client.post(reverse('level2'), json.dumps(payload_level2), content_type="application/json")
    assert json.loads(response.getvalue().decode('utf-8')) == result_level2


def test_level2_raise_error_method_not_allowded():
    expected = [{"Error": {"Message": "Method not allowed"}}]
    response = client.get(reverse('level2'), content_type='application/json')
    assert json.loads(response.getvalue().decode('utf-8')) == expected


def test_level2_returns_correct_error_message_when_payload_is_empty():
    """Checks the message error if payload was forgoten"""
    payload = {}
    expected = [{"Error": {"Message": "The payload is not present on the request."}}]
    resp = client.post(reverse('level2'), json.dumps(payload), content_type="application/json")

    assert json.loads(resp.getvalue().decode('utf-8')) == expected


def test_level2_returns_correct_error_message_when_payload_no_have_articles():
    """Checks the message error if payload doesn't have the articles"""
    payload = {
        "carts": [{"id": 1, "total": 2000}],
        "delivery_fees": [{"eligible_transaction_volume": {"min_price": 0, "max_price": 1000}, "price": 800}],
    }
    expected = [{"Error": {"Message": "The follow keys ('articles',) were not present on payload."}}]
    resp = client.post(reverse('level2'), json.dumps(payload), content_type="application/json")

    assert json.loads(resp.getvalue().decode('utf-8')) == expected


def test_leve2_returns_correct_error_message_when_payload_no_have_carts():
    """Checks the message error if payload doesn't have the carts"""
    payload = {
        "articles": [{"id": 1, "name": "water", "price": 100}],
        "delivery_fees": [{"eligible_transaction_volume": {"min_price": 0, "max_price": 1000}, "price": 800}],
    }
    expected = [{"Error": {"Message": "The follow keys ('carts',) were not present on payload."}}]
    resp = client.post(reverse('level2'), json.dumps(payload), content_type="application/json")

    assert json.loads(resp.getvalue().decode('utf-8')) == expected


def test_level2_returns_correct_error_message_when_payload_no_have_delivery_fees():
    """Checks the message error if payload doesn't have the delivery fees"""
    payload = {
        "articles": [{"id": 1, "name": "water", "price": 100}],
        "carts": [{"id": 1, "total": 2000}],
    }
    expected = [{"Error": {"Message": "The follow keys ('delivery_fees',) were not present on payload."}}]
    resp = client.post(reverse('level2'), json.dumps(payload), content_type="application/json")

    assert json.loads(resp.getvalue().decode('utf-8')) == expected


# Tests Views for the Level 3 of the Tech Interview


@fixture
def payload_level3():
    return {
        "articles": [
            {"id": 1, "name": "water", "price": 100},
            {"id": 2, "name": "honey", "price": 200},
            {"id": 3, "name": "mango", "price": 400},
            {"id": 4, "name": "tea", "price": 1000},
            {"id": 5, "name": "ketchup", "price": 999},
            {"id": 6, "name": "mayonnaise", "price": 999},
            {"id": 7, "name": "fries", "price": 378},
            {"id": 8, "name": "ham", "price": 147},
        ],
        "carts": [
            {
                "id": 1,
                "items": [
                    {"article_id": 1, "quantity": 6},
                    {"article_id": 2, "quantity": 2},
                    {"article_id": 4, "quantity": 1},
                ],
            },
            {"id": 2, "items": [{"article_id": 2, "quantity": 1}, {"article_id": 3, "quantity": 3}]},
            {"id": 3, "items": [{"article_id": 5, "quantity": 1}, {"article_id": 6, "quantity": 1}]},
            {"id": 4, "items": [{"article_id": 7, "quantity": 1}]},
            {"id": 5, "items": [{"article_id": 8, "quantity": 3}]},
        ],
        "delivery_fees": [
            {"eligible_transaction_volume": {"min_price": 0, "max_price": 1000}, "price": 800},
            {"eligible_transaction_volume": {"min_price": 1000, "max_price": 2000}, "price": 400},
            {"eligible_transaction_volume": {"min_price": 2000, "max_price": None}, "price": 0},
        ],
        "discounts": [
            {"article_id": 2, "type": "amount", "value": 25},
            {"article_id": 5, "type": "percentage", "value": 30},
            {"article_id": 6, "type": "percentage", "value": 30},
            {"article_id": 7, "type": "percentage", "value": 25},
            {"article_id": 8, "type": "percentage", "value": 10},
        ],
    }


@fixture
def result_level3():
    return {
        "carts": [
            {"id": 1, "total": 2350},
            {"id": 2, "total": 1775},
            {"id": 3, "total": 1798},
            {"id": 4, "total": 1083},
            {"id": 5, "total": 1196},
        ]
    }


def test_level3_status_code_ok(payload_level3):
    """Checks if the endpoint responds 200 Ok"""
    response = client.post(reverse('level3'), json.dumps(payload_level3), content_type="application/json")
    assert response.status_code == 200


def test_level3_works_properly(payload_level3, result_level3):
    """Checks if the endpoint returns correctly"""
    response = client.post(reverse('level3'), json.dumps(payload_level3), content_type="application/json")
    assert json.loads(response.getvalue().decode('utf-8')) == result_level3


def test_level3_raise_error_method_not_allowded():
    expected = [{"Error": {"Message": "Method not allowed"}}]
    response = client.get(reverse('level3'), content_type='application/json')
    assert json.loads(response.getvalue().decode('utf-8')) == expected


def test_level3_returns_correct_error_message_when_payload_is_empty():
    """Checks the message error if payload was forgoten"""
    payload = {}
    expected = [{"Error": {"Message": "The payload is not present on the request."}}]
    resp = client.post(reverse('level3'), json.dumps(payload), content_type="application/json")

    assert json.loads(resp.getvalue().decode('utf-8')) == expected


def test_level3_returns_correct_error_message_when_payload_no_have_articles():
    """Checks the message error if payload doesn't have the articles"""
    payload = {
        "carts": [{"id": 1, "total": 2000}],
        "delivery_fees": [{"eligible_transaction_volume": {"min_price": 0, "max_price": 1000}, "price": 800}],
        "discounts": [{"article_id": 2, "type": "amount", "value": 25}],
    }
    expected = [{"Error": {"Message": "The follow keys ('articles',) were not present on payload."}}]
    resp = client.post(reverse('level3'), json.dumps(payload), content_type="application/json")

    assert json.loads(resp.getvalue().decode('utf-8')) == expected


def test_leve3_returns_correct_error_message_when_payload_no_have_carts():
    """Checks the message error if payload doesn't have the carts"""
    payload = {
        "articles": [{"id": 1, "name": "water", "price": 100}],
        "delivery_fees": [{"eligible_transaction_volume": {"min_price": 0, "max_price": 1000}, "price": 800}],
        "discounts": [{"article_id": 2, "type": "amount", "value": 25}],
    }
    expected = [{"Error": {"Message": "The follow keys ('carts',) were not present on payload."}}]
    resp = client.post(reverse('level3'), json.dumps(payload), content_type="application/json")

    assert json.loads(resp.getvalue().decode('utf-8')) == expected


def test_level3_returns_correct_error_message_when_payload_no_have_delivery_fees():
    """Checks the message error if payload doesn't have the delivery fees"""
    payload = {
        "articles": [{"id": 1, "name": "water", "price": 100}],
        "carts": [{"id": 1, "total": 2000}],
        "discounts": [{"article_id": 2, "type": "amount", "value": 25}],
    }
    expected = [{"Error": {"Message": "The follow keys ('delivery_fees',) were not present on payload."}}]
    resp = client.post(reverse('level3'), json.dumps(payload), content_type="application/json")

    assert json.loads(resp.getvalue().decode('utf-8')) == expected


def test_level3_returns_correct_error_message_when_payload_no_have_discounts():
    """Checks the message error if payload doesn't have the discounts"""
    payload = {
        "articles": [{"id": 1, "name": "water", "price": 100}],
        "carts": [{"id": 1, "total": 2000}],
        "delivery_fees": [{"eligible_transaction_volume": {"min_price": 0, "max_price": 1000}, "price": 800}],
    }
    expected = [{"Error": {"Message": "The follow keys ('discounts',) were not present on payload."}}]
    resp = client.post(reverse('level3'), json.dumps(payload), content_type="application/json")

    assert json.loads(resp.getvalue().decode('utf-8')) == expected
