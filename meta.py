# MAIN SCRAPER HANDLER

from smaxpy import Smax

req_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}


class Meta:
    """
    Meta class handler
    """

    @classmethod
    async def get(cls, website):
        """
        Return a bs4 soup for the class to scrape and compile.
        """

        # TODO: needs rework
        try:
            smax = Smax(website, headers=req_headers)
            code = 200
        except Exception as e:
            print(e)
            return cls(500, None)

        # status_code needs udpate from smaxpy
        return cls(code, smax._soup)

    def __init__(self, status_code, soup) -> None:
        super().__init__()
        self.status_code = status_code

        self.soup = soup.head if soup else soup

    def check_err(self):
        return self.status_code != 200

    def get_title(self):
        """
        Returns the <title> tag text.
        """
        try:
            return self.soup.title.get_text()
        except Exception:
            return ""  # return a blank if the webpage / site has no title

    def meta_default(self):
        """
        Compiles and returns the default and common <meta> tags.
        """
        meta = {"title": self.get_title()}
        # get the description
        try:
            meta["description"] = self.soup.find("meta", attrs={"name": "description"})[
                "content"
            ]
        except Exception:
            meta["description"] = ""

        # get the robots meta
        try:
            meta["robots"] = self.soup.find("meta", attrs={"name": "robots"})["content"]
        except Exception:
            pass

        # get the viewport
        try:
            meta["viewport"] = self.soup.find("meta", attrs={"name": "viewport"})[
                "content"
            ]
        except Exception:
            meta["viewport"] = ""

        # get the canonical tag
        try:
            meta["canonical"] = self.soup.find("link", attrs={"rel": "canonical"})[
                "href"
            ]
        except Exception:
            pass

        # get the charset
        try:
            meta["charset"] = self.soup.find("meta", attrs={"charset": True})[
                "chartset"
            ]
        except Exception:
            pass

        # return the basic meta tags
        return meta

    def meta_opengraph(self):
        """
        Gets and returns the <og:> meta tags.
        """
        og_properties = [
            "type",
            "title",
            "description",
            "image",
            "url",
            "site_name",
        ]  # common opengraph properties
        opengraph = {}

        for i in og_properties:
            try:
                opengraph[i] = self.soup.find("meta", attrs={"property": f"og:{i}"})[
                    "content"
                ]
            except Exception:
                # if the property doens't exist, do nothing
                pass

        # return the opengraph meta tags
        return opengraph

    # THIS WILL BE ADDED NEXT
    def meta_twitter(self):
        """
        Gets and returns the <twitter:> meta tags.
        """
        tw_properties = [
            "title",
            "description",
            "image",
            "site",
            "creator",
        ]  # common twitter meta tags
        twitter = {}

        for i in tw_properties:
            try:
                twitter[i] = self.soup.find("meta", attrs={"name": f"twitter:{i}"})[
                    "content"
                ]
            except Exception:
                # if the property doens't exist, do nothing
                pass

        # return the opengraph meta tags
        return twitter
