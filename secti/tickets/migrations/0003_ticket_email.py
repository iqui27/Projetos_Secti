# Generated by Django 4.2 on 2023-04-12 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_alter_ticket_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]