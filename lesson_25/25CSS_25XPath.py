# google_parser_demo.py

import requests
from lxml import html
from bs4 import BeautifulSoup


def fetch_html(url: str) -> bytes:
    headers = {
        "User-Agent": "Chrome/5.0 (QA Parser Demo)", #Google без User-Agent може заблокувати, бо подумає,що це  бот 
        "Accept-Language": "uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7",  #пріоритет виведення  мови сторінки
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status() #це перевірка HTTP-статусу відповіді, тобто якщо сайт повернув 404 або 500 — буде помилка.
    return response.content #Повертається HTML у байтах.



# Функція генерує перші 25 універсальних локаторів для сторінки:
# CSS selector та XPath для кожного елемента
def extract_25_universal_locators(html_content: bytes):
    tree = html.fromstring(html_content)

    elements = tree.xpath("//*")[:25]#//* → знайти всі елементи сторінки, [:25] → беремо перші 25


    for i, el in enumerate(elements, start=1):#Проходимо по елементах, i → порядковий номер елемента, el → сам елемент
        tag = el.tag #tag → тег елемента (div, span, a, p тощо)

        xpath = f"(//{tag})[{i}]" #(//{tag})[{i}] → універсальний XPath для i-го елемента з цим тегом
        css = f"{tag}:nth-of-type({i})" #CSS-селектор для i-го елемента з цим тегом

        print(f"{i}. CSS: {css}")
        print(f"   XPath: {xpath}\n")


def main():
    url = "https://vidi.ua/ua/"

    html_content = fetch_html(url)

    extract_25_universal_locators(html_content)


if __name__ == "__main__":
    main()


