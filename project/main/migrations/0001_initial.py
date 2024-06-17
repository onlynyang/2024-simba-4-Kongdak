# Generated by Django 5.0.6 on 2024-06-17 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField()),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('weather', models.CharField(choices=[('sunny', '맑음'), ('bad', '나쁨')], default='sunny', max_length=5)),
            ],
        ),
    ]