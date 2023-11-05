import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')


links = soup.select('.titleline > a')
subtext = soup.select('.subtext')
links2 = soup2.select('.titleline > a')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtexts = subtext + subtext2


def sort_stories_by_votes(hnlist):
  return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
  hn = []
  for idx, item in enumerate(links):
    title = item.getText()
    href = item.get('href', None)
    vote = subtext[idx].select('.score')
    if len(vote):
      points = int(vote[0].getText().replace(' points', ''))
      if points > 99:
        hn.append({'title': title, 'link': href, 'votes': points})
  return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links, mega_subtexts))






















'''print(soup) # we get the html form of it instead of a string
print(soup.body) # we get the body part of the html
print(soup.contents) # we get the entire content in list form
print(soup.find_all('div')) # we get all the divs that is in html
print(soup.find_all('a')) # we get all the (a) tags which are the links of the site
print(soup.find('a'))# we get the first a tag which is the site
print(soup.title) # we get the title tag of our soup object
print(soup.a) # we get the fist a tag only'''