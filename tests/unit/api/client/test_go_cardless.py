import pytest

from interview.api.client import go_cardless


FIXTURE = {
  "id": "M28A9",
  "iban": "GB2756386333762976",
  "discount": {
    "minimum_transaction_count": 49,
    "fees_discount": 7
  },
  "transactions": [
    {
      "amount": 54869,
      "fee": 290
    },
    {
      "amount": 50033,
      "fee": 297
    },
    {
      "amount": 17955,
      "fee": 97
    },
    {
      "amount": 51090,
      "fee": 354
    },
    {
      "amount": 33927,
      "fee": 339
    },
    {
      "amount": 54130,
      "fee": 505
    },
    {
      "amount": 62043,
      "fee": 326
    },
    {
      "amount": 36850,
      "fee": 230
    },
    {
      "amount": 358,
      "fee": 2
    },
    {
      "amount": 62882,
      "fee": 317
    },
    {
      "amount": 41075,
      "fee": 206
    },
    {
      "amount": 24336,
      "fee": 211
    },
    {
      "amount": 14168,
      "fee": 93
    },
    {
      "amount": 69822,
      "fee": 671
    },
    {
      "amount": 1276,
      "fee": 7
    },
    {
      "amount": 37182,
      "fee": 312
    },
    {
      "amount": 36214,
      "fee": 190
    },
    {
      "amount": 24350,
      "fee": 123
    },
    {
      "amount": 10060,
      "fee": 78
    },
    {
      "amount": 22604,
      "fee": 132
    },
    {
      "amount": 52478,
      "fee": 286
    },
    {
      "amount": 28791,
      "fee": 232
    },
    {
      "amount": 54706,
      "fee": 405
    },
    {
      "amount": 26662,
      "fee": 153
    },
    {
      "amount": 66725,
      "fee": 340
    },
    {
      "amount": 10339,
      "fee": 77
    },
    {
      "amount": 20459,
      "fee": 116
    },
    {
      "amount": 64777,
      "fee": 337
    }
  ]
}


def test_get_magic_number():
    expected_result = 1023435
    discount = FIXTURE['discount']

    result = go_cardless.calculate_total_payable_amount(FIXTURE['transactions'],
                                                        discount['minimum_transaction_count'],
                                                        discount['fees_discount'])

    assert result == expected_result


def test_get_magic_number_no_fee_discount():
    expected_result = 104315
    discount = FIXTURE['discount']

    result = go_cardless.calculate_total_payable_amount(FIXTURE['transactions'][:2],
                                                        discount['minimum_transaction_count'],
                                                        discount['fees_discount'])

    assert result == expected_result


def test_get_magic_number_empty():
    expected_result = 0
    discount = FIXTURE['discount']

    result = go_cardless.calculate_total_payable_amount([],
                                                        discount['minimum_transaction_count'],
                                                        discount['fees_discount'])

    assert result == expected_result
