import requests
import logging
import time
import random
from bs4 import BeautifulSoup
from db_handler import SQLiteWriter
from autoria.utils import CSVWriter, StdOutWriter, get_page, get_card_detailed_page, get_car_detailed_data

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

BASE_URL = "https://auto.ria.com/uk/search/"


#def main():
#    # TODO query parameters
#    response = requests.get('https://auto.ria.com/uk/search/?indexName=auto,order_auto,newauto_search&categories.main.id=1&country.import.usa.not=-1&price.currency=1&abroad.not=0&custom.not=1&page=0&size=10')
#    response.raise_for_status()
#
#    soup = BeautifulSoup(response.text, 'html.parser')
#    search_results = soup.find('div', {'id': 'searchResults'})
#    ticket_items = search_results.find('section', {'class': 'ticket-item'})
#
#    for ticket_item in ticket_items:
#        car_details = ticket_item.find('div', {'class': 'hide'})
#        car_id = car_details['data-id']
#        car_mark_name = car_details['data-mark-name']
#
#        data_link_to_view = car_details['data-link-to-view']



#if __name__ == '__main__':
#    main()


def main() -> None:
    current_page = 0
    unique_cars = set()

    csv_headers = [
        "Car ID",
        "Manufacturer",
        "Model",
        "Year",
        "Modification",
        "Link to Page",
        "Price",
        "Total Run",
        "Engine",
        "Gearbox",
        "Color",
        "Condition",
        "Drive Type",
    ]

    # creating csv handlers
    writers = (
        CSVWriter('../../currency2/autoria/cars.csv', csv_headers),
        StdOutWriter(),
    )

    # creating db handler
    db = SQLiteWriter("cars.db")
    db.create_table()
    logging.info("CONNECTING TO DB")

    while True:
        logging.info(f"PAGE: {current_page+1}")
        time.sleep(random.randint(1, 3))

        page_html = get_page(BASE_URL, page=current_page)
        soup = BeautifulSoup(page_html, "html.parser")

        search_content = soup.find("div", {"id": "searchResults"})
        content = search_content.find_all("section", {"class": "ticket-item"})

        if not content:
            break

        for item in content:
            time.sleep(random.randint(1, 3))
            car_details = item.find("div", {"class": "hide"})
            car_id = car_details["data-id"]
            link_to_page = car_details["data-link-to-view"]
            car_manufacturer = car_details["data-mark-name"]
            car_model = car_details["data-model-name"]
            car_modification = car_details["data-modification-name"]
            car_year = car_details["data-year"]

            detailed_page_html = get_card_detailed_page(link_to_page)
            car_detailed_data = get_car_detailed_data(detailed_page_html)

            data = [
                car_id,
                car_manufacturer,
                car_model,
                car_year,
                car_modification,
                link_to_page,
                car_detailed_data.get("car_price"),
                car_detailed_data.get("car_run"),
                car_detailed_data.get("car_engine"),
                car_detailed_data.get("car_gearbox"),
                car_detailed_data.get("car_color"),
                car_detailed_data.get("car_condition"),
                car_detailed_data.get("car_drive"),
            ]

            unique_cars.add(car_id)

            # writing to CSV file
            for writer in writers:
                writer.write(data)
            logging.info("INSERTED DATA TO CSV")

            # writing to SQLite DB
            db.insert_car(data)
            logging.info("INSERTED DATA TO DB")

            current_page += 1

    logging.info("PARSING COMPLETED")
    logging.info(f"PARSED {len(unique_cars)} unique cars")


if __name__ == "__main__":
    main()
