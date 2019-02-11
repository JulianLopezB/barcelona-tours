"""
Tours Barcelona Museums

Copyright (C) 2019  Jose Fernando Nuñez, José Miguel Flores, Julián López, Sergi Mas

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import requests as _req
import wikipedia as _wk
from re import findall as _findall


_guardian_key = ""
_nyt_key = ""
_guardian_url = "http://content.guardianapis.com/search"
_nyt_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"


class MediaAggregatorMixin:
    """
    This is the base class for all current and future media aggregators.
    """
    def __init__(self):
        pass

    def get_news(self, query):
        pass

    def get_limit(self):
        pass


class GuardianAggregator:
    def __init__(self):
        self._params = {"q": "", "api-key": _guardian_key}
        self._limit = None

    def get_news(self, query):
        self._params["q"] = str(query)
        response = _req.get(_guardian_url, params = self._params)
        # self._limit = response.headers["X-RateLimit-Remaining-day"]
        return [x["webUrl"] for x in response.json()["response"]["results"] if x["type"] == "article" and
                x["sectionName"] != u"Media" and "quiz" not in x["webUrl"].lower()]

    def get_limit(self):
        if not self._limit:
            self.get_news("test")
        return self._limit


class NYTAggregator:
    def __init__(self):
        self._params = {"q": "", "api-key": _nyt_key}

    def get_news(self, query):
        self._params["q"] = str(query)
        response = _req.get(_nyt_url, params = self._params)
        return [x["web_url"] for x in response.json()["response"]["docs"] if x["type_of_material"] == "News"]

    def get_limit(self):
        return self._limit


def shorten_news(url, n = 5):
    from bs4 import BeautifulSoup as bs
    from summarizer import FrequencySummarizer as fs
    response = _req.get(url)
    if not response.ok:
        return False
    page = response.content
    soup = bs(page, "lxml")
    summary = fs().summarize("\n".join([x.text for x in soup.findAll("p") if len(x.text.split()) > 1]), n)
    summary.insert(0, soup.title.text)
    return ' '.join(summary)


def get_gkg(query):
    try:
        s = _wk.summary(query, sentences = 5)
        for x in _findall("\(.*\)", s):
            s = s.replace(x, "")
        return s
    except _wk.DisambiguationError as e:
        return False