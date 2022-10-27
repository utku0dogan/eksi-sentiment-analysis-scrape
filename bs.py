from bs4 import BeautifulSoup
import requests
import re
import datetime
import csv
start = datetime.datetime.now()


URL = input()

entries = []

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




page_count = page_counts(URL)

rootURL = URL[:-1]


for i in range(int(page_count) + 1):   ##pagecount
    
    URL_ = rootURL + str(i)
    r = requests.get(URL_, headers={'User-Agent': USER_AGENT})
    soup2 = BeautifulSoup(r.text, 'html.parser')
    entry = soup2.find('div', {'class':'content'}) # find entry content
    entry_date = soup2.find('a', {'class':'entry-date permalink'}) # find date of the entry
    while entry is not None: # iterate until entry object not None 
        data = {
            'Entry': entry.get_text(separator=" ").replace('\n','').replace('\r', '').replace('\t', '').replace('    ', '').replace('bkz: ', '').replace('---  spoiler  ---', ''),# clear the contents of the entry from unnecessary things
            'Date': entry_date.text[:10],
        }
        entries.append(data)
        entry = entry.find_next('div', {'class':'content'}) # find next entry content
        entry_date = entry_date.find_next('a', {'class':'entry-date permalink'}) # find next date of the entry



print(entries[0]["Entry"])
print(len(entries))
# https://eksisozluk.com/recep-tayyip-erdogan--95281?p=1, https://eksisozluk.com/26-ekim-2022-ozgur-ozel-tweeti--7448728?a=popular, https://eksisozluk.com/recep-tayyip-erdogan--95281


for i in range(len(entries)):
    print('\n --------------------------------------------- \n' + entries[i]["Entry"] + ' - '+ entries[i]["Date"] )
    

## 
end = datetime.datetime.now()

print("start time: ", start)
print("end- time: ", end)

print(end-start)

## ?a=popular -> delete last 9 
## ?p=1 -> non delete
## if it is not  both of above, then add '?p='  


with open('entries.csv', 'w', newline='') as writeFile:
    writer = csv.writer(writeFile, delimiter='\n',quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(entries)

keys = entries[0].keys()
with open('a.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(entries)
