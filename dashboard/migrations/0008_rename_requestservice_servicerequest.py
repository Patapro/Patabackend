# Generated by Django 4.2.6 on 2023-10-25 04:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0007_requestservice'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RequestService',
            new_name='ServiceRequest',
        ),
    ]