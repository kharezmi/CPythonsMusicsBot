# Generated by Django 3.2.6 on 2021-08-10 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botapp', '0004_alter_users_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='uu_id',
            field=models.TextField(default=0, max_length=15),
        ),
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]