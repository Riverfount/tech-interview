import json

from django.test import Client
from django.urls import reverse
from pytest import fixture

client = Client()


@fixture
def payload():
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
def result():
    return {"carts": [{"id": 1, "total": 2000}, {"id": 2, "total": 1400}, {"id": 3, "total": 0}]}


def test_level1_status_code_ok(payload):
    """Checks if the endpoint responds 200 Ok"""
    response = client.post(reverse('level1'), json.dumps(payload), content_type="application/json")
    assert response.status_code == 200


def test_level1_works_properly(payload, result):
    """Checks if the endpoint returns correctly"""
    response = client.post(reverse('level1'), json.dumps(payload), content_type="application/json")
    assert json.loads(response.getvalue().decode('utf-8')) == result


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
