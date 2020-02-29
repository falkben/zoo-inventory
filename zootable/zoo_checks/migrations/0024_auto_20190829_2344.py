# Generated by Django 2.2.4 on 2019-08-30 03:44

from django.db import migrations
import django_extensions.db.fields


def migrate_data_forward(apps, schema_editor):
    Animal = apps.get_model("zoo_checks", "Animal")
    Enclosure = apps.get_model("zoo_checks", "Enclosure")
    Group = apps.get_model("zoo_checks", "Group")
    Species = apps.get_model("zoo_checks", "Species")

    for model_type in [Animal, Enclosure, Group, Species]:
        for instance in model_type.objects.all():
            print("Generating slug for %s" % instance)
            instance.save()  # Will trigger slug update


def migrate_data_backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [("zoo_checks", "0023_auto_20190704_1623")]

    operations = [
        migrations.AddField(
            model_name="animal",
            name="slug",
            field=django_extensions.db.fields.AutoSlugField(
                blank=True,
                default=None,
                editable=False,
                null=True,
                populate_from=["accession_number"],
                unique=True,
            ),
        ),
        migrations.AddField(
            model_name="enclosure",
            name="slug",
            field=django_extensions.db.fields.AutoSlugField(
                blank=True,
                default=None,
                editable=False,
                null=True,
                populate_from="name",
                unique=True,
            ),
        ),
        migrations.AddField(
            model_name="group",
            name="slug",
            field=django_extensions.db.fields.AutoSlugField(
                blank=True,
                default=None,
                editable=False,
                null=True,
                populate_from="accession_number",
                unique=True,
            ),
        ),
        migrations.AddField(
            model_name="species",
            name="slug",
            field=django_extensions.db.fields.AutoSlugField(
                blank=True,
                default=None,
                editable=False,
                null=True,
                populate_from=["common_name", "species_name"],
                unique=True,
            ),
        ),
        migrations.RunPython(migrate_data_forward, migrate_data_backward),
    ]
