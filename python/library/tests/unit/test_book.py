import pytest
import datetime as dt

from src.library.domain import models
from src.library.domain import errors
from src.library.services import notifications


class TestBook:
    @pytest.fixture
    def fake_library_policy(self):
        def factory(rental_period_length):
            class FakePolicy:
                def get_rental_period_length_days(self) -> int:
                    return rental_period_length

            return FakePolicy()

        return factory


    def test_rent_a_book_case_can_rent_then_assign_account(self, book, account):
        book.rent(to=account)
        assert book.rented_by == account

    def test_rent_a_book_case_rented_already_then_raise_error(self, book_factory, account):
        book: models.Book = book_factory(is_rented=True)

        with pytest.raises(errors.BookRentedAlready):
            book.rent(to=account)

    @pytest.mark.parametrize("rental_period_length", [14, 28])
    def test_rent_a_book_always_set_return_due_date_according_to_policy(
        self, book, account, fake_library_policy, rental_period_length
    ):
        policy = fake_library_policy(rental_period_length)
        book.set_library_policy(policy)

        book.rent(to=account)

        assert book.return_due_date == dt.date.today() + dt.timedelta(days=rental_period_length)

    def test_return_a_book_always_set_rented_by_to_none(self, book_factory):
        book: models.Book = book_factory(is_rented=True)
        book.make_return()
        assert book.rented_by is None

    def test_return_a_book_always_set_return_due_date_to_none(self, book_factory):
        book: models.Book = book_factory(is_rented=True)
        book.make_return()
        assert book.rented_by is None

    def test_send_overdue_notification_case_notification_service_not_set_then_raise_attribute_error(self, book_factory):
        book: models.Book = book_factory(is_rented=True)

        with pytest.raises(AttributeError):
            book.send_overdue_notification()

    def test_send_overdue_notification_case_notification_service_set_then_call_it(self, book_factory, mocker):
        mock = mocker.create_autospec(notifications.NotificationService)
        book: models.Book = book_factory(is_rented=True)
        book.set_notification_service(mock)

        book.send_overdue_notification()

        mock.send_email.assert_called_with(book.rented_by.email, mocker.ANY)
