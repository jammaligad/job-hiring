# Generated by Django 2.1.5 on 2019-03-03 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_platform', '0010_auto_20190303_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='author',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='recruiter', to=settings.AUTH_USER_MODEL),
        ),
    ]
