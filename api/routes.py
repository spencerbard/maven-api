""" routes for flask api """
from flask import Blueprint, request, jsonify

from api import DB
from api.models import NumberCount


NUMBER_COUNT = Blueprint("number_count", __name__, template_folder="templates")
KEY_NUM = "number"
KEY_INC = "increment_value"
KEY_COUNT = "count"
INVALID_MSG_NUM = f"Request body must contain a key {KEY_NUM} with an integer value"
INVALID_MSG_INC = (
    f"Request body must contain a key {KEY_INC} with a non-negative integer value"
)
INVALID_MSG_NUM_DNE = (
    "Cannot perform `PUT` for number: {0}. Number: {0} does not exist in database."
)


@NUMBER_COUNT.route("/jello")
def jello():
    """ Test api is up. """
    return "jello!"


def get_int_val_from_dict(from_dict, key):
    """ Validate, extract, and transform int value keyed by `key` from dict.

    Args:
        from_dict (dict): dict from which to extract integer value
        key (str): key within from_dict from which integer value should be
    Returns:
        (int | None): int if request data is correctly formed, else None
    """
    if from_dict and isinstance(from_dict, dict) and key in from_dict:
        try:
            return int(from_dict[key])
        except ValueError:
            return None
    return None


def ret_number_count(number_count_obj):
    """ Return formatted number count response.

    Args:
        (number_count_obj): NumberCount obj from which to extract data for response
    Returns:
        (dict): obj with "number" and "count" keys extract from number_count_obj
    """
    return jsonify(
        {KEY_NUM: number_count_obj.number, KEY_COUNT: number_count_obj.count}
    )


@NUMBER_COUNT.route("/", methods=["POST", "PUT"])
def inc_post():
    """ Increment `number` from post data by one. """
    request_data = request.get_json()
    number = get_int_val_from_dict(request_data, KEY_NUM)
    inc_val = 1
    if number is None:
        return jsonify(INVALID_MSG_NUM), 400
    number_count_obj = (
        DB.session.query(NumberCount).filter(NumberCount.number == number).first()
    )
    if request.method == "PUT":
        if number_count_obj is None:
            return jsonify(INVALID_MSG_NUM_DNE.format(number)), 400
        inc_val = get_int_val_from_dict(request_data, KEY_INC)
        if inc_val is None or inc_val < 0:
            return jsonify(INVALID_MSG_INC), 400
    if not number_count_obj:
        number_count_obj = NumberCount(number=number, count=1)
        DB.session.add(number_count_obj)
        DB.session.commit()
    else:
        number_count_obj.count += inc_val
        DB.session.commit()
    return ret_number_count(number_count_obj)
