from http import HTTPStatus

import pytest
from django.test import TestCase


class AlphaWordsFormTestCase(TestCase):

    def test_get_form(self):
        response = self.client.get("/words/alpha/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_post_form(self):
        response = self.client.post("/words/alpha/", data={"text": "on top of the world!"})
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_post_form_return_alpha_words_total(self):
        response = self.client.post("/words/alpha/", data={"text": "on top of the world!"})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Total of alpha words: 5")
