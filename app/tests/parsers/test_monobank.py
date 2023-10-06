from unittest.mock import MagicMock
from currency import consts
from currency.choices import CurrencyChoices
from currency.models import Rate, Source
from currency.tasks import get_currency_monobank
import json

with open("app/tests/parsers/data/monobank_test_data.json", "r") as f:
    monobank_test_data = json.load(f)


def test_monobank_parser(mocker):
    request_get_mock = mocker.patch(
        "requests.get", return_value=MagicMock(json=lambda: monobank_test_data)
    )

    rate_count = Rate.objects.count()

    get_currency_monobank()

    new_rate_count = rate_count + 2
    assert Rate.objects.count() == new_rate_count
    assert request_get_mock.call_count == 1
    assert request_get_mock.call_args[0][0] == "https://api.monobank.ua/bank/currency"


def test_monobank_parser_prevent_duplicates(mocker):
    request_get_mock = mocker.patch(
        "requests.get", return_value=MagicMock(json=lambda: monobank_test_data)
    )
    source = Source.objects.get(dev_name=consts.MONOBANK_DEV_NAME)

    Rate.objects.create(
        buy="39.63", sell="41.00", source=source, currency=CurrencyChoices.EUR
    )
    Rate.objects.create(
        buy="36.64", sell="37.44", source=source, currency=CurrencyChoices.USD
    )
    rate_count = Rate.objects.count()
    get_currency_monobank()

    assert Rate.objects.count() == rate_count
    assert request_get_mock.call_count == 1
