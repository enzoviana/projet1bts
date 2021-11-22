from django.shortcuts import render
from django.http import HttpResponse
from instagramapp.models import *


def vue(request):
    #return HttpResponse("<h1> Bienvuenue sur instatech</h1>")
    media = Media.objects.all()
    return render(request, "instagramapp/index.html",
                  context ={"media" : media})

def listeCommentaire(request, id):
    commentaire = Commentaire.objects.get(id=id)
    return render(request, 'instagramapp/liste_Commentaire.html',
                  {"commentaire" : commentaire})
