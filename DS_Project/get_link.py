from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import string

try:
    html = urlopen("https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=PAG&type=10-Q&dateb=&owner=exclude&count=20")
except HTTPError as e:
    print("can't connect to website");

soup = BeautifulSoup(html.read())
for line in soup.find_all(id="interactiveDataBtn"):
    print(line.get('href'))
    date=line.parent.next_sibling.next_sibling.next_sibling.next_sibling.string;
    print(str(date));
