# Generated by Django 4.0.3 on 2022-09-20 00:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('intelin', '0006_refute_modify_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='argument',
            name='voter',
            field=models.ManyToManyField(related_name='voter_question', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='refute',
            name='voter',
            field=models.ManyToManyField(related_name='voter_refute', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='argument',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_argument', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='refute',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_refute', to=settings.AUTH_USER_MODEL),
        ),
    ]
