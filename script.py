import sys
from urllib.parse import urlparse
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
    sys.exit()
    
website = input("What is the name of your website? ").strip()
keyword = input("What keyword would you like to search for? ").strip()
print ('Searching Google for keyword ', keyword, 'and website ', website)

for index, url in enumerate(search(keyword, tld="co.uk", num=10, stop=10, pause=2)):
    parsed_url = urlparse(url)
    if website == parsed_url.netloc:
        print("Found at postion: ", index + 1)
        sys.exit()