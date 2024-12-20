# Generated by Django 5.1.4 on 2024-12-17 12:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Mailing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_send_at",
                    models.DateTimeField(
                        default=datetime.datetime(2024, 12, 17, 15, 51, 11, 292704),
                        verbose_name="Дата и время первой отправки",
                    ),
                ),
                (
                    "finish_send_at",
                    models.DateTimeField(
                        default=datetime.datetime(2024, 12, 18, 15, 51, 11, 292704),
                        verbose_name="Дата и время окончания отправки",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("completed", "Завершена"),
                            ("created", "Создана"),
                            ("running", "Запущена"),
                        ],
                        max_length=9,
                        verbose_name="Статус рассылки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
                "ordering": ["id"],
                "permissions": [("can_cancel_mailing", "Can cancel mailing")],
            },
        ),
        migrations.CreateModel(
            name="MailingAttempt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "attempted_at",
                    models.DateTimeField(verbose_name="Дата и время попытки отправки"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("success", "Успешно"), ("failure", "Не успешно")],
                        max_length=7,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "mail_server_response",
                    models.TextField(
                        blank=True, null=True, verbose_name="Ответ сервера"
                    ),
                ),
            ],
            options={
                "verbose_name": "Попытка рассылки",
                "verbose_name_plural": "Попытки рассылки",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="Тема письма")),
                ("message", models.TextField(verbose_name="Тело письма")),
            ],
            options={
                "verbose_name": "Сообщение",
                "verbose_name_plural": "Сообщения",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Recipient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="Адрес почты должен быть уникальным",
                        max_length=254,
                        unique=True,
                        verbose_name="Почта",
                    ),
                ),
                ("full_name", models.CharField(max_length=200, verbose_name="ФИО")),
                (
                    "comment",
                    models.TextField(blank=True, null=True, verbose_name="Комментарий"),
                ),
            ],
            options={
                "verbose_name": "Получатель рассылки",
                "verbose_name_plural": "Получатели рассылки",
                "ordering": ["id"],
            },
        ),
    ]
