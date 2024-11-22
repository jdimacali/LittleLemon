from django.test import TestCase
from restaurant.models import Menu  # Note: The model is Menu, not MenuItem

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")  # Need to use str(item) to get string representation
