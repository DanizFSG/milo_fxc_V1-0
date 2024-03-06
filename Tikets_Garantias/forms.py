from django.contrib.auth.forms import UserCreationForm
from .models import Models_Tickets

class Register_tikets(UserCreationForm):
    class Meta:
        model = Models_Tickets
        fields = ['cliente', 'correo_ticket', 'empresa','refereencia','serial','marca', 'garantia', 'fecha_ingreso', 'fecha_salida', 'foto_equipo', 'foto_1', 'foto_2']
