# Generated by Django 3.2.5 on 2021-10-25 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='crated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
