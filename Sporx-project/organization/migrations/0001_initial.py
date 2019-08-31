# Generated by Django 2.2.4 on 2019-08-31 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='organizatio',
            fields=[
                ('org_name', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='images')),
                ('room_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]