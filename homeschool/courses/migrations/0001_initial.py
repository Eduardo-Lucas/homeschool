# Generated by Django 3.0.2 on 2020-01-28 04:41

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("schools", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Course",
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
                (
                    "days_of_week",
                    models.PositiveIntegerField(
                        default=31, help_text="The days of the week when this runs"
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                (
                    "grade_level",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="courses",
                        to="schools.GradeLevel",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="CourseTask",
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
                ("uuid", models.UUIDField(db_index=True, default=uuid.uuid4)),
                ("description", models.TextField()),
                (
                    "duration",
                    models.PositiveIntegerField(
                        help_text="The expected length of the task in minutes"
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="course_tasks",
                        to="courses.Course",
                    ),
                ),
            ],
        ),
    ]
