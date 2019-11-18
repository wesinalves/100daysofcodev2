# Python Journey - Chapter 22
# Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Googling...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# TODO: Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

# TODO: Open a browser tab for each result.
links = soup.select('.r a')
num_tabs = min(5, len(links))

for i in range(num_tabs):
    webbrowser.open('http://google.com' + links[i].get('href'))
