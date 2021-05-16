from meta import Meta
from datetime import datetime
from urllib.parse import urlparse


async def main_handler(website):
    # check if website is valid
    if not check_site(website=website):
        return {"request_url": website, "response": "Invalid website url!"}

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


def check_site(website):
    # a website url should atleast starts with these schemes
    if website.startswith("https://") or website.startswith("http://"):
        url = urlparse(website)

        # check if there is a dot in the netloc, based from: https://stackoverflow.com/questions/25259134/how-can-i-check-whether-a-url-is-valid-using-urlparse
        if len(url.netloc.split(".")) > 1:
            return True  # this means that there is a dot in the url, haha

    return False
