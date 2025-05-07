from django.apps import AppConfig
from django.db.models.signals import post_migrate



class ModelTestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'DjangoProject.model_test'

    def ready(self):
        post_migrate.connect(initialize_app, sender=self)


def initialize_app(sender, **kwargs):
    from DjangoProject.model_test.models import Author, Book

    author, _ = Author.objects.get_or_create(name='name1')
    Book.objects.get_or_create(title='title1', author=author)
