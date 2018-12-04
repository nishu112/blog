# Generated by Django 2.0.2 on 2018-12-04 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailid', models.EmailField(max_length=30)),
                ('fname', models.CharField(max_length=15)),
                ('Quotes', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Blog',
                'db_table': 'Blog_Entry',
            },
        ),
    ]
