

def calculation(payload):
    total_amount = 0
    for tax in taxes:
        total_amount = total_amount + tax["etH_AMOUNT_PAID"]
    print(total_amount)
    return {
        "total": total_amount
    }


if __name__ == '__main__':
    payload = {
    "status": 0,
    "message": "Record found.",
    "data": {
        "etranS_ID": 12813171,
        "dues": [
            {
                "taT_NAME": "MOTOR VEHICLE TAX",
                "etH_AMOUNT_PAID": 1800.0
            },
            {
                "taT_NAME": "INCOME TAX",
                "etH_AMOUNT_PAID": 5000.0
            },
            {
                "taT_NAME": "PROFESSIONAL TAX",
                "etH_AMOUNT_PAID": 400.0
            },
            {
                "taT_NAME": "MOTOR VEHCILE TAX ARREARS",
                "etH_AMOUNT_PAID": 1800.0
            },
            {
                "taT_NAME": "MISCELLANEOUS",
                "etH_AMOUNT_PAID": 0.0
            },
            {
                "taT_NAME": "EPAYMENT DISCOUNT",
                "etH_AMOUNT_PAID": -90.0
            }
        ]
    }
}
    taxes = payload["data"]["dues"]
    # print(taxes)
    calculation(taxes)