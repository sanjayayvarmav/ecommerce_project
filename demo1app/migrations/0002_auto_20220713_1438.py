# Generated by Django 3.2.14 on 2022-07-13 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo1app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('det', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='place',
            name='desc',
            field=models.TextField(),
        ),
    ]