# Generated by Django 4.2 on 2023-04-29 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField(max_length=200)),
                ('fullname', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
            ],
        ),
    ]