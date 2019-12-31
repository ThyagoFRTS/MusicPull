from django.contrib import admin
from .models import Musicas
from .models import Albuns
from .models import Vendas
from .models import Clientes
from .models import Logins
# Register your models here.

admin.site.register(Musicas)
admin.site.register(Albuns)
admin.site.register(Vendas)
admin.site.register(Clientes)
admin.site.register(Logins)
