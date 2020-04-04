import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.farfetch.com/mx/shopping/men/off-white-cinturon-industrial-con-logo-item-13526124.aspx'

HEADERS = {
    'User-Agent': 'your user agent'}


def checkPrice():
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(class_='_947f4f _b4c5cd _f01e99').get_text()
    desc = soup.find(class_='_b4693b _b4693b _a32b92').get_text()
    price = soup.find(class_='_def925 _b4693b').get_text()
    convertedPrice = float(price[1:].replace(',', ''))

    if (convertedPrice <= 4000):
        sendEmail()
    else:
        print("The product is still not cheap enough")


def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('yourEmail@gmail.com', 'yourPassword')

    subject = ('The Product is CHEAPER Now (Farfetch Scraper)')
    body = (f'Link: {URL}')
    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail('yourEmail@gmail.com',
                    'yourEmail@gmail.com', msg)
    print('Email has been sent!')

    server.quit()


while(True):
    checkPrice()
    time.sleep(60*60)
