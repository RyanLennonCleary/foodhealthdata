from django.core.management.base import BaseCommand,CommandError
from django.contrib.auth.models import User
from catalog.models import User
class Command(BaseCommand):
    def handle(self,*args,**options):
        self.stdout.write("hello world")

