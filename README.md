# Google Search Keyword Position Checker
This is a Python package that makes use of [SerpsBot API](https://serpsbot.com) and gets the keyword position for a URL in Google Search Results.

### Installation
Install from [PyPi](https://pypi.org/project/gkpt/):
```bash
pip install gkpt
```

Or clone this repo and run setup:

```bash
git clone https://github.com/serpsbotapi/gkpt && \
cd gkpt && \
python setup.py install
```

### Usage
You need a SerpsBot API key. Get your API key at SerpsBot [here](https://serpsbot.com).

```python
from gkpt.lib import Gkpt
tracker = Gkpt('your-serpsbot-api-key')
result = tracker.get_ranking('https://gvanrossum.github.io/', 'Guido van Rossum')
```

Response will look like:
```json
{
    'url': 'https://gvanrossum.github.io/',
    'rank': 2
}
```

By default, the exact match URL is checked in SERPs. If you want to match just the domain name (excluding path), you can pass a third parameter as `False` to `get_ranking()` function:

```python
from gkpt.lib import Gkpt
tracker = Gkpt('your-serpsbot-api-key')
result = tracker.get_ranking('en.wikipedia.org', 'Guido van Rossum', exactMatchUrl=False)
```
Response will look like:
```json
{
    "url": "https://en.wikipedia.org/wiki/Guido_van_Rossum",
    "rank": 1
}
```

### Targetting by Country
To get ranking for your URL and the keyword in a specific country, set the `gl` attribute with two-letter country code on the instance before `get_ranking()` function call:

```python
# Get results for Canada
tracker.gl = 'ca'
result = tracker.get_ranking('en.wikipedia.org', 'Guido van Rossum', exactMatchUrl=False)
```

### Targetting by Language
To get ranking for your URL and the keyword in for a specific language, set the `hl` attribute with the language code on the instance before `get_ranking()` function call:

```python
# Get results for Chinese
tracker.hl = 'cn-CN'
result = tracker.get_ranking('gvanrossum.github.io', 'Guido van Rossum', exactMatchUrl=False)
```

### Bugs & Issues
Please use the issues section to report any bugs. Before opening a new issue, please considering looking through the existing issues to find any possible solution.

### Contact Us
For queries, contact us at **sales[at]serpsbot.com**.