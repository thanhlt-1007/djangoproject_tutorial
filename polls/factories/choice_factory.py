from .question_factory import QuestionFactory

from factory import Faker
from factory import SubFactory

from factory.django import DjangoModelFactory


class ChoiceFactory(DjangoModelFactory):
    class Meta:
        model = "polls.Choice"

    question = SubFactory(QuestionFactory)
    choice_text = Faker("sentence")
    votes = Faker("pyint")
