from django.test import TestCase
from django.urls import reverse
from .models import Ticket
from django.contrib.auth import get_user_model, login


class TicketCreationTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
        username='John Doe',
        email='john@example.com',
        password='testpassword123',
        )
        self.client.login(username='John Doe', password='testpassword123')


    def test_create_ticket(self):
        response = self.client.post(reverse('tickets:create_ticket'), {
            'motivo': 'Problema com o computador',
            'nome': 'John Doe',
            'setor': 'TI',
            'categoria': "Hardware",
            'prioridade': 1,
            'email': self.user.email,
        }, follow=True)

        print("Conteúdo da resposta:", response.content)
        self.assertEqual(response.status_code, 200)  # Verifica se a resposta é um redirecionamento
        self.assertEqual(Ticket.objects.count(), 1)  # Verifica se um ticket foi criado
        ticket = Ticket.objects.first()
        self.assertEqual(ticket.motivo, 'Problema com o computador')
        self.assertEqual(ticket.nome, 'John Doe')
        self.assertEqual(ticket.categoria, "Hardware")
        self.assertEqual(ticket.prioridade, 1)
        self.assertEqual(ticket.email, 'johndoe@example.com')
