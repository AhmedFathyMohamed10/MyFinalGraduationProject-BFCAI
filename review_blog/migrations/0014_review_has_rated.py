# Generated by Django 4.1.2 on 2023-05-21 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("review_blog", "0013_review_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="has_rated",
            field=models.BooleanField(default=False),
        ),
    ]
