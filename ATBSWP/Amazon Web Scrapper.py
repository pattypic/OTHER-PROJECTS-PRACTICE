from bs4 import BeautifulSoup
import csv
import pandas as pd
import requests
import time 
import datetime
import smtplib

# Connect to Website

URL = 'https://www.amazon.com/Panasonic-20-3MP-Mirrorless-Thirds-Streaming/dp/B0942SJF1X/?_encoding=UTF8&pd_rd_w=V3Ayh&content-id=amzn1.sym.b01d0a49-a06d-4f08-9f57-5f20b110a83c&pf_rd_p=b01d0a49-a06d-4f08-9f57-5f20b110a83c&pf_rd_r=YYS9P3XNGHJV6FBFVBSM&pd_rd_wg=SxJKC&pd_rd_r=f8227c8e-a9fa-46a4-a983-eb99a7717283&ref_=pd_gw_trq_dl'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
page = requests.get(URL, headers = headers)
Soup1 = BeautifulSoup(page.content, "html.parser")
Soup2 = BeautifulSoup(Soup1.prettify(), "html.parser")
# Finds the ID title (works)
title = Soup2.find(id='productTitle').get_text()
# Finds the ID price (doesnt work)
#price = Soup2.find(id="priceblock_ourprice").get_text()
# price = price.strip()[1:]
title = title.strip()
today = datetime.date.today()
# The lines of code are what trasnfer the data to the datasheet. 
header = ['Title', 'Price', 'Date']
data = [title ,{} ,today ] #should be data = [title, price, today]
with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

# Now we are appending data to CSV
with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)

def check_price():
    URL = 'https://www.amazon.com/Panasonic-20-3MP-Mirrorless-Thirds-Streaming/dp/B0942SJF1X/?_encoding=UTF8&pd_rd_w=V3Ayh&content-id=amzn1.sym.b01d0a49-a06d-4f08-9f57-5f20b110a83c&pf_rd_p=b01d0a49-a06d-4f08-9f57-5f20b110a83c&pf_rd_r=YYS9P3XNGHJV6FBFVBSM&pd_rd_wg=SxJKC&pd_rd_r=f8227c8e-a9fa-46a4-a983-eb99a7717283&ref_=pd_gw_trq_dl'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers = headers)

    Soup1 = BeautifulSoup(page.content, "html.parser")

    Soup2 = BeautifulSoup(Soup1.prettify(), "html.parser")
    # Finds the ID title (works)
    title = Soup2.find(id='productTitle').get_text()

    # Finds the ID price (doesnt work)
    # price = Soup2.find(id="priceblock_ourprice").get_text()

    #price = price.strip()[1:]
    title = title.strip()

    import datetime

    today = datetime.date.today()
    
    import csv 

    header = ['Title', 'Price', 'Date']
    data = [title, {}, today]

    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
df = pd.read_csv(r'/Users/patrickpichardo/Desktop/ATBSWP/AmazonWebScraperDataset.csv')

print(df)

# Runs check_price after a set time and inputs data into your CSV

# while(True):
    # check_price()
    # time.sleep(1)


