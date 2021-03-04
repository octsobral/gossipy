from src.support.config import Config
from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup
import requests

DAILY = '&as_qdr=d'
WEEKLY = '&as_qdr=w'
MONTHLY = '&as_qdr=m'

URL = 'https://news.google.com/rss/search?q='
URL_2 = 'http://www.google.com/search?q='
RESULT_NUMBER = '&num='

HEADERS = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
}


class SearchService:

    def __init__(self):
        self.config = Config()

    def search(self, query):

        session = requests.Session()

        search_url = self._create_search_url(query)

        request = session.get(search_url, headers=HEADERS)

        result = self._clean_results(request)

        return result

    def _create_search_url(self, query, **kwargs):

        frequency_option = ['daily, weekly, monthly']

        frequency = self.config.FREQUENCY

        if frequency.lower() not in frequency_option:
            frequency_option = DAILY
        else:
            if frequency.lower() is 'daily':
                frequency_option = DAILY
            elif frequency.lower() is 'weekly':
                frequency_option = WEEKLY
            elif frequency.lower() is 'monthly':
                frequency_option = MONTHLY

        result = self.config.RESULT
        if self.config.RESULT is None:
            result = 10

        query = '+'.join(query.split())

        search_url = URL + query + frequency_option + RESULT_NUMBER + str(result)

        return search_url


    def _clean_results(self, request):

        soup = BeautifulSoup(request.text, "html.parser")

        result = []

        search_result = soup.findAll('item')
        for content in search_result:
            link = str(search_result[content].contents[2])
            title = str(search_result[content].contents[7])
            publication_raw = str(search_result[content].contents[4])
            publication_date = publication_raw[9:-10]
            organized_content = {'link': link, 'title': title, 'publication_date': publication_date }
            result.append(organized_content)

        return result

    def _web_scraping(self, cleaned_urls):

        result = []

        for results in cleaned_urls:
            page = requests.get(results, headers=HEADERS).text
            soup = BeautifulSoup(page)
            done = {'nome': soup.title.string, 'url': result}
            result.append(done)

        return result

    def _clean_results_google_search(self, request):

        soup = BeautifulSoup(request.text, "html.parser")
        output = []

        soup.findAll('link')
        anchors = soup.find(id='search').findAll('a')

        for anchor in anchors:

            try:
                url = anchor['href']
                text = anchor.text.strip()
                result = {'text': text, 'url': url}
            except KeyError:
                continue

            try:
                if url.startswith('/url?'):
                    ostricized = urlparse(url, 'http')
                    url = parse_qs(ostricized.query)['q'][0]

                ostricized = urlparse(url, 'http')
                if ostricized.netloc and 'google' not in ostricized.netloc:
                    output.append(url)
                else:
                    pass
            except Exception:
                pass

            if len(result) >= 1:
                output.append(url)

        result = list(dict.fromkeys(output))

        return result

