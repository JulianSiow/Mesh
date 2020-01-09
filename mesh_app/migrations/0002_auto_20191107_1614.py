# Generated by Django 2.2.7 on 2019-11-08 00:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mesh_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendees',
            name='attendee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendees', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='attendees',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendees', to='mesh_app.Event'),
        ),
        migrations.AlterField(
            model_name='event',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL),
        ),
    ]
