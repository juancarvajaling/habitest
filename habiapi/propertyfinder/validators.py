"""
Module to validate incoming request data to find properties.
"""
import json
from enum import Enum

from pydantic import BaseModel, ValidationError, conint
from typing import Optional


class StatusEnum(str, Enum):
    """
    Set the posible values for status query param.
    """
    pre_venta = "pre_venta"
    en_venta = "en_venta"
    vendido = "vendido"


class QueryParamsValidator(BaseModel):
    """
    Class used to validate incoming query params.
    """
    year: Optional[conint(gt=1900)]
    city: Optional[str]
    status: Optional[StatusEnum]


def validate_query_params(query_params: dict) -> dict:
    """
    Validates query params to get the proper fields and values.

    :param dict query_params: dictionary with the query params to validate. It
        should only have 'year', 'city', and 'status' fields.

    :return dictionary with validation result
    """

    try:
        query_params_validated = QueryParamsValidator(**query_params)
    except ValidationError as error:
        return {"is_ok": False, "result": json.loads(error.json())}

    return {"is_ok": True, "result": json.loads(query_params_validated.json())}
