import requests

def main():
    # TODO query parameters
    response = requests.get('https://auto.ria.com/uk/search/?indexName=auto,order_auto,newauto_search&body.id[0]=3&categories.main.id=1&country.import.usa.not=-1&price.currency=1&abroad.not=0&custom.not=1&page=0&size=10')
    response.raise_for_status()


if __name__ == '__main__':
    main()