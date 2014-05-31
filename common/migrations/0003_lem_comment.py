# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'common', b'0002_meaning'),
    ]

    operations = [
        migrations.AddField(
            model_name=b'lem',
            name=b'comment',
            field=models.CharField(max_length=5000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
