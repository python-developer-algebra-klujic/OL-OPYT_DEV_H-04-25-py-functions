invoices = [
    {
        'id': 1,
        'number': '001/01/2025',
        'items': [
            {
                'nr': 1,
                'description': 'Dell laptop',
                'amount': 2,
                'unit_price': 1_500.00
            }
        ],
        'total': 3_000.00
    },
    {
        'id': 2,
        'number': '002/01/2025',
        'items': [
            {
                'nr': 1,
                'description': 'Dell laptop',
                'amount': 4,
                'unit_price': 1_500.00
            }
        ],
        'total': 6_000.00
    },
    {
        'id': 3,
        'number': '003/01/2025',
        'items': [
            {
                'nr': 1,
                'description': 'Dell monitor',
                'amount': 1,
                'unit_price': 600.00
            }
        ],
        'total': 600.00
    },
    {
        'id': 4,
        'number': '004/01/2025',
        'items': [
            {
                'nr': 1,
                'description': 'Logitech',
                'amount': 4,
                'unit_price': 250.00
            }
        ],
        'total': 1_000.00
    },
    {
        'id': 5,
        'number': '005/01/2025',
        'items': [
            {
                'nr': 1,
                'description': 'Lenovo laptop',
                'amount': 2,
                'unit_price': 1_600.00
            }
        ],
        'total': 3_200.00
    },
]


for invoice in invoices:
    print(invoice['total'])