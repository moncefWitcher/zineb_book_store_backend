# Generated by Django 3.2.5 on 2023-03-23 05:24

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_the_content_as_sidepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='file',
            field=models.FileField(blank=True, upload_to=app.models.upload_file),
        ),
    ]