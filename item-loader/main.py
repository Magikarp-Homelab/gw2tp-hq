import requests
import logging
import logging.config


# Logging
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('item-loader')


BASE_URL = 'https://api.guildwars2.com/'
ENDPOINT_ITEMS = 'v2/item'


class HttpStatusCodeException(Exception):
    pass


def get_all_item_ids():
    try:
        response = requests.get(BASE_URL+ENDPOINT_ITEMS)
        if response.status_code != 200:
            raise HttpStatusCodeException(f'HTTP Error {response.status_code}')
    except HttpStatusCodeException:
        logger.error(f'Error requesting data. Status Code: {response.status_code}. Message: {response.reason}. URL: {response.url}')
        raise
    except:
        logger.error(f'Unexpected error while querying data. URL {BASE_URL+ENDPOINT_ITEMS}')
        raise

    return response


if __name__ == '__main__':
    r = get_all_item_ids()
    print('Done')
