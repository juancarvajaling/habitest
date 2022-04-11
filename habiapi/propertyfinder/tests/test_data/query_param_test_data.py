QUERY_PARAM_TEST_DATA = [
    [
        {"year": "a year", "city": "medellin", "status": "en_venta"},
        {
            "is_ok": False,
            "result": [{
                "loc": ["year"],
                "msg": "value is not a valid integer",
                "type": "type_error.integer"
            }]
        }
    ],
    [
        {"year": "1800", "city": "medellin", "status": "en_venta"},
        {
            "is_ok": False,
            "result": [{
                "loc": ["year"],
                "msg": "ensure this value is greater than 1900",
                "type": "value_error.number.not_gt",
                "ctx": {"limit_value": 1900}
            }]
        }
    ],
    [
        {"year": "2022", "city": "medellin", "status": "a status"},
        {
            "is_ok": False,
            "result": [{
                "loc": ["status"],
                "msg": "value is not a valid enumeration member; permitted: 'pre_venta', 'en_venta', 'vendido'",
                "type": "type_error.enum",
                "ctx": {"enum_values": ["pre_venta", "en_venta", "vendido"]}
            }]
        }
    ],
    [
        {"city": "medellin", "status": "vendido"},
        {
            "is_ok": True,
            "result": {"year": None, "city": "medellin", "status": "vendido"}
        }
    ],
    [
        {"year": "2022", "status": "vendido"},
        {
            "is_ok": True,
            "result": {"year": 2022, "city": None, "status": "vendido"}
        }
    ],
    [
        {"year": "2022", "city": "medellin"},
        {
            "is_ok": True,
            "result": {"year": 2022, "city": "medellin", "status": None}
        }
    ]
]
