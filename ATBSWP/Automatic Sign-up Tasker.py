from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup



s = HTMLSession()
url = 'https://www.taskrabbit.com/become-a-tasker'

def getdata(url):
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def firstpgsignup(soup):
    state_container = soup.find('div', {'class': ' css-qc6sy-singleValue'})
    cat_container = soup.find('div', {'class': ' css-qc6sy-singleValue'})
    data = state_container == 'Austin', cat_container == 'Personal Assistant'
    response = requests.post(url, data=data)
    return response
        
soup = getdata(url)
print(firstpgsignup(soup))
