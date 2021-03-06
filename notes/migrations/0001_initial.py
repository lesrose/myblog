# Generated by Django 3.0.4 on 2020-03-25 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_create_time', models.DateTimeField(blank=True, null=True)),
                ('n_content', models.CharField(blank=True, max_length=255, null=True)),
                ('n_is_done', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'db_table': 't_notes',
                'managed': True,
            },
        ),
    ]
