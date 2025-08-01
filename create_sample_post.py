from blog.models import Post
from django.contrib.auth.models import User

# Crie um usuário se não existir
user, _ = User.objects.get_or_create(username='admin', defaults={'email': 'admin@example.com'})

# Crie o post publicado com o slug desejado
post, created = Post.objects.get_or_create(
    slug='second-post',
    defaults={
        'title': 'Second Post',
        'content': 'Conteúdo de exemplo para o segundo post.',
        'author': user,
        'status': 1,  # 1 = Published
    }
)

if created:
    print('Post criado com sucesso!')
else:
    print('O post já existia.') 