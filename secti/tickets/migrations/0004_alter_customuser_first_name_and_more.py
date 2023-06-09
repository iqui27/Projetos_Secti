# Generated by Django 4.2 on 2023-04-12 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_ticket_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='setor',
            field=models.CharField(choices=[('Secretaria Executiva', 'Secretaria Executiva'), ('Gabinete', 'Gabinete'), ('Assessoria Jurídico-Legislativa', 'Assessoria Jurídico-Legislativa'), ('Assessoria de Comunicação', 'Assessoria de Comunicação'), ('Assessoria de Gestão Estratégica', 'Assessoria de Gestão Estratégica'), ('Assessoria de Relações Institucionais e Atendimento à Comunidade', 'Assessoria de Relações Institucionais e Atendimento à Comunidade'), ('Assessoria de Captação de Recursos', 'Assessoria de Captação de Recursos'), ('Assessoria de Relações Sociais', 'Assessoria de Relações Sociais'), ('Ouvidoria', 'Ouvidoria'), ('Subsecretaria de Administração Geral', 'Subsecretaria de Administração Geral'), ('Diretoria Administrativa', 'Diretoria Administrativa'), ('Gerência de Pessoas', 'Gerência de Pessoas'), ('Gerência de Frota', 'Gerência de Frota'), ('Gerência de Documentos', 'Gerência de Documentos'), ('Gerência de Contratos', 'Gerência de Contratos'), ('Gerência de Materiais', 'Gerência de Materiais'), ('Gerência de Patrimônio', 'Gerência de Patrimônio'), ('Gerência de Tecnologia da Informação', 'Gerência de Tecnologia da Informação'), ('Diretoria de Orçamento e Finanças', 'Diretoria de Orçamento e Finanças'), ('Diretoria de Licitações', 'Diretoria de Licitações'), ('Subsecretaria de Inovação, Capacitação e Inclusão Digital', 'Subsecretaria de Inovação, Capacitação e Inclusão Digital'), ('Diretoria de Jogos Eletrônicos', 'Diretoria de Jogos Eletrônicos'), ('Diretoria de Capacitação e Inclusão Digital', 'Diretoria de Capacitação e Inclusão Digital'), ('Subsecretaria de Promoção à Ciência e Desenvolvimento Tecnológico', 'Subsecretaria de Promoção à Ciência e Desenvolvimento Tecnológico'), ('Diretoria de Difusão Científica e Cidades Inteligentes', 'Diretoria de Difusão Científica e Cidades Inteligentes'), ('Gerência de Curadoria Científica do Planetário de Brasília', 'Gerência de Curadoria Científica do Planetário de Brasília'), ('Gerência de Pesquisa e Retorno Social', 'Gerência de Pesquisa e Retorno Social'), ('Diretoria de Economia Circular', 'Diretoria de Economia Circular'), ('Gerência de Recebimento e Baixa', 'Gerência de Recebimento e Baixa')], max_length=100),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='setor',
            field=models.CharField(choices=[('Secretaria Executiva', 'Secretaria Executiva'), ('Gabinete', 'Gabinete'), ('Assessoria Jurídico-Legislativa', 'Assessoria Jurídico-Legislativa'), ('Assessoria de Comunicação', 'Assessoria de Comunicação'), ('Assessoria de Gestão Estratégica', 'Assessoria de Gestão Estratégica'), ('Assessoria de Relações Institucionais e Atendimento à Comunidade', 'Assessoria de Relações Institucionais e Atendimento à Comunidade'), ('Assessoria de Captação de Recursos', 'Assessoria de Captação de Recursos'), ('Assessoria de Relações Sociais', 'Assessoria de Relações Sociais'), ('Ouvidoria', 'Ouvidoria'), ('Subsecretaria de Administração Geral', 'Subsecretaria de Administração Geral'), ('Diretoria Administrativa', 'Diretoria Administrativa'), ('Gerência de Pessoas', 'Gerência de Pessoas'), ('Gerência de Frota', 'Gerência de Frota'), ('Gerência de Documentos', 'Gerência de Documentos'), ('Gerência de Contratos', 'Gerência de Contratos'), ('Gerência de Materiais', 'Gerência de Materiais'), ('Gerência de Patrimônio', 'Gerência de Patrimônio'), ('Gerência de Tecnologia da Informação', 'Gerência de Tecnologia da Informação'), ('Diretoria de Orçamento e Finanças', 'Diretoria de Orçamento e Finanças'), ('Diretoria de Licitações', 'Diretoria de Licitações'), ('Subsecretaria de Inovação, Capacitação e Inclusão Digital', 'Subsecretaria de Inovação, Capacitação e Inclusão Digital'), ('Diretoria de Jogos Eletrônicos', 'Diretoria de Jogos Eletrônicos'), ('Diretoria de Capacitação e Inclusão Digital', 'Diretoria de Capacitação e Inclusão Digital'), ('Subsecretaria de Promoção à Ciência e Desenvolvimento Tecnológico', 'Subsecretaria de Promoção à Ciência e Desenvolvimento Tecnológico'), ('Diretoria de Difusão Científica e Cidades Inteligentes', 'Diretoria de Difusão Científica e Cidades Inteligentes'), ('Gerência de Curadoria Científica do Planetário de Brasília', 'Gerência de Curadoria Científica do Planetário de Brasília'), ('Gerência de Pesquisa e Retorno Social', 'Gerência de Pesquisa e Retorno Social'), ('Diretoria de Economia Circular', 'Diretoria de Economia Circular'), ('Gerência de Recebimento e Baixa', 'Gerência de Recebimento e Baixa')], max_length=100),
        ),
    ]
