import pytest

from src.library.domain.business import LibraryBusiness


class TestBusiness:
    @pytest.fixture
    def business(self):
        return LibraryBusiness()

    def test_rent_and_return_flow_always_clear_rental_data_on_the_end(self, business, book, account):
        business.rent(book, to=account)
        business.make_return(book)

        assert book.rented_by is None
        assert book.return_due_date is None

    def test_send_overdue_notification_case_overdue_then_return_true(self, business, book_factory):
        book = book_factory(is_overdue=True)
        result = business.send_overdue_notification(book)
        assert result

