# Generated by Django 3.1.3 on 2021-05-28 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idestado', models.IntegerField()),
                ('estado', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='hero',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
