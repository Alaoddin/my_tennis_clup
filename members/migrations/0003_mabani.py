# Generated by Django 4.2.2 on 2023-06-21 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_joined_date_member_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mabani',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('prise', models.IntegerField()),
                ('post_date', models.DateField(null=True)),
                ('adress', models.CharField(max_length=255)),
                ('estate_type', models.CharField(max_length=255)),
                ('estate_size', models.IntegerField()),
                ('city', models.CharField(max_length=255)),
                ('neighborhood', models.CharField(max_length=255)),
            ],
        ),
    ]