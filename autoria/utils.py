import csv
import logging

import requests
from bs4 import BeautifulSoup


def get_page(url: str, page: int, page_size: int = 100) -> str:
    query_parameters = {
        "indexName": "auto,order_auto,newauto_search",
        "categories.main.id": "1",
        "brand.id[0]": "59",
        "country.import.usa.not": "-1",
        "price.currency": "1",
        "abroad.not": "0",
        "custom.not": "1",
        "page": str(page),
        "size": str(page_size),
    }

    response = requests.get(url=url, params=query_parameters)
    response.raise_for_status()
    page_html = response.text
    return page_html


def get_card_detailed_page(car_url: str) -> str:
    response = requests.get(f"https://auto.ria.com/uk{car_url}")
    response.raise_for_status()
    return response.text


def get_car_detailed_data(page_html: str) -> dict:
    result = dict()
    soup = BeautifulSoup(page_html, "html.parser")

    price_div = soup.find("div", {"class": "price_value"})

    if price_div is not None:
        result["car_price"] = price_div.text

    additional_data = soup.find("div", {"class", "box-panel description-car"})

    if additional_data is not None:
        data_fields = additional_data.find_all("dd")
        for item in data_fields:
            if item.find("span") is not None:
                if "Пробіг" in item.text:
                    result["car_run"] = item.find("span", {"class": "argument"}).text
                elif "Двигун" in item.text:
                    result["car_engine"] = item.find("span", {"class": "argument"}).text
                elif "Колір" in item.text:
                    result["car_color"] = item.find("span", {"class": "argument"}).text
                elif "Привід" in item.text:
                    result["car_drive"] = item.find("span", {"class": "argument"}).text
                elif "Коробка передач" in item.text:
                    result["car_gearbox"] = item.find("span", {"class": "argument"}).text
                elif "Технічний стан" in item.text:
                    result["car_condition"] = item.find("span", {"class": "argument"}).text

    return result


class CSVWriter:
    def __init__(self, filename, headers):
        self.filename = filename

        with open(filename, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(headers)

    def write(self, data):
        with open(self.filename, 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(data)


class StdOutWriter:
    @staticmethod
    def write(data):
        logging.info(data)
