import pytest

from src.library.domain.business import LibraryBusiness
from src.library.domain.models import Book, Account


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
