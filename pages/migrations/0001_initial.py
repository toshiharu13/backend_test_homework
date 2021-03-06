# Generated by Django 2.2 on 2020-11-13 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arm',
            fields=[
                ('name_arm', models.CharField(max_length=30)),
                ('id_arm', models.AutoField(primary_key=True, serialize=False)),
                ('ip_arm', models.GenericIPAddressField(null=True)),
                ('dt_version_arm', models.CharField(blank=True, max_length=30)),
                ('os_version_arm', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]
