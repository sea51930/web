# Generated by Django 2.0.7 on 2018-07-05 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gas', '0003_gasadvisory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gasadvisory',
            options={'verbose_name_plural': 'Gas Advisories'},
        ),
        migrations.AlterModelOptions(
            name='gasprofile',
            options={'verbose_name_plural': 'Gas Profiles'},
        ),
    ]