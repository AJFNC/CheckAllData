
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def index(request):
        now = datetime.now()

        return render(
                    request,
                    "CheckDApp/index.html",  # Relative path from the 'templates' folder to the template file
                    # "index.html", # Use this code for VS 2017 15.7 and earlier
                    {
                        'content': "Fala galera no " + now.strftime("%A, %d %B, %Y at %X"),
                        'title': "Verifica dados da Bluewater",
                        'message': "Teste de variaveis: "
                    }
               )

