from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker
from polls.models import Post, Comment

fake = Faker()
UserModel = get_user_model()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, choices=range(10, 500), help='Number of random User')

    def handle(self, *args, **options):
        count = options['count']

        for i in range(count):
            User.objects.create(username=fake.name(), password=make_password('password'))

        posts = []
        for l in User.objects.all():
            for i in range(5):
                posts.append(Post(title=fake.sentence(nb_word=2), brief_desc=fake.sentence(nb_words=5),
                                  full_desc=fake.text(), author=l))
        Post.objects.bulk_create(posts)

        comments = []
        for el in Post.objects.all():
            for i in range(7):
                posts.append(Comment(username=fake.name(), text=fake.sentence(nb_words=4), posts=el))
        Comment.objects.bulk_create(comments)

        self.stdout.write(self.style.SUCCES('Succes fill db'))