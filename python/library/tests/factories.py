import factory

from src.library.domain import models
from pytest_factoryboy import register


@register
class BookFactory(factory.Factory):
    class Meta:
        model = models.Book

    title = factory.Faker('word', part_of_speech='noun')
    author = factory.Faker('name_nonbinary')

    class Params:
        is_rented = factory.Trait(
            rented_by=factory.SubFactory('tests.factories.AccountFactory'),
            return_due_date=factory.Faker('future_date', end_date='+14d')
        )
        is_overdue = factory.Trait(
            rented_by=factory.SubFactory('tests.factories.AccountFactory'),
            return_due_date=factory.Faker('past_date')
        )


@register
class AccountFactory(factory.Factory):
    class Meta:
        model = models.Account

    name = factory.Faker('name_nonbinary')
    email = factory.Faker('email')
