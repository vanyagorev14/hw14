from celery import shared_task
from django.core.mail import send_mail as django_send_mail
from bs4 import BeautifulSoup
from celery import shared_task
from django.core.mail import send_mail as django_send_mail
import requests
from .models import Author, Citate

@shared_task
def celery_send_mail(message, receiver):
    django_send_mail(['Promt!'], message, ['admin@example.com'], receiver)


@shared_task
def nothing_to_send(subject, message, receiver):
    django_send_mail(subject, message, ['admin@example.com'], receiver)


@shared_task
def parser_for_page():
    url = 'https://quotes.toscrape.com'
    quotes_num = 5
    page_num = 1

    while quotes_num > 0:
        req = requests.get(f'{url}/page/{str(page_num)}/')
        soup = BeautifulSoup(req.content, features='xml')
        quotes = soup.findAll('div', class_='quote')

        for el in quotes:
            text = el.find('span', class_='text').text

            if not Quote.objects.filter(text=text).exists():

                url_ends = el.find('small', class_='author').find_next_sibling('a').get('href')
                auth_url = f'{url}/{url_ends}'
                auth_r = requests.get(auth_url)
                auth_soup = BeautifulSoup(auth_r.content, features='xml')
                author_block = auth_soup.find('div', class_='author-details')

                name = author_block.find('h3', class_='author-title').text

                if not Author.objects.filter(name=name).exists():
                    birthday = author_block.find('span', class_='author-born-date').text
                    birth_loc = author_block.find('span', class_='author-born-location').text
                    description = author_block.find('div', class_='author-description').text
                    author = Author.objects.create(name=name, birthday=birthday, birth_loc=birth_loc, description=description)

                else:
                    author = Author.objects.get(name=name)

                quote = Quote.objects.create(text=text, author=author)
                quote.save()
                quotes_num -= 1

            if quotes_num != 0 and el == quotes[-1] and not soup.find('li', class_='next'):
                nothing_to_send.delay(subject='Quotes ended', message='Sorry, there are no quotes here', receiver='receiver@example.com')
                quotes_num = 0
                break
        page_num += 1