# Generated by Django 3.0 on 2019-12-10 20:47

from django.db import migrations, models
import fernet_fields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CredentialSet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField(blank=True, default='')),
                ('user', models.CharField(max_length=25, verbose_name='unpriviledged username')),
                ('userPass', fernet_fields.fields.EncryptedCharField(max_length=254, verbose_name='unpriviledged password')),
                ('privUser', models.CharField(blank=True, max_length=25, verbose_name='priviledged username')),
                ('privUserPass', fernet_fields.fields.EncryptedCharField(blank=True, max_length=254, verbose_name='priviledged password')),
            ],
        ),
    ]