# Generated by Django 3.2.3 on 2021-10-01 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artpiece',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('exhibited', 'Exhibited')], default='created', max_length=10),
        ),
    ]
