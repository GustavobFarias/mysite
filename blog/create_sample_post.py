from django.contrib.auth.models import User
from .models import Post

def create_sample_post(user=None):
    # Se user não for passado, pega o admin
    if user is None:
        user = User.objects.filter(username='admin').first()

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
        print("Post público criado automaticamente!")
    else:
        print("O post já existia.")