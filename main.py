from fastapi import FastAPI
from typing import Optional

from handler import main_handler

app = FastAPI()


@app.get("/", tags=["index"])
def index():
    return "Website META Scraper API"


@app.get("/meta", tags=["meta"])
async def meta(site: Optional[str] = None):
    if site:
        return await main_handler(website=site)

    # if there are no values parsed to `site`
    return "You need to parse a `site` to the endpoint."