from django.test import TestCase
from .models import Actor, Movie


class ActorModelTests(TestCase):
    def test_creation(self):
        actor = Actor(name="Deep")
        self.assertIs(actor.name == 'Deep', True)
        self.assertIs(actor.name == 'dj', False)


class MovieModelTests(TestCase):
    def test_creation(self):
        actor = Movie(title="sakat", year=2020)
        self.assertIs(actor.title == "sakat", True)
        self.assertIs(actor.year == 2020, True)
