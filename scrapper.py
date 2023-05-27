from email_validation import validate_email
from bs4 import BeautifulSoup
import requests


def getData(url):
    payload = requests.get(url)
    data = payload.text
    data = BeautifulSoup(data, 'html.parser')
    address = validate_email(data)
    if len(address) == 0:
        print("No Email Address Found...!")
    else:
        print(address)


if __name__ == '__main__':
    url = input("Enter URL for Scrapping >>> ")
    print(f"--- URL ---> {url}")
    print("Executing Scrapper.......")
    getData(url)
