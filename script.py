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

googleResults = search(keyword, num_results=10, lang="en")
for index, result in enumerate(googleResults):
    parsed_url = urlparse(result)
    if website == parsed_url.netloc:
        print("Found at postion: ", index + 1)
        sys.exit()