# Generated by Django 2.2.9 on 2020-01-28 03:22

import operator
from functools import reduce

from django.conf import settings
from django.db import migrations, models
from django.db.models import Q


def migrate_data_forward(apps, schema_editor):
    Role = apps.get_model("zoo_checks", "Role")
    Enclosure = apps.get_model("zoo_checks", "Enclosure")

    enclosures = Enclosure.objects.all()

    # extract "tuples" of users for each enclosure
    # create a set of unique sets of users
    shared_users_set = {
        # needs to be tuple to be put into a set (immutable)
        # sorted to create identical sequences
        tuple([u for u in enc.users.exclude(first_name="admin").order_by("id")])
        for enc in enclosures
    }

    for users_group in shared_users_set:
        if not users_group:
            continue

        query = reduce(operator.and_, (Q(users=user) for user in users_group))

        enclosure_group = [
            enc for enc in Enclosure.objects.exclude(~query).order_by("id")
        ]

        role_name = "_".join(enc.name[:10] for enc in enclosure_group)

        role = Role(name=role_name[:100])
        role.save()
        role.users.add(*users_group)
        role.enclosures.add(*enclosure_group)


def migrate_data_backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("zoo_checks", "0029_animalcount_comment"),
    ]

    operations = [
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                ("enclosures", models.ManyToManyField(to="zoo_checks.Enclosure")),
                ("users", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["name"],},
        ),
        migrations.RunPython(migrate_data_forward, migrate_data_backward),
        migrations.RemoveField(model_name="enclosure", name="users",),
    ]
