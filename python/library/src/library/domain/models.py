import datetime as dt
from attrs import define, field


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
