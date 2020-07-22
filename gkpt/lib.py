from serpsbot.client import SerpsBot
from urllib.parse import urlparse

class Gkpt():
    def __init__(self, serpsbotApiKey, pages=10, gl='us', hl='en-US', autocorrect=0):
        self.pages = pages
        self.gl = gl
        self.hl = hl
        self.autocorrect = autocorrect
        self.sb = SerpsBot(serpsbotApiKey)

    def get_ranking(self, url, keyword, exactMatchUrl=True):
        rank = None
        resurl = None
        if not url.strip().startswith('http'):
            url = f'http://{url}'
        parsedurl = urlparse(url)
        if len(parsedurl.netloc) == 0:
            return rank
        else:
            targeturl = f'{parsedurl.netloc}/{parsedurl.path}'
        results = self.sb.getresults(q=keyword, pages=self.pages, hl=self.hl, gl=self.gl, autocorrect=self.autocorrect)
        if results.get('status') is True:
            try:
                for result in results.get('data').get('data').get('results').get('organic'):
                    parsedresult = urlparse(result.get('url'))
                    parsedresulturl = f'{parsedresult.netloc}/{parsedresult.path}'
                    if exactMatchUrl is True:
                        if targeturl.strip('/') == parsedresulturl.strip('/'):
                            rank = result.get('rank')
                            resurl = result.get('url')
                            break
                    else:
                        if parsedurl.netloc == parsedresult.netloc:
                            rank = result.get('rank')
                            resurl = result.get('url')
                            break
            except Exception as e:
                pass
        return {
            'url': resurl,
            'rank': rank,
            'gl': self.gl,
            'hl': self.hl
        }


