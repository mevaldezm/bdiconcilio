from django.contrib import admin

# Register your models here.
from .models import Evento, Promocion, FechaEvento, Exposicion, Expositor, Localidad, Participante, Registro, AgentePago, Recibo

admin.site.register(Evento)
admin.site.register(Promocion)
admin.site.register(FechaEvento)
admin.site.register(Exposicion)
admin.site.register(Expositor)
admin.site.register(Localidad)
admin.site.register(Participante)
admin.site.register(Registro)
admin.site.register(AgentePago)
admin.site.register(Recibo)

