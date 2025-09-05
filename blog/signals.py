from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import User
from .create_sample_post import create_sample_post

@receiver(post_migrate)
def create_superuser_and_post(sender, **kwargs):
    # Cria superusuário se não existir
    user, created = User.objects.get_or_create(
        username='admin',
        defaults={'email': 'admin@example.com', 'is_staff': True, 'is_superuser': True}
    )
    if created:
        user.set_password('senha123')
        user.save()
        print("Superusuário criado automaticamente!")

    # Cria post usando sua função
    create_sample_post(user)
