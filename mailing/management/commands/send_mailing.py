from mailing.models import Mailing, MailingAttempt
from config.settings import DEFAULT_FROM_EMAIL
from django.utils.timezone import now
from django.core.management.base import BaseCommand
from django.db.models import Q
from django.core.mail import send_mail


class Command(BaseCommand):
    """Функция для отправки рассылок"""

    def handle(self, *args, **kwargs):
        mailings = Mailing.objects.filter(
            (Q(status=Mailing.CREATED) | Q(status=Mailing.RUNNING)) &
            Q(first_send_at__lte=now()) &
            Q(finish_send_at__gte=now())
        )

        for mailing in mailings:
            mailing.status = Mailing.RUNNING
            mailing.save()

            recipients = mailing.recipients.all()
            for recipient in recipients:
                try:
                    send_mail(
                        subject=mailing.message,
                        message=mailing.message.message,
                        from_email=DEFAULT_FROM_EMAIL,
                        recipient_list=[recipient.email])
                    status = MailingAttempt.SUCCESS
                    response = f"{recipient}: Успешно отправлено"
                    self.stdout.write(self.style.SUCCESS(response))

                except Exception as e:
                    status = MailingAttempt.FAILURE
                    response = f"{recipient}: Ошибка при отправке: {e}"
                    self.stdout.write(self.style.ERROR(response))

                MailingAttempt.objects.create(
                    attempted_at=now(),
                    status=status,
                    mail_server_response=response,
                    mailing=mailing)
