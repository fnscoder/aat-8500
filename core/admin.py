from django.contrib import admin
from .models import Atuacao, Carro, Falha, Trem


admin.site.register(Atuacao)
admin.site.register(Carro)
admin.site.register(Falha)
admin.site.register(Trem)
