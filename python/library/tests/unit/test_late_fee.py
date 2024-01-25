# TDD workshop start:
# TODO: implement late fee feature
from src.library.domain import business
from src.library.domain.business import LibraryBusiness
import datetime as dt


class TestLateFee:
    def test_case_not_overdue_then_no_fee(self, book):
        business = LibraryBusiness()
        result = business.calculate_late_fee(book)
        assert result == 0.

    def test_case_grace_period_then_no_fee(self, book):
        book.return_due_date = dt.date.today() - dt.timedelta(days=6)
        business = LibraryBusiness()
        result = business.calculate_late_fee(book)
        assert result == 0.

    def test_case_grace_period_ended_then_charge_flat_fee(self, book):
        book.return_due_date = dt.date.today() - dt.timedelta(days=7)
        business = LibraryBusiness()
        result = business.calculate_late_fee(book)
        assert result == 1.

    def test_case_grace_period_end_plus_one_day_then_charge_flat_fee_plus_daily_cost(self, book):
        book.return_due_date = dt.date.today() - dt.timedelta(days=8)
        business = LibraryBusiness()
        result = business.calculate_late_fee(book)
        assert result == 1. + 1 * 0.25