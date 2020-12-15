from meta import Meta
from datetime import datetime


async def main_handler(website):
    scraper = await Meta.get(website=website)

    # if there was a status_code err,
    if scraper.check_err():
        return {
            "request_url": website,
            "status_code": scraper.status_code,
            "response": "There was a problem with the request.",
            "datetime": datetime.utcnow(),
        }

    # continue if there was no problem
    # return the scraped response
    return {
        "request_url": website,
        "response": {
            "url": website,
            "title": scraper.get_title(),
            "meta": {
                "default": scraper.meta_default(),
                "opengraph": scraper.meta_opengraph(),
                "twitter": scraper.meta_twitter(),
            },
        },
        "datetime": datetime.utcnow(),
    }