from django.contrib import admin

from .models import Etudiant
from .models import Auberge
from .models import Etage
from .models import TypeChambre
from .models import Chambre
from .models import Habiter
from .models import CustomUser
# Register your models here.
class AdminEtudiant(admin.ModelAdmin):
    list_display=('nom','prenom','numPossport','telephone','email','domFormation','dateNaissance','sexe')
admin.site.register(Etudiant,AdminEtudiant)
class AdminEtage(admin.ModelAdmin):
    list_display=('nomEtage','numAuberge' )
admin.site.register(Auberge)
admin.site.register(Etage, AdminEtage)
admin.site.register(TypeChambre)
admin.site.register(Chambre)
admin.site.register(Habiter)
admin.site.register(CustomUser)

