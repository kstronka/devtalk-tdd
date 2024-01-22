import datetime as dt
import pytest

from src.library.domain.business import LibraryBusiness
from src.library.domain.models import Book, Account
from src.library.services import notifications


class TestLibrary:
    def test_business_methods(self):
        business = LibraryBusiness()
        book = Book('Do androids dream of electric sheep?', 'Philip K. Dick', None, None)
        account = Account('jsmith@example.com', 'John Smith')
        business.rent(book, to=account)

        assert book.rented_by == account
        assert book.return_due_date

        business.make_return(book)
        assert book.rented_by is None

        business.rent(book, to=account)
        other = Account('randy@example.com', 'Randy Marsh')

        with pytest.raises(Exception):
            business.rent(to=other)

    def test_overdue(self, book, account, mocker):
        business = LibraryBusiness()
        mocker.patch('src.library.domain.policies.complex_rental_period_calculation', return_value=10)
        business.rent(book, to=account)
        assert book.return_due_date == dt.date.today() + dt.timedelta(days=10)

    def test_notification(self, book, account, mocker):
        business = LibraryBusiness()
        business.rent(book, to=account)
        book.return_due_date = dt.date.fromisoformat('1900-01-01')
        spy = mocker.spy(notifications, name='external_api_call')
        business.send_overdue_notification(book)
        spy.assert_called_once()
