from django.shortcuts import render
from django.http import JsonResponse
from .models import Cliente
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        try:
            cliente = Cliente.objects.get(email=email)
            if cliente.check_senha(senha):
                return JsonResponse({'message': 'Login bem-sucedido!'})
            else:
                return JsonResponse({'message': 'Senha incorreta.'}, status=401)
        
        except Cliente.DoesNotExist:
            return JsonResponse({'message': 'Cliente não encontrado.'}, status=404)
        
    return JsonResponse({'error': 'Método não permitido'}, status=405)
