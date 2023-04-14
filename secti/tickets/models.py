from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



class CustomUser(AbstractUser):
    SETORES_CHOICES = [
        ('Secretaria Executiva', 'Secretaria Executiva'),
        ('Gabinete', 'Gabinete'),
        ('Assessoria Jurídico-Legislativa', 'Assessoria Jurídico-Legislativa'),
        ('Assessoria de Comunicação', 'Assessoria de Comunicação'),
        ('Assessoria de Gestão Estratégica', 'Assessoria de Gestão Estratégica'),
        ('Assessoria de Relações Institucionais e Atendimento à Comunidade', 'Assessoria de Relações Institucionais e Atendimento à Comunidade'),
        ('Assessoria de Captação de Recursos', 'Assessoria de Captação de Recursos'),
        ('Assessoria de Relações Sociais', 'Assessoria de Relações Sociais'),
        ('Ouvidoria', 'Ouvidoria'),
        ('Subsecretaria de Administração Geral', 'Subsecretaria de Administração Geral'),
        ('Diretoria Administrativa', 'Diretoria Administrativa'),
        ('Gerência de Pessoas', 'Gerência de Pessoas'),
        ('Gerência de Frota', 'Gerência de Frota'),
        ('Gerência de Documentos', 'Gerência de Documentos'),
        ('Gerência de Contratos', 'Gerência de Contratos'),
        ('Gerência de Materiais', 'Gerência de Materiais'),
        ('Gerência de Patrimônio', 'Gerência de Patrimônio'),
        ('Gerência de Tecnologia da Informação', 'Gerência de Tecnologia da Informação'),
        ('Diretoria de Orçamento e Finanças', 'Diretoria de Orçamento e Finanças'),
        ('Diretoria de Licitações', 'Diretoria de Licitações'),
        ('Subsecretaria de Inovação, Capacitação e Inclusão Digital', 'Subsecretaria de Inovação, Capacitação e Inclusão Digital'),
        ('Diretoria de Jogos Eletrônicos', 'Diretoria de Jogos Eletrônicos'),
        ('Diretoria de Capacitação e Inclusão Digital', 'Diretoria de Capacitação e Inclusão Digital'),
        ('Subsecretaria de Promoção à Ciência e Desenvolvimento Tecnológico', 'Subsecretaria de Promoção à Ciência e Desenvolvimento Tecnológico'),
        ('Diretoria de Difusão Científica e Cidades Inteligentes', 'Diretoria de Difusão Científica e Cidades Inteligentes'),
        ('Gerência de Curadoria Científica do Planetário de Brasília', 'Gerência de Curadoria Científica do Planetário de Brasília'),
        ('Gerência de Pesquisa e Retorno Social', 'Gerência de Pesquisa e Retorno Social'),
        ('Diretoria de Economia Circular', 'Diretoria de Economia Circular'),
        ('Gerência de Recebimento e Baixa', 'Gerência de Recebimento e Baixa'),
    ]
    setor = models.CharField(max_length=100, choices=SETORES_CHOICES)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_manager = models.BooleanField(default=False)  # Adicione este campo


class Ticket(models.Model):
    motivo = models.TextField()
    nome = models.CharField(max_length=255)
    SETORES_CHOICES = [
        ('Secretaria Executiva', 'Secretaria Executiva'),
        ('Gabinete', 'Gabinete'),
        ('Assessoria Jurídico-Legislativa', 'Assessoria Jurídico-Legislativa'),
        ('Assessoria de Comunicação', 'Assessoria de Comunicação'),
        ('Assessoria de Gestão Estratégica', 'Assessoria de Gestão Estratégica'),
        ('Assessoria de Relações Institucionais e Atendimento à Comunidade', 'Assessoria de Relações Institucionais e Atendimento à Comunidade'),
        ('Assessoria de Captação de Recursos', 'Assessoria de Captação de Recursos'),
        ('Assessoria de Relações Sociais', 'Assessoria de Relações Sociais'),
        ('Ouvidoria', 'Ouvidoria'),
        ('Subsecretaria de Administração Geral', 'Subsecretaria de Administração Geral'),
        ('Diretoria Administrativa', 'Diretoria Administrativa'),
        ('Gerência de Pessoas', 'Gerência de Pessoas'),
        ('Gerência de Frota', 'Gerência de Frota'),
        ('Gerência de Documentos', 'Gerência de Documentos'),
        ('Gerência de Contratos', 'Gerência de Contratos'),
        ('Gerência de Materiais', 'Gerência de Materiais'),
        ('Gerência de Patrimônio', 'Gerência de Patrimônio'),
        ('Gerência de Tecnologia da Informação', 'Gerência de Tecnologia da Informação'),
        ('Diretoria de Orçamento e Finanças', 'Diretoria de Orçamento e Finanças'),
        ('Diretoria de Licitações', 'Diretoria de Licitações'),
        ('Subsecretaria de Inovação, Capacitação e Inclusão Digital', 'Subsecretaria de Inovação, Capacitação e Inclusão Digital'),
        ('Diretoria de Jogos Eletrônicos', 'Diretoria de Jogos Eletrônicos'),
        ('Diretoria de Capacitação e Inclusão Digital', 'Diretoria de Capacitação e Inclusão Digital'),
        ('Subsecretaria de Promoção à Ciência e Desenvolvimento Tecnológico', 'Subsecretaria de Promoção à Ciência e Desenvolvimento Tecnológico'),
        ('Diretoria de Difusão Científica e Cidades Inteligentes', 'Diretoria de Difusão Científica e Cidades Inteligentes'),
        ('Gerência de Curadoria Científica do Planetário de Brasília', 'Gerência de Curadoria Científica do Planetário de Brasília'),
        ('Gerência de Pesquisa e Retorno Social', 'Gerência de Pesquisa e Retorno Social'),
        ('Diretoria de Economia Circular', 'Diretoria de Economia Circular'),
        ('Gerência de Recebimento e Baixa', 'Gerência de Recebimento e Baixa'),
    ]
    setor = models.CharField(max_length=100, choices=SETORES_CHOICES)
    CATEGORIAS_CHOICES = [
        ('Hardware', 'Hardware'),
        ('Software', 'Software'),
        ('Rede', 'Rede'),
        ('Outros', 'Outros'),
    ]
    categoria = models.CharField(max_length=100, choices=CATEGORIAS_CHOICES)
    prioridade = models.IntegerField(choices=[(1, 'Baixa'), (2, 'Média'), (3, 'Alta')])
    STATUS_CHOICES = [
        (1, 'Aberto'),
        (2, 'Em progresso'),
        (3, 'Resolvido'),
        (4, 'Fechado'),
    ]
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    nota = models.TextField(blank=True, null=True)
   
   
    def status_name(self):
        return dict(self.STATUS_CHOICES)[self.status]
    
    def get_priority_name(self):
        priority_dict = {
        1: 'Baixa',
        2: 'Média',
        3: 'Alta',
    }
        return priority_dict.get(self.prioridade, 'Desconhecida')


