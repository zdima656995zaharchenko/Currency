import requests
from celery import shared_task
from django.conf import settings
from currency import consts
from decimal import Decimal, ROUND_DOWN
from currency.choices import CurrencyChoices
from currency.consts import PRIVATBANK_CODE_NAME, MONOBANK_CODE_NAME
from currency.consts import MONOBANK_DEV_NAME
from currency.utils import to_2_places_decimal
from django.core.mail import send_mail

@shared_task
def send_email_contact_us(cleaned_data: dict):
    email_body = f"""
            From: {cleaned_data['email_from']}
            Subject: {cleaned_data['subject']}
            Message: {cleaned_data['message']}
            """

    from django.conf import settings

    send_mail(
        "Contact Us",
        email_body,
        settings.DEFAULT_FROM_EMAIL,
        [settings.DEFAULT_FROM_EMAIL],
        fail_silently=False,
    )
    return True

@shared_task
def parse_privatbank():
    from currency.models import Rate, Source
    from currency.choices import CurrencyChoices

    source, _ = Source.objects.get_or_create(
        code_name=consts.PRIVATBANK_CODE_NAME, defaults={"name": "PrivatBank"}
    )

    url = "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11"
    response = requests.get(url)

    rates = response.json()

    available_currencies = {"USD": CurrencyChoices.USD, "EUR": CurrencyChoices.EUR}

    for rate in rates:
        buy = to_2_places_decimal(rate["buy"])
        sale = to_2_places_decimal(rate["sale"])
        currency = rate["ccy"]

        if currency not in available_currencies:
            continue

        currency = available_currencies[currency]

        last_rate = (
            Rate.objects.filter(source=source, currency=currency)
            .order_by("created")
            .last()
        )

        if last_rate is not None and (last_rate.buy != buy or last_rate.sell != sale):
            Rate.objects.create(buy=buy, sell=sale, source=source, currency=currency)


@shared_task
def get_currency_monobank():
    import logging
    logging.info("PARSING MONOBANK")
    from currency.models import Rate, Source

    monobank_api_url = "https://api.monobank.ua/bank/currency"

    source = Source.objects.filter(dev_name=MONOBANK_DEV_NAME).first()
    if source is None:
        source = Source.objects.create(
            dev_name=MONOBANK_DEV_NAME, name="MonoBank", url=monobank_api_url
        )
        logging.info("NEW MONOBANK SOURCE")

    response = requests.get(monobank_api_url)
    response.raise_for_status()

    rates = response.json()[0:2]

    available_currencies = {
        840: CurrencyChoices.USD,
        978: CurrencyChoices.EUR,
    }

    for rate in rates:
        currency = rate["currencyCodeA"]
        buy = to_2_places_decimal(rate["rateBuy"])
        sell = to_2_places_decimal(rate["rateSell"])

        if currency not in available_currencies.keys():
            continue

        last_rate = (
            Rate.objects.filter(source=source, currency=available_currencies[currency])
            .order_by("-created")
            .first()
        )

        if last_rate is None or last_rate.buy != buy or last_rate.sell != sell:
            Rate.objects.create(
                currency=available_currencies[currency],
                buy=buy,
                sell=sell,
                source=source,
            )
            logging.info("NEW MONOBANK RATE")


def mono_api():
    return requests.get("https://api.monobank.ua/bank/currency").json()




@shared_task
def send_signup_verify_email(subject, body, from_email, recipient):
    send_mail(
        subject,
        body,
        from_email,
        [recipient],
        fail_silently=False,
    )
    return True
