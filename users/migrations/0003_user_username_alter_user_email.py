# Generated by Django 5.0.4 on 2024-04-24 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_remove_user_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="username",
            field=models.CharField(
                default="ro", max_length=150, verbose_name="Никнейм"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                blank=True,
                max_length=254,
                unique=True,
                verbose_name="Электронная почта",
            ),
        ),
    ]
