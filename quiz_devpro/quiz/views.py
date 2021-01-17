from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def indice(requisicao):
    return HttpResponse('Hello world!!')



#def indice(requisicao):
#    return render(requisicao, 'quiz/indice.html')

#def perguntas(requisicao):
#    return render(requisicao, 'quiz/pergunta.html')

#def classificacao(requisicao):
#    return render(requisicao, 'quiz/classificacao.html')
