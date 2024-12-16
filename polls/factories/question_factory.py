from factory import Faker
from factory.django import DjangoModelFactory


class QuestionFactory(DjangoModelFactory):
    class Meta:
        model = "polls.Question"

    question_text = Faker("sentence")
    pub_date = Faker("date_object")
