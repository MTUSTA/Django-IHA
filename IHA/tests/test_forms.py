from django.test import TestCase
from IhaApp.forms import UserForm, IhaCreateForm, IhaPropertyCreateForm, IhaProductUpdateForm, IhaPropertyUpdateForm
from IhaApp.models import iha_product,iha_property

class TestForms(TestCase):

    def test_user_form_valid_data(self):
        form = UserForm(data={
            "username": 'admin',
            "first_name": 'admin',
            "last_name": 'admin',
            "email": 'admin@gmail.com',
            "password1": 'AEKSD213.alsjdhas',
            "password2": 'AEKSD213.alsjdhas'
        })

        self.assertTrue(form.is_valid())

    def test_user_form_no_data(self):
        form = UserForm(data={})

        self.assertFalse(form.is_valid())
        self.assertNotEqual(len(form.errors), 0)

    def test_iha_create_form_valid_data(self):
        form = IhaCreateForm(data={
            "model_code": 'model_code',
        })
        self.assertTrue(form.is_valid())

    def test_iha_create_form_no_data(self):
        form = IhaCreateForm(data={})

        self.assertFalse(form.is_valid())
        self.assertNotEqual(len(form.errors), 0)

    def test_iha_property_form_valid_data(self):
        form = IhaCreateForm(data={
            "model_code": 'model_code',
        })
        self.assertTrue(form.is_valid())
        iha_prod = form.save()

        form = IhaPropertyCreateForm(data={
            "iha_Product": iha_prod,
            "ad": "BAYKAR",
            "marka": "BAYKAR",
            "model": "BAYKAR",
            "agirlik": "1",
            "kategori": "Savunma",

        })
        self.assertTrue(form.is_valid())

    def test_iha_property_form_no_data(self):
        form = IhaCreateForm(data={
            "model_code": 'model_code',
        })
        self.assertTrue(form.is_valid())
        iha_prod = form.save()

        form = IhaPropertyCreateForm(data={})
        self.assertFalse(form.is_valid())
        self.assertNotEqual(len(form.errors), 0)
    def test_iha_product_update_form_valid_data(self):
        form = IhaCreateForm(data={
            "model_code": 'model_code',
        })
        self.assertTrue(form.is_valid())
        iha_prod = form.save()

        form = IhaProductUpdateForm(instance=iha_prod,data={
            "model_code": 'model_code2',
        })
        self.assertTrue(form.is_valid())

