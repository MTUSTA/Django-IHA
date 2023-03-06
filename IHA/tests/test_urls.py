from django.test import SimpleTestCase
from django.urls import reverse, resolve

from IhaApp.views import loginPage, registerPage, logoutPage, dashboard, create_iha, update_iha, delete_iha, \
    error_page_404


class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, loginPage)

    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, registerPage)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logoutPage)

    def test_dashboard_url_is_resolved(self):
        url = reverse('dashboard')
        self.assertEquals(resolve(url).func, dashboard)

    def test_create_iha_url_is_resolved(self):
        url = reverse('create_iha')
        self.assertEquals(resolve(url).func, create_iha)

    def test_update_iha_url_is_resolved(self):
        url = reverse('update_iha', args=[3])
        self.assertEquals(resolve(url).func, update_iha)

    def test_delete_iha_url_is_resolved(self):
        url = reverse('delete_iha', args=[3])
        self.assertEquals(resolve(url).func, delete_iha)

    def test_404_url_is_resolved(self):
        url = reverse('404')
        self.assertEquals(resolve(url).func, error_page_404)
