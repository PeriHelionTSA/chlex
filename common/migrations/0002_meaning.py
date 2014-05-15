# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'common', b'0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name=b'Meaning',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'meaning', models.CharField(max_length=5000)),
                (b'lem', models.ForeignKey(to=b'common.Lem', to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
