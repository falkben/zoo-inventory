# Generated by Django 2.2.9 on 2020-02-22 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zoo_checks", "0034_auto_20200219_2316"),
    ]

    operations = [
        migrations.AddField(
            model_name="group",
            name="population_total",
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="groupcount",
            name="comment",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AddField(
            model_name="groupcount",
            name="count_bar",
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="groupcount",
            name="count_not_seen",
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="groupcount",
            name="count_seen",
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="groupcount",
            name="count_total",
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="groupcount",
            name="needs_attn",
            field=models.BooleanField(default=False),
        ),
    ]
