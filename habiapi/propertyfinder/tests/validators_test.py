"""Tests for validators module"""

import pytest

from propertyfinder.validators import validate_query_params
from propertyfinder.tests.test_data.query_param_test_data import QUERY_PARAM_TEST_DATA


@pytest.mark.parametrize("query_params, expected_result", QUERY_PARAM_TEST_DATA)
def test_validate_query_params(query_params, expected_result):
    """Test to validate all the posible query params. It includes valid and
    invalid query params
    """

    result = validate_query_params(query_params)

    assert result == expected_result
