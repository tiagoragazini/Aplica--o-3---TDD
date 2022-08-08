from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animais.models import Animal

class IndexViewtestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.animal = Animal.objects.create(
            nome_animal = 'calopsita',
            predador = 'Não',
            venenoso = 'Não',
            domestico = 'Sim',
        )

    def test_index_view_retorna_caracteristicas_do_animal(self):
        responde = self.client.get('/', {'buscar':'calopsita'})
        caracteristica_animal_pesquisado = responde.context['caracteristicas']
        self.assertIs(type(responde.context['caracteristicas']), QuerySet)
        self.assertEqual(caracteristica_animal_pesquisado[0].nome_animal, 'calopsita')