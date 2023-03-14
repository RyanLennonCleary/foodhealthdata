
from django.contrib.auth.models import User
user = User.objects.create_user('test2','r.cleary13@gmail.com','password')
user.save()
