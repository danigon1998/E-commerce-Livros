from django.db import models
from django.contrib.auth.hashers import make_password

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    
    def set_senha(self, senha):
        self.senha = make_password(senha)  

    def check_senha(self, senha):
        from django.contrib.auth.hashers import check_password
        return check_password(senha, self.senha)

    def __str__(self):
        return self.nome
    
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)
    metodo_pagamento = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Pedido {self.id_pedido} - Cliente {self.cliente.nome}"
    
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto_id = models.CharField(max_length=24)
    quantidade = models.IntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('pedido', 'produto_id') 

    def __str__(self):
        return f"Item Pedido {self.pedido.id_pedido} - Produto {self.produto_id}"


