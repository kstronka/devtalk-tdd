import datetime as dt
import pytest
from src.library.domain.business import LibraryBusiness
from src.library.domain import errors
from src.library.services import notifications


class TestLibraryBusiness:
    @pytest.fixture
    def fake_library_policy(self):
        def factory(rental_period_length=14):
            class FakePolicy:
                def get_rental_period_length_days(self) -> int:
                    return rental_period_length

            return FakePolicy()

        return factory

    @pytest.fixture
    def business(self, fake_library_policy, mocker):
        business = LibraryBusiness()

        business.set_library_policy(fake_library_policy())
        business.set_notification_service(mocker.create_autospec(notifications.NotificationService))

        return business

    def test_rent_case_book_not_rented_then_mark_it_rented_by(self, business, book, account):
        business.rent(book, to=account)
        assert book.rented_by == account

    def test_rent_case_rented_already_then_raise_error(self, business, book_factory, account):
        book = book_factory(is_rented=True)

        with pytest.raises(errors.BookRentedAlready):
            business.rent(book, to=account)

    @pytest.mark.parametrize('period', [14, 28])
    def test_rent_case_can_rent_then_set_return_due_date(self, business, book, account, fake_library_policy, period):
        business.set_library_policy(fake_library_policy(period))
        business.rent(book, to=account)
        assert book.return_due_date == dt.date.today() + dt.timedelta(days=period)

    def test_make_return_always_clear_book_rented_at(self, business, book_factory):
        book = book_factory(is_rented=True)
        business.make_return(book)
        assert book.rented_by is None

    def test_make_return_always_clear_return_due_date(self, business, book_factory):
        book = book_factory(is_rented=True)
        business.make_return(book)
        assert book.return_due_date is None

    def test_send_overdue_notification_case_book_is_overdue_then_send_email(self, business, book_factory, mocker):
        mock = mocker.create_autospec(notifications.NotificationService)
        business.set_notification_service(mock)
        book = book_factory(is_rented=True, return_due_date=dt.date.today() - dt.timedelta(days=1))

        business.send_overdue_notification(book)

        mock.send_email.assert_called_with(book.rented_by.email, mocker.ANY)

    def test_send_overdue_notification_case_book_not_rented_then_do_nothing(self, business, book, mocker):
        mock = mocker.create_autospec(notifications.NotificationService)
        business.set_notification_service(mock)

        business.send_overdue_notification(book)

        mock.send_email.assert_not_called()

    def test_send_overdue_notification_case_is_not_due_yet_then_do_nothing(self, business, book_factory, mocker):
        mock = mocker.create_autospec(notifications.NotificationService)
        business.set_notification_service(mock)
        book = book_factory(is_rented=True)

        business.send_overdue_notification(book)

        mock.send_email.assert_not_called()

    def test_send_overdue_notification_case_sent_then_return_true(self, business, book_factory):
        book = book_factory(is_rented=True, return_due_date=dt.date.today() - dt.timedelta(days=1))
        result = business.send_overdue_notification(book)
        assert result

    def test_send_overdue_notification_case_not_sent_then_return_false(self, business, book_factory):
        book = book_factory(is_rented=True, return_due_date=dt.date.today())
        result = business.send_overdue_notification(book)
        assert not result
