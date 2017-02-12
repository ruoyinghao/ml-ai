from urllib.request import urlopen
import urllib
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import string
import re
import os

fr = open('test.txt', 'r');
ticker=fr.readline();
#get rid of \n
ticker=ticker[0:len(ticker)-1];

print(ticker+" download started");
while ticker!="":
    try:
        urladdress="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK="+ticker+"&type=10-Q&dateb=&owner=exclude&count=20"
        ticker_link = urlopen(urladdress);
    except HTTPError as e:
        print("Ticker level: can't connect to website");

    epl_list=[];
    file_date=[];
    soup = BeautifulSoup(ticker_link.read())
    
    for line in soup.find_all(id="interactiveDataBtn"):
        excel_page_link=line.get('href');
        epl_list.append(str(excel_page_link));
        date=line.parent.next_sibling.next_sibling.next_sibling.next_sibling.string;
        file_date.append(date);
    for i in range(0,len(epl_list)):
        try:
            excel_page=urlopen("https://www.sec.gov"+epl_list[i]);
        except HTTPError as e:
            print("10Q level: can't connect to website");

        #get the link to excel file
        subsoup=BeautifulSoup(excel_page.read())
        for link in subsoup.find_all(href=re.compile("Financial_Report.xlsx")):
            file_link= link.get('href');
            
            urllib.request.urlretrieve("https://www.sec.gov"+file_link,ticker+"_"+file_date[i]+"_"+"10Q"+".xlsx")
            print(file_link+" download complete");
    print(ticker+" download complete");
    ticker=fr.readline();

fr.close();
        
        
