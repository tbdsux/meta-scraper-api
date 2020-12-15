# meta-scraper-api
Just a simple Web API for scraping `<meta>` tags.

#### API Url (Hosted on `https://deta.sh`)
**https://c8ndo9.deta.dev/**

### Hosting
You can host an serve this at your own server or containers.

## Development:
- Clone the repo
```
git clone https://github.com/TheBoringDude/meta-scraper-api.git
```
- Install the required modules
```
pip3 install -r requirements.txt
```
- Run the app using `uvicorn`. You might need to install it manually (`pip3 install uvicorn`) since it is not included in the `requirements.txt`.
```
uvicorn main:app --reload
```

#### Developed by:
##### :heart: TheBoringDude