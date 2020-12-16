# meta-scraper-api
Just a simple Web API for scraping `<meta>` tags.

#### Sample Output:
```json
{
    "request_url":"https://github.com",
    "response":{
        "url":"https://github.com",
        "title":"GitHub: Where the world builds software · GitHub",
        "meta":{
            "default":{
                "title":"GitHub: Where the world builds software · GitHub",
                "description":"GitHub is where over 56 million developers shape the future of software, together. Contribute to the open source community, manage your Git repositories, review code like a pro, track bugs and features, power your CI/CD and DevOps workflows, and secure code before you commit it.",
                "viewport":"width=device-width",
                "canonical":"https://github.com/"
            },
            "opengraph":{
                "type":"object",
                "title":"GitHub: Where the world builds software",
                "description":"GitHub is where over 56 million developers shape the future of software, together. Contribute to the open source community, manage your Git repositories, review code like a pro, track bugs and feat...",
                "image":"https://github.githubassets.com/images/modules/open_graph/github-mark.png",
                "url":"https://github.com/",
                "site_name":"GitHub"
            },
            "twitter":{
                "title":"GitHub: Where the world builds software",
                "description":"GitHub is where over 56 million developers shape the future of software, together. Contribute to the open source community, manage your Git repositories, review code like a pro, track bugs and feat...",
                "site":"@github"
            }
        }
    },
    "datetime":"2020-12-16T06:52:01.417278"
}
```

#### API Url (Hosted on https://deta.sh)
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