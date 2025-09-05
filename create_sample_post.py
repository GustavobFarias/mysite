import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from blog.models import Post
from django.contrib.auth.models import User

user, created = User.objects.get_or_create(
    username='admin',
    defaults={'email': 'admin@example.com', 'is_staff': True, 'is_superuser': True}
)
if created:
    user.set_password('senha123')
    user.save()
    print("Superusuário criado!")
else:
    print("O superusuário já existia.")

post, created = Post.objects.get_or_create(
    slug='second-post',
    defaults={
        'title': 'Second Post',
        'content': 'Conteúdo de exemplo para o segundo post.',
        'author': user,
        'status': 1,
    }
)
if created:
    print("Post criado com sucesso!")
else:
    print("O post já existia.")
