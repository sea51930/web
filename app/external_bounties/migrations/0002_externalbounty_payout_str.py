# Generated by Django 2.0.3 on 2018-03-21 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('external_bounties', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='externalbounty',
            name='payout_str',
            field=models.CharField(default='', help_text='string representation of the payout (only needed it amount/denomination cannot be filled out', max_length=255),
            preserve_default=False,
        ),
    ]
