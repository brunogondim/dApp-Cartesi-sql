# Generated by Django 3.2 on 2022-02-24 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSQL', '0002_rename_imputs_inputs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_sender', models.CharField(max_length=70)),
                ('epoch_index', models.IntegerField()),
                ('input_index', models.IntegerField()),
                ('block_number', models.IntegerField()),
                ('time_stamp', models.IntegerField()),
                ('payload', models.CharField(max_length=70)),
            ],
        ),
    ]
