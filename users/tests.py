from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class RegisterUserTestCase(TestCase):
    def setUp(self):
        self.data ={
            'username': 'user',
            'email': 'user@mail.ru',
            'first_name': 'Talgat',
            'last_name': 'Asakeev',
            'password1': '123231Atdnt',
            'password2': '123231Atdnt',
        }

    def test_form_registration_get(self):
        path = reverse('users:register')
        response = self.client.get(path)
        print(response)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_user_registrations_success(self):
        user_model = get_user_model()
        path = reverse('users:register')
        response = self.client.post(path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(user_model.objects.filter(username=self.data['username']).exists())

    def test_user_registration_password_error(self):
        self.data['password2'] = '123'
        path = reverse('users:register')
        response = self.client.post(path, self.data)
        print(response)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'The two password fields didn’t match.')

    def test_user_registration_exists_error(self):
        user_model = get_user_model()
        user_model.objects.create(username=self.data['username'])
        path = reverse('users:register')
        response = self.client.post(path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'A user with that username already exists.')