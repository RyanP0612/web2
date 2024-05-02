# Generated by Django 5.0.3 on 2024-04-25 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatBot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='chatbot')),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('scheduledDate', models.DateTimeField()),
            ],
        ),
    ]