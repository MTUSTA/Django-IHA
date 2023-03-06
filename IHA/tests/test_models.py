from django.test import TestCase

from IhaApp.models import *


class TestModels(TestCase):

    def setUp(self):
        self.iha_product1 = iha_product.objects.create(
            model_code="test_model_code"
        )

        self.iha_property1 = iha_property.objects.create(
            iha_Product=self.iha_product1,
            ad='test_model_ad',
            marka='BAYKAR',
            model='BAYKAR MODEL',
            agirlik='1',
            kategori='HAVA1'
        )

    def test_object_created(self):

        self.assertEqual(self.iha_product1.model_code,'test_model_code')
        self.assertEqual(self.iha_property1.ad, 'test_model_ad')

