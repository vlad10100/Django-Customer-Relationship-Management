from django.test import TestCase
from django.shortcuts import reverse


class HomePageTest(TestCase):

    def test_status_code(self):
        # TODO some sort of test
        response = self.client.get(reverse('leads:home'))
        self.assertEqual(response.status_code, 200)



    # def test_template_name(self):
        # pass