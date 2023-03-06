from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from IhaApp.models import iha_product


class TestViews(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='admin', password='admin', email="admin@admin.com")
        self.client = Client()
        self.loginPage = 'index'
        self.registerPage = 'register'
        self.logoutPage = 'logout'
        self.dashboard = 'dashboard'
        self.create_iha = 'create_iha'
        self.update_iha = 'update_iha'
        self.delete_iha = 'delete_iha'
        self.error_page_404 = '404'

    def test_views_index_without_login_GET(self):
        response = self.client.get(reverse(self.loginPage))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages-link.html')
        self.assertTemplateUsed(response, 'pages-js.html')
        self.assertTemplateUsed(response, 'pages-login.html')

    def test_views_index_with_login_GET(self):
        logged_in = self.client.force_login(self.user)
        response = self.client.get(reverse(self.loginPage), follow=True)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages-link.html')
        self.assertTemplateUsed(response, 'pages-js.html')
        self.assertTemplateUsed(response, 'pages-dashboard.html')

    def test_views_register_GET(self):
        response = self.client.get(reverse(self.registerPage))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages-link.html')
        self.assertTemplateUsed(response, 'pages-js.html')
        self.assertTemplateUsed(response, 'pages-register.html')

    def test_views_logout_with_login_GET(self):
        logged_in = self.client.force_login(self.user)
        response = self.client.get(reverse(self.logoutPage), follow=True)

        self.assertEquals(response.status_code, 200)

        self.assertTemplateUsed(response, 'pages-login.html')

    def test_views_logout_without_login_GET(self):
        logged_in = self.client.force_login(self.user)
        response = self.client.get(reverse(self.logoutPage), follow=True)

        self.assertEquals(response.status_code, 200)

        self.assertTemplateUsed(response, 'pages-login.html')

    def test_views_dashboard_with_login_GET(self):
        logged_in = self.client.force_login(self.user)
        response = self.client.get(reverse(self.dashboard), follow=True)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages-link.html')
        self.assertTemplateUsed(response, 'pages-js.html')
        self.assertTemplateUsed(response, 'pages-dashboard.html')

    def test_views_dashboard_without_login_GET(self):
        response = self.client.get(reverse(self.dashboard), follow=True)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages-link.html')
        self.assertTemplateUsed(response, 'pages-js.html')
        self.assertTemplateUsed(response, 'pages-login.html')

    def test_views_create_with_login_no_create_iha_GET(self):
        logged_in = self.client.force_login(self.user)
        response = self.client.get(reverse(self.create_iha))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages-link.html')
        self.assertTemplateUsed(response, 'pages-js.html')
        self.assertTemplateUsed(response, 'pages-iha-create.html')

    def test_views_create_with_login_create_iha_POST(self):
        logged_in = self.client.force_login(self.user)

        data = {
            'model_code': 'test_model_code', 'ad': 'test_model_ad', 'marka': 'BAYKAR',
            'model': 'BAYKAR MODEL', 'agirlik': '1', 'kategori': 'Keşif ve İstihbarat'

        }
        response = self.client.post(reverse(self.create_iha), data, format='json', follow=True)
        o = iha_product.objects.filter(model_code='test_model_code')

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages-link.html')
        self.assertTemplateUsed(response, 'pages-js.html')
        self.assertTemplateUsed(response, 'pages-dashboard.html')
        self.assertEqual(len(o), 1)

    def test_views_create_without_login_iha_GET(self):
        response = self.client.get(reverse(self.create_iha), follow=True)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages-link.html')
        self.assertTemplateUsed(response, 'pages-js.html')
        self.assertTemplateUsed(response, 'pages-login.html')

    def test_views_update_with_login_with_iha_iha_POST(self):
        logged_in = self.client.force_login(self.user)
        data = {
            'model_code': 'test_model_code', 'ad': 'test_model_ad', 'marka': 'BAYKAR',
            'model': 'BAYKAR MODEL', 'agirlik': '1', 'kategori': 'Savunma'

        }
        response = self.client.post(reverse(self.create_iha), data, format='json', follow=True)

        o = iha_product.objects.filter(model_code='test_model_code')
        self.assertEqual(len(o), 1)

        data2 = {
            'model_code': 'test_model_code2', 'ad': 'test_model_ad2', 'marka': 'BAYKAR2',
            'model': 'BAYKAR MODEL2', 'agirlik': '2', 'kategori': 'Savunma'

        }
        target_id = o.first().id
        response = self.client.post(reverse(self.update_iha, args=[target_id]), data2, format='json', follow=True)

        o2 = iha_product.objects.get(pk=target_id)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages-link.html')
        self.assertTemplateUsed(response, 'pages-js.html')
        self.assertTemplateUsed(response, 'pages-dashboard.html')
        self.assertEqual(o2.model_code, 'test_model_code2')

    def test_views_update_with_login_no_iha_iha_GET(self):
        logged_in = self.client.force_login(self.user)

        response = self.client.get(reverse(self.update_iha, args=[1]), follow=True)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages-link.html')
        self.assertTemplateUsed(response, 'pages-js.html')
        self.assertTemplateUsed(response, 'pages-error-404.html')

    def test_views_update_without_login_iha_GET(self):
        response = self.client.get(reverse(self.update_iha, args=[1]), follow=True)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages-link.html')
        self.assertTemplateUsed(response, 'pages-js.html')
        self.assertTemplateUsed(response, 'pages-login.html')

    def test_views_delete_with_login_iha_POST(self):
        logged_in = self.client.force_login(self.user)
        data = {
            'model_code': 'test_model_code', 'ad': 'test_model_ad', 'marka': 'BAYKAR',
            'model': 'BAYKAR MODEL', 'agirlik': '1', 'kategori': 'Savunma'

        }
        response = self.client.post(reverse(self.create_iha), data, format='json', follow=True)

        o = iha_product.objects.get(model_code='test_model_code')

        response = self.client.post(reverse(self.delete_iha, args=[o.id]), follow=True)
        o = iha_product.objects.filter(model_code='test_model_code')

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages-link.html')
        self.assertTemplateUsed(response, 'pages-js.html')
        self.assertTemplateUsed(response, 'pages-dashboard.html')
        self.assertEqual(len(o), 0)

    def test_views_delete_with_login_no_iha_GET(self):
        logged_in = self.client.force_login(self.user)

        response = self.client.post(reverse(self.delete_iha, args=[1]), follow=True)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages-link.html')
        self.assertTemplateUsed(response, 'pages-js.html')
        self.assertTemplateUsed(response, 'pages-error-404.html')

    def test_views_delete_without_login_iha_GET(self):
        response = self.client.get(reverse(self.delete_iha, args=[1]), follow=True)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages-link.html')
        self.assertTemplateUsed(response, 'pages-js.html')
        self.assertTemplateUsed(response, 'pages-login.html')

    def test_views_404_iha_GET(self):
        response = self.client.get(reverse(self.error_page_404))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages-link.html')
        self.assertTemplateUsed(response, 'pages-js.html')
        self.assertTemplateUsed(response, 'pages-error-404.html')
