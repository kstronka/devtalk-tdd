from typing import Protocol


def complex_rental_period_calculation() -> int:
    # let's pretend this depends on many factors and system configuration
    return 14


class LibraryPolicy(Protocol):
    def get_rental_period_length_days(self) -> int:
        raise NotImplementedError


class _LibraryPolicyImpl:
    def get_rental_period_length_days(self) -> int:
        return complex_rental_period_calculation()


def create_library_policy():
    return _LibraryPolicyImpl()
