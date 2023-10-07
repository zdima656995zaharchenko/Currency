from unittest.mock import MagicMock

from currency import consts
from currency.choices import CurrencyChoices
from currency.models import Rate, Source
from currency.tasks import parse_privatbank

privatbank_test_data = [
    {"ccy": "EUR", "base_ccy": "UAH", "buy": "39.62", "sale": "39.62"},
    {"ccy": "USD", "base_ccy": "UAH", "buy": "37.45", "sale": "37.45"},
    {"ccy": "PLN", "base_ccy": "UAH", "buy": "37.45", "sale": "37.45"},
]


def test_privatbank_parser(mocker):
    request_get_mock = mocker.patch(
        "requests.get", return_value=MagicMock(json=lambda: privatbank_test_data)
    )

    rate_count = Rate.objects.count()

    parse_privatbank()

    new_rate_count = rate_count + 2
    assert Rate.objects.count() == new_rate_count
    assert request_get_mock.call_count == 1
    assert (
        request_get_mock.call_args[0][0]
        == "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11"
    )


def test_privatbank_parser_prevent_duplicates(mocker):
    request_get_mock = mocker.patch(
        "requests.get", return_value=MagicMock(json=lambda: privatbank_test_data)
    )
    source = Source.objects.get(dev_name=consts.PRIVATBANK_DEV_NAME)
    Rate.objects.create(
        buy="39.62", sell="39.62", source=source, currency=CurrencyChoices.EUR
    )
    Rate.objects.create(
        buy="37.45", sell="37.45", source=source, currency=CurrencyChoices.USD
    )

    rate_count = Rate.objects.count()

    parse_privatbank()

    assert Rate.objects.count() == rate_count
    assert request_get_mock.call_count == 1
