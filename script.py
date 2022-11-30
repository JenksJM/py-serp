import sys
from urllib.parse import urlparse
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
    sys.exit()
    
website = input("What is the name of your website? ").strip()
keywords = input("What keywords would you like to search for? (keyword1,keyword2) ").strip()

def findKeywordPostion(keyword, website):
    print ('Searching Google for keyword ', keyword, 'and website ', website)
    for index, url in enumerate(search(keyword, tld="co.uk", num=100, pause=2)):
        parsed_url = urlparse(url)
        if website == parsed_url.netloc:
            print("Found at postion: ", index + 1)

for keyword in keywords.split(', '):
    findKeywordPostion(keyword, website)