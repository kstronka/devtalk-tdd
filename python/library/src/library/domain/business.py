from abc import ABC
from typing import Protocol


class LibraryPolicy(Protocol):
    def get_rental_period_length_days(self) -> int:
        raise NotImplementedError


class _LibraryPolicyImpl:
    def get_rental_period_length_days(self) -> int:
        # complex logic here
        return 14


def create_library_policy():
    return _LibraryPolicyImpl()
