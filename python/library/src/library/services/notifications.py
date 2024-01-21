from typing import Protocol


class NotificationService(Protocol):
    def send_email(self, email, message):
        raise NotImplementedError


class _NotificationServiceImpl(NotificationService):
    def send_email(self, email, message):
        # call external API
        return


def create_notification_service() -> NotificationService:
    return _NotificationServiceImpl()