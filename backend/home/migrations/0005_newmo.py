# Generated by Django 2.2.28 on 2023-06-02 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20230531_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewMo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aaa', models.BigIntegerField()),
            ],
        ),
    ]