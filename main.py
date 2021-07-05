from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

from handler import main_handler

app = FastAPI()

# setup cors middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["index"])
def index():
    return "Website META Scraper API"


@app.get("/meta", tags=["meta"])
async def meta(site: Optional[str] = None):
    if site:
        return await main_handler(website=site)

    # if there are no values parsed to `site`
    return "You need to parse a `site` to the endpoint."
