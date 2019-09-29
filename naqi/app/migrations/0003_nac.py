# Generated by Django 2.1.7 on 2019-09-29 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190928_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nac',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hostid', models.BigIntegerField()),
                ('ip', models.CharField(max_length=255)),
                ('mac', models.CharField(max_length=255)),
                ('dhcp_server', models.CharField(max_length=255)),
                ('dhcp_hostname', models.CharField(max_length=255)),
                ('nbtdomain', models.CharField(max_length=255)),
                ('ad_displayname', models.CharField(max_length=255)),
                ('ad_name', models.CharField(max_length=255)),
                ('ad_mail', models.CharField(max_length=255)),
                ('ad_title', models.CharField(max_length=255)),
                ('ad_department', models.CharField(max_length=255)),
                ('ad_mobile', models.CharField(max_length=255)),
                ('href', models.CharField(max_length=255)),
                ('etag', models.CharField(max_length=255)),
                ('update_time', models.CharField(max_length=255)),
            ],
        ),
    ]
