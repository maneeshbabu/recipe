from django.test import TestCase

from app.calc import add


class CalcTestCase(TestCase):

    def test_add_numbers(self):
        """Test that add numbers """
        self.assertEqual(add(3, 6), 9)
