# Generated by Django 4.1.3 on 2022-11-17 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie_app", "0003_movie_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="image",
            field=models.ImageField(default="images/default.jpg", upload_to="images"),
        ),
    ]