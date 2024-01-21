import factory
from factory import post_generation

from src.library.domain import business
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
            rented_by=factory.SubFactory('tests.unit.factories.AccountFactory'),
            return_due_date=factory.Faker('future_date', end_date='+14d')
        )

    @post_generation
    def set_up_policy(self, create, extracted, **kwargs):
        self.set_library_policy(business.create_library_policy())


@register
class AccountFactory(factory.Factory):
    class Meta:
        model = models.Account

    name = factory.Faker('name_nonbinary')
    email = factory.Faker('email')
