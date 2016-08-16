from django.contrib.auth.models import User



user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')