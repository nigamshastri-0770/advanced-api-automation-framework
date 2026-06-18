booking_schema = {

    "type": "object",

    "properties": {

        "bookingid": {
            "type": "integer"
        },

        "booking": {

            "type": "object",

            "properties": {

                "firstname": {
                    "type": "string"
                },

                "lastname": {
                    "type": "string"
                },

                "totalprice": {
                    "type": "integer"
                },

                "depositpaid": {
                    "type": "boolean"
                }

            },

            "required": [

                "firstname",

                "lastname",

                "totalprice",

                "depositpaid"
            ]
        }
    },

    "required": [

        "bookingid",

        "booking"
    ]
}