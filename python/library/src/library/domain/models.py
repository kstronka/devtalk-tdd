import datetime as dt
from attrs import define, field
from src.library.domain import business
from src.library.domain import errors
from src.library.services import notifications


@define
class Account:
    name: str
    email: str


@define
class Book:
    title: str
    author: str

    rented_by: Account | None = field(default=None)
    return_due_date: dt.date | None = field(default=None)

    _policy: business.LibraryPolicy | None = field(default=None)
    _notifications: notifications.NotificationService | None = field(default=None)

    def rent(self, *, to: Account):
        if self.rented_by:
            raise errors.BookRentedAlready()

        if not self._policy:
            raise AttributeError("Missing library policy")

        self.rented_by = to
        self.return_due_date = dt.date.today() + dt.timedelta(days=self._policy.get_rental_period_length_days())

    def make_return(self):
        self.rented_by = None

    def send_overdue_notification(self):
        if not self._notifications:
            raise AttributeError("No notifications service set")

        if not self.rented_by:
            return

        self._notifications.send_email(self.rented_by.email, f'Book "{self.title}" you rented is overdue')

    def set_library_policy(self, policy: business.LibraryPolicy | None):
        self._policy = policy

    def set_notification_service(self, service: notifications.NotificationService | None):
        self._notifications = service
