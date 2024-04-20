# Generated by Django 3.2 on 2024-04-19 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentApp', '0002_auto_20240415_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(default='https://www.freepik.com/premium-vector/african-american-man-face_2585211.htm#fromView=search&page=1&position=40&uuid=76e184f4-fc4d-4e05-81c9-737edda42205', upload_to='', verbose_name='Photo de profil'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
