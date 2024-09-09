# Test doubles is a better generic name than Mocks. There are 5 types of test doubles:
# - dummy (does nothing, only needed for required parameters)
# - stub (returns hard coded data)
# - spy (stub + recording of info on how they were called)
# - fake (has some behavior, but not suitable for production, i.e. uses shortcuts)
# - mock (fake + expectations of the calls they are expected to receive)
#
# see <https://www.martinfowler.com/bliki/TestDouble.html> for more details

from datetime import date
from mocking.basics import Dice, Person


def test_hardcoded_randint(mocker):
    mocker.patch("random.randint", return_value=1)
    dice = Dice()
    assert dice.roll() == 1


def test_person_age(mocker):
    fake_date = mocker.patch("mocking.basics.date")
    fake_date.today.return_value = date(2010, 1, 1)

    person = Person(date_of_birth=date(2000, 1, 1))
    assert person.age() == 10
