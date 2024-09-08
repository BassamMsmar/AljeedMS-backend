# Generated by Django 4.2.6 on 2024-09-08 10:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shipments',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='shipments',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipments',
            name='expected_delivery_date',
            field=models.DateField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='shipments',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
