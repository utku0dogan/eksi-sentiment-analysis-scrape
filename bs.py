from bs4 import BeautifulSoup
import requests

URL = input()
page = requests.get(URL)
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.277"
r = requests.get(URL, headers={'User-Agent': USER_AGENT})
soup = BeautifulSoup(r.content, 'html.parser')


def page_counts(url):
    """
        Get page counts of the titles
    """
    r = requests.get(url, headers={'User-Agent':USER_AGENT})
    soup = BeautifulSoup(r.content, 'html.parser')
    try:
        last_page = soup.find('div', {'class':'pager'})['data-pagecount']
    except TypeError:
        last_page = 1
    return int(last_page)


entries = []

soup2 = BeautifulSoup(r.text, 'html.parser')

entry = soup2.find('div', {'class':'content'}) # find entry content
entry_date = soup2.find('a', {'class':'entry-date permalink'}) # find date of the entry
entry_author = soup2.find('a', {'class':'entry-author'}) # find author of the entry


while entry is not None: # iterate until entry object not None 
    data = {
        'Entry': entry.get_text(separator=" ").replace('\n','').replace('\r', '').replace('\t', '').replace('    ', '').replace('bkz: ', '').replace('---  spoiler  ---', ''),# clear the contents of the entry from unnecessary things
        'Date': entry_date.text,
    }
    entries.append(data)
    entry = entry.find_next('div', {'class':'content'}) # find next entry content
    entry_date = entry_date.find_next('a', {'class':'entry-date permalink'}) # find next date of the entry


print(entries[0]["Entry"])


page_count = page_counts(URL)
for i in range(page_count):
    pass
