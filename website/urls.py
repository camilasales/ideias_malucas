from django.urls import path, include
# aqui deve ser importado os meodos da viws
# é uma má pratica importar um de cada vez
from website.views import index, sobre, login, cadastrar_ideia, remover_ideia

urlpatterns = [
    path('', index),
    path('sobre', sobre),
    path('login', login),
    path('ideias', cadastrar_ideia),
    path('remover_ideia/<int:id>', remover_ideia)
]
