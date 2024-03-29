import datetime as dt
from src.library.domain.models import Account
from src.library.domain.models import Book
from src.library.domain import errors
from src.library.domain import policies
from src.library.services import notifications


class LibraryBusiness:
    def __init__(self):
        self._policy: policies.LibraryPolicy = policies.create_library_policy()
        self._notifications: notifications.NotificationService = notifications.create_notification_service()

    def rent(self, book: Book, *, to: Account):
        if book.rented_by:
            raise errors.BookRentedAlready()

        book.rented_by = to
        book.return_due_date = dt.date.today() + dt.timedelta(days=self._policy.get_rental_period_length_days())

    def make_return(self, book: Book):
        book.rented_by = None
        book.return_due_date = None

    def send_overdue_notification(self, book: Book) -> False:
        if not book.rented_by:
            return False

        if book.return_due_date >= dt.date.today():
            return False

        self._notifications.send_email(
            book.rented_by.email,
            f'Book {book.title} you rented is overdue. Rental period ended on {book.return_due_date}',
        )
        return True

    def set_library_policy(self, policy: policies.LibraryPolicy):
        self._policy = policy

    def set_notification_service(self, service: notifications.NotificationService):
        self._notifications = service

    def calculate_late_fee(self, book: Book):
        if not book.return_due_date:
            return 0.

        grace_period_end = dt.date.today() - dt.timedelta(days=7)

        if book.return_due_date > grace_period_end:
            return 0.

        days_charged = (grace_period_end - book.return_due_date).days
        return 1. + 0.25 * days_charged

