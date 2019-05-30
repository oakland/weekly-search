import sys
import re
import requests
from bs4 import BeautifulSoup

print('Start searching ....')

def get_articles(url, pattern, selector):
  linkReg = re.compile(pattern)
  html = requests.get(url).text
  soup = BeautifulSoup(html, 'html.parser')
  links = soup.find(id = selector).find_all('a', href = linkReg)
  articles = []

  for link in links:
    if 'href' in link.attrs:
      articles.append({
        'title': link.text,
        'url': link.attrs['href']
      })
  return articles

rootArticles = get_articles('https://github.com/ruanyf/weekly', '^(/ruanyf/weekly/blob/master/docs/issue-(\d){1,}\.md)', 'readme')

def get_target_articles(articles, keyword):
  target = []

  for article in articles:
    links = get_articles('https://github.com' + article['url'], '', 'readme')
    for link in links:
      if keyword in link['title']:
        print(article['title'] + ' - ' + link['title'] + ': ' + link['url'])
        target.append(link)

  return target

get_target_articles(rootArticles, sys.argv[1]);

print('Search ends ....')
