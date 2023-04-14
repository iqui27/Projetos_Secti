from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, TicketForm, UserProfileForm
from .models import CustomUser, Ticket
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Avg, F, Count, ExpressionWrapper, fields
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.http import JsonResponse
from datetime import timedelta

def user_signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('tickets:user_dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'tickets/user_signup.html', {'form': form})

def closed_tickets(request):
    if request.user.is_authenticated and request.user.is_manager:
        closed_tickets = Ticket.objects.filter(status=4)
        return render(request, 'tickets/closed_tickets.html', {'tickets': closed_tickets})
    else:
        return redirect('tickets:user_login')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if request.user.is_manager:
                return redirect('tickets:manager_dashboard')
            else:
                return redirect('tickets:user_dashboard')
        else:
            messages.error(request, 'Usuário ou senha incorretos')
    else:
        form = AuthenticationForm()

    return render(request, 'tickets/user_login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('tickets:user_login')

def user_dashboard(request):
    if request.user.is_authenticated:
        tickets = Ticket.objects.filter(nome=request.user.username)
        open_tickets = Ticket.objects.filter(nome=request.user.username).exclude(status=4)
        resolved_tickets = Ticket.objects.filter(nome=request.user.username, status=4)  # Adicione esta linha
        return render(request, 'tickets/user_dashboard.html', {'tickets': open_tickets, 'resolved_tickets': resolved_tickets})
    else:
        return redirect('tickets:user_login')

def manager_logout(request):
    if 'manager_id' in request.session:
        del request.session['manager_id']
    return redirect('tickets:manager_login')


def manager_dashboard(request):
    if request.user.is_authenticated and request.user.is_manager:
        tickets = Ticket.objects.exclude(status=4).order_by('prioridade', 'data_criacao')
        resolved_tickets = Ticket.objects.filter(status=4)  # Tickets resolvidos
        avg_resolution_time = resolved_tickets.annotate(
            resolution_time=ExpressionWrapper(
                F('data_atualizacao') - F('data_criacao'), output_field=fields.DurationField()
            )
        ).aggregate(Avg('resolution_time'))['resolution_time__avg']

        # Estatísticas
        total_tickets = tickets.count()
        open_tickets = tickets.filter(status=1).count()
        in_process_tickets = tickets.filter(status=2).count()
        pending_tickets = tickets.filter(status=3).count()
        resolved_tickets_count = resolved_tickets.count()

        if request.method == 'POST':
            ticket_id = request.POST.get('ticket_id')
            if ticket_id:
                new_status = int(request.POST['new_status'])
                ticket = Ticket.objects.get(pk=ticket_id)
                ticket.status = new_status
                ticket.save()
                messages.success(request, f"Status do ticket {ticket_id} atualizado.")

        context = {
            'tickets': tickets,
            'avg_resolution_time': avg_resolution_time,
            'total_tickets': total_tickets,
            'open_tickets': open_tickets,
            'in_process_tickets': in_process_tickets,
            'pending_tickets': pending_tickets,
            'resolved_tickets': resolved_tickets_count
        }
        return render(request, 'tickets/manager_dashboard.html', context)
    else:
        return redirect('tickets:user_login')


def create_ticket(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TicketForm(request.POST)
            if form.is_valid():
                ticket = form.save(commit=False)
                ticket.nome = request.user.username
                ticket.setor = request.user.setor
                ticket.status = 1  # Status "Aberto"
                ticket.save()
                return redirect('tickets:user_dashboard')
        else:
            form = TicketForm()
        return render(request, 'tickets/create_ticket.html', {'form': form})
    else:
        return redirect('tickets:user_login')
    
def edit_ticket(request, ticket_id):
    if request.user.is_authenticated:
        try:
            ticket = Ticket.objects.get(pk=ticket_id)
            if request.user.is_manager or ticket.nome == request.user.username:
                if request.method == 'POST':
                    form = TicketForm(request.POST, instance=ticket, is_manager=request.user.is_manager)
                    if form.is_valid():
                        form.save()
                        return redirect('tickets:user_dashboard')
                else:
                    form = TicketForm(instance=ticket, is_manager=request.user.is_manager)
                return render(request, 'tickets/edit_ticket.html', {'form': form})
            else:
                messages.error(request, 'Acesso negado.')
                return redirect('tickets:user_dashboard')
        except Ticket.DoesNotExist:
            messages.error(request, 'Ticket não encontrado.')
            return redirect('tickets:user_dashboard')
    else:
        return redirect('tickets:user_login')
    
def delete_ticket(request, ticket_id):
    if request.user.is_authenticated:
        try:
            ticket = Ticket.objects.get(pk=ticket_id)
            if request.user.is_manager or ticket.nome == request.user.username:
                ticket.delete()
                messages.success(request, 'Ticket excluído com sucesso.')
            else:
                messages.error(request, 'Acesso negado.')
        except Ticket.DoesNotExist:
            messages.error(request, 'Ticket não encontrado.')

        if request.user.is_manager:
            return redirect('tickets:manager_dashboard')
        else:
            return redirect('tickets:user_dashboard')
    else:
        return redirect('tickets:user_login')
    
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('tickets:user_dashboard')  # substitua 'dashboard' pelo nome da URL da página do painel do usuário
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'tickets/edit_profile.html', {'form': form})

def change_status(request, ticket_id):
    if request.user.is_authenticated and request.user.is_manager:
        if request.method == 'POST':
            try:
                ticket = Ticket.objects.get(pk=ticket_id)
                new_status = int(request.POST.get('new_status'))
                ticket.status = new_status
                ticket.save()
                return JsonResponse({'success': True, 'message': 'Status atualizado com sucesso.'})
            except Ticket.DoesNotExist:
                return JsonResponse({'success': False, 'message': 'Ticket não encontrado.'})
        else:
            return JsonResponse({'success': False, 'message': 'Método não permitido.'})
    else:
        return JsonResponse({'success': False, 'message': 'Acesso negado.'})
    
def is_manager(user):
    return user.groups.filter(name='Gerente').exists()

def ticket_notes(request, ticket_id):
    if request.user.is_authenticated:
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        if request.method == 'POST':
            nota = request.POST['nota']
            ticket.nota = nota
            ticket.save()
            messages.success(request, 'Nota atualizada com sucesso.')
            if request.user.is_manager:
                return redirect('tickets:manager_dashboard')
            else:
                return redirect('tickets:user_dashboard')
        return render(request, 'tickets/ticket_notes.html', {'ticket': ticket})
    else:
        return redirect('tickets:user_login')

    
    
