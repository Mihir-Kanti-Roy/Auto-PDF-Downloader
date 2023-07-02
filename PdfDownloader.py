from bs4 import BeautifulSoup
import requests
from requests import get


page = requests.get(input('Enter URL: '))
filetype = '.' + input('Enter File Extension (with no dot): ')
soup = BeautifulSoup(page.text, 'html.parser')
i=1
for link in soup.find_all('a'):
    url = link.get('href')
    if filetype in url:
        print(url)
        file_name='document'+str(i)+'.pdf'
        i=i+1
        with open(file_name, 'wb') as file:
            response = requests.get(url)
            file.write(response.content)
           
    else:
             continue