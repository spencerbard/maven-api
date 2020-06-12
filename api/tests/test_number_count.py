""" Tests the number count blueprint. """
import json

from api.routes import INVALID_MSG_NUM, INVALID_MSG_INC, INVALID_MSG_NUM_DNE


def test_post_invalid(client):
    """ Test post route response with invalid data body. """
    resp = client.post("/", json={"number": "invalid"})
    data = json.loads(resp.data)
    assert resp.status_code == 400
    assert data == INVALID_MSG_NUM
    resp = client.post("/", json={"num": 1})
    data = json.loads(resp.data)
    assert resp.status_code == 400
    assert data == INVALID_MSG_NUM


def test_post_valid(client):
    """ Test post route response with valid data body. """

    def assert_post_inc(number, expected):
        """ Assert that incrementing by number occurs as expected. """
        resp = client.post("/", json={"number": number})
        assert resp.status_code == 200
        data = json.loads(resp.data)
        assert "number" in data
        assert data["number"] == number
        assert "count" in data
        assert data["count"] == expected

    assert_post_inc(1, 1)
    assert_post_inc(1, 2)
    assert_post_inc(2, 1)
    assert_post_inc(1, 3)
    assert_post_inc(0, 1)
    assert_post_inc(0, 2)
    assert_post_inc(-1, 1)
    assert_post_inc(-1, 2)


def test_put_invalid(client):
    """ Test put route response with invalid data body. """

    def assert_put_inc_invalid(put_data, msg):
        resp = client.put("/", json=put_data)
        data = json.loads(resp.data)
        assert resp.status_code == 400
        assert data == msg

    assert_put_inc_invalid({"number": "invalid", "increment_value": 1}, INVALID_MSG_NUM)
    assert_put_inc_invalid(
        {"number": 1, "increment_value": 2}, INVALID_MSG_NUM_DNE.format(1)
    )
    client.post("/", json={"number": 1})
    assert_put_inc_invalid({"number": 1}, INVALID_MSG_INC)
    assert_put_inc_invalid({"number": 1, "increment_value": "invalid"}, INVALID_MSG_INC)
    assert_put_inc_invalid({"number": 1, "inc_value": 1}, INVALID_MSG_INC)
    assert_put_inc_invalid({"number": 1, "increment_value": -1}, INVALID_MSG_INC)


def test_put_valid(client):
    """ Test put route response with valid data body. """

    def assert_put_inc(number, increment_value, expected):
        """ Assert that incrementing by number occurs as expected. """
        resp = client.put(
            "/", json={"number": number, "increment_value": increment_value}
        )
        assert resp.status_code == 200
        data = json.loads(resp.data)
        assert "number" in data
        assert data["number"] == number
        assert "count" in data
        assert data["count"] == expected

    client.post("/", json={"number": -1})
    client.post("/", json={"number": 0})
    client.post("/", json={"number": 1})
    assert_put_inc(-1, 2, 3)
    assert_put_inc(0, 200, 201)
    assert_put_inc(1, 0, 1)
