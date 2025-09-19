
from itertools import count
from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .forms import Form_Etudiant, Form_Etage, FormAUberge, FormTypeChambre, FormChambre, FormHabiter, Form_Login, CustomAuthenticationForm, user_cerateForm
from .models import Etudiant, Etage, Auberge, TypeChambre, Chambre, Habiter
from django.db.models import Count, Q



def inscription(request):
    if request.method=='POST':
        form=Form_Login(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user) 
            return redirect('login')
    else:
        form=Form_Login()
    return render(request, 'login/inscription.html', {'form': form})
def login(request):
    if request.method=='POST':
        form=CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            
            return  redirect('home')
    else:
        messages.error(request, "Nom d’utilisateur ou mot de passe incorrect.")
        form=CustomAuthenticationForm()
        
    return render (request, 'login/login.html', {'form':form})
    
def deconnexion(request):
    return render(request)









# Create your views here.
def page_accueil(request):
    
    return render(request, 'etudiant/pageAccueil.html', {'date': datetime.now()})

def ajout(request):
    if request.method =='POST':
        form=Form_Etudiant(request.POST)
        if form.is_valid():
            form.save()
    form=Form_Etudiant()

    return render(request,'etudiant/ajouter.html',{'form':form})

def affiche(request):
    etud=Etudiant.objects.all()
    context= {'etud':etud}
    return render(request, 'etudiant/affiche.html',context)
def liste_etudiant(request):
    etud=Etudiant.objects.all()
    context= {'etud':etud}
    return render(request, 'etudiant/liste_etudiant.html',context)
def modifier_e(request,pk):
    eleve=get_object_or_404(Etudiant,id=pk)
    context=None
    if request.method=="POST":
        form=Form_Etudiant(request.POST, instance=eleve)
        if form.is_valid():
            form.save()
            redirect('affiche')
    else:
        form=Form_Etudiant(instance=eleve)
        context={
            'eleve':eleve,
            'form':form
        }
    return render(request, 'etudiant/modifier.html', context)


def delete_e(request,pk):
    eleve=get_object_or_404(Etudiant,id=pk)
    eleve.delete()
    return  redirect('affiche')
def ajout_etage(request):
    
    if request.method== "POST":
        
        form= Form_Etage(request.POST)
        if form.is_valid():
           form.save()
        
    form= Form_Etage()
    return render(request,'etudiant/etage.html', {'form': form} )


def enregitrer_auberge(request):
   
    if request.method=='POST':

        form=FormAUberge(request.POST)
        if form.is_valid():
            nombre=request.POST.get('nombreEtage')
           
            auberge=form.save()
            for i in range(int(nombre)):
                    Etage.objects.create(
                        nomEtage=f"Etage N° {i+1}",
                        numAuberge=auberge
                    )
    form=FormAUberge()
    return render(request, 'auberge/ajout_auberge.html',{'form': form})
def ajout_chambre(request):
    if request.method=="POST":
       
        form=FormChambre(request.POST)
        if form.is_valid():
            chambre= request.POST.get('nombreChambre')
            
            types=form.cleaned_data['numTypeChambre']
            etag=form.cleaned_data['etage']
        
            for i in range(int(chambre)):
                    Chambre.objects.create(
                        nomChambre=f"Chambre N° {i+1}",
                        numTypeChambre=types,
                        etage=etag
                        )

    form= FormChambre()
    return render(request,'auberge/ajout_chambre.html',{'form': form} )

   
def liste_chambre(request,pk):
    chambre= Chambre.objects.annotate(nommbre_de_personne=Count('vivre')).filter(numTypeChambre=pk)    
    return render(request, 'auberge/listechambre.html', {'chamb':chambre})
   


def liste_aub(request):
    aub=Auberge.objects.all()
    context= {'aub':aub}
    return render(request, 'auberge/Liste_aub.html',context)
def liste_etage(request):
    etag= Etage.objects.all()
    context={'etag': etag}
    return render(request, 'auberge/liste_etage.html', context)
def ajout_type_chambre(request):
    if request.method=="POST":
        form= FormTypeChambre(request.POST)
        if form.is_valid():
            form.save()
    form= FormTypeChambre()
    return render(request, 'auberge/ajout_type_chambre.html', {'form':form})
    

def les_etages_de_aub(request,pk):
    etages=Etage.objects.filter(numAuberge=pk)

    return render(request,'auberge/etages_par_aub.html', {'etag': etages})
def liste_type_chambre(request):
    type=TypeChambre.objects.all()
    return render(request, 'auberge/liste_type_chambre.html', {'type': type})
def ajout_habiter(request):
    if request.method=="POST":
        form=FormHabiter(request.POST)
        if form.is_valid():
            form.save()
    form=FormHabiter()
    return render(request, 'auberge/ajout_habiter.html', {'form':form})
def liste_habiter(request,pk):
    habite=Habiter.objects.filter(numChambre=pk)
    return render(request,'auberge/liste_habiter.html',{'habite': habite})
def contact(request):
    return render(request, 'etudiant/contact.html')
