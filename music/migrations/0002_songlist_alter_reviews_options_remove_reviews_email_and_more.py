# Generated by Django 5.1.4 on 2024-12-27 13:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Songlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_file', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.AlterModelOptions(
            name='reviews',
            options={},
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='email',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='name',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='song',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='text',
        ),
        migrations.AddField(
            model_name='song',
            name='audio_file',
            field=models.FileField(blank=True, upload_to='songs/', verbose_name='музыка'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='default_user', max_length=255)),
                ('text', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.review', verbose_name='Родитель')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.song', verbose_name='Песня')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]