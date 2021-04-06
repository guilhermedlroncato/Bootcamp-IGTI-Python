from django.shortcuts import render
from django.http import HttpResponseNotAllowed, HttpResponse
from . import forms
from . import models

def cadastro(request):
        
    form = forms.SerieForm()

    if request.method == 'POST':
        form = forms.SerieForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
        else:
            print('ERROR')
    
    serie_list = models.Serie.objects.order_by('nome')
    
    data_dict = {
        'form': form,
        'serie_records': serie_list
    }
    
    return render(request, 'serie/serie.html', data_dict)

def delete(request, id):
    try:
        models.Serie.objects.filter(id = id).delete()
        form = forms.SerieForm()
        serie_list = models.Serie.objects.order_by('nome')
        data_dict = {
            'form': form,
            'serie_records': serie_list
        }
        return render(request, 'serie/serie.html', data_dict)
    except:
        return HttpResponseNotAllowed()

def update(request, id):
    item = models.Serie.objects.get(id = id)
    if request.method == 'GET':
        form = forms.SerieForm(initial = {'nome': item.nome})
        data_dict = {
            'form': form
        }
        return render(request, 'serie/serie_upd.html', data_dict)
    else:
        form = forms.SerieForm(request.POST)
        item.nome = form.data['nome']
        item.save()
        serie_list = models.Serie.objects.order_by('nome')
        data_dict = {
            'form': form,
            'serie_records': serie_list
        }
        return render(request, 'serie/serie.html', data_dict)
