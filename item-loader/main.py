import requests
import logging
import logging.config


# Logging
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('item-loader')


BASE_URL = 'https://api.guildwars2.com/'
ENDPOINT_ITEMS = 'v2/items'


class HttpStatusCodeException(Exception):
    pass


def get_all_item_ids():
    try:
        url = BASE_URL+ENDPOINT_ITEMS
        response = requests.get(url)
        if response.status_code != 200:
            raise HttpStatusCodeException(f'HTTP Error {response.status_code}')
    except HttpStatusCodeException:
        logger.error(f'Error requesting data. Status Code: {response.status_code}. Message: {response.reason}. URL: {response.url}')
        raise
    except:
        logger.error(f'Unexpected error while querying data. URL {url}')
        raise

    return response.json()


def get_single_item_with_id(item_id):
    try:
        params = f'/{item_id}?lang=en'
        url = BASE_URL+ENDPOINT_ITEMS+params
        response = requests.get(url)
        if response.status_code != 200:
            raise HttpStatusCodeException(f'HTTP Error {response.status_code}')
    except HttpStatusCodeException:
        logger.error(f'Error requesting data. Status Code: {response.status_code}. Message: {response.reason}. URL: {response.url}')
        raise
    except:
        logger.error(f'Unexpected error while querying data. URL {url}')
        raise

    return response.json()


if __name__ == '__main__':
    # r = get_all_item_ids()
    r = get_single_item_with_id(30704)
    print('Done')
