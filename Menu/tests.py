from django.test import TestCase
from .models import Menu


class MenuTestCase(TestCase):
    def test_menu_create(self):
        Menu.objects.create(dishname="Karahi", price=500, description="Spicy")
        self.assertEqual(Menu.objects.count(), 1)