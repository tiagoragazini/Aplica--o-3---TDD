from urllib import request
from django.test import TestCase, RequestFactory
from django.urls import reverse
from animais.views import index

class AnimaisURLSTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_rota_usl_utiliza_view_index(self):
        """Teste se a home da aplicação utiliza a função indesx da view"""
        request = self.factory.get('/')
        with self.assertTemplateUsed('index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)