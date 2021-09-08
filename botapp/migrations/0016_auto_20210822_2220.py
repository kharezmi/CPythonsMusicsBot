# Generated by Django 3.2.6 on 2021-08-22 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botapp', '0015_alter_taskmanager_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmanager',
            name='photo',
            field=models.ImageField(default=2, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='taskmanager',
            name='txt',
            field=models.CharField(choices=[('Send Message All Users', 'Send Message'), ('Send Photo All Users', 'Send Photo')], max_length=30),
        ),
    ]