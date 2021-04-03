from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from . import forms
from . import models

def cadastro(request):
    form = forms.GeneroForm()

    if request.method == 'POST':
        form = forms.GeneroForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
        else:
            print('ERROR')
    
    genero_list = models.Genero.objects.order_by('descricao')
    
    data_dict = {
        'form': form,
        'genero_records': genero_list
    }
    
    return render(request, 'genero/genero.html', data_dict)

def delete(request, id):
    try:
        models.Genero.objects.filter(id = id).delete()
        form = forms.GeneroForm()
        genero_list = models.Genero.objects.order_by('descricao')
        data_dict = {
            'form': form,
            'genero_records': genero_list
        }
        return render(request, 'genero/genero.html', data_dict)
    except:
        return HttpResponseNotAllowed()

def update(request, id):
    item = models.Genero.objects.get(id = id)
    if request.method == 'GET':
        form = forms.GeneroForm(initial = {'descricao': item.descricao})
        data_dict = {
            'form': form
        }
        return render(request, 'genero/genero_upd.html', data_dict)
    else:
        form = forms.GeneroForm(request.POST)
        item.descricao = form.data['descricao']
        item.save()
        genero_list = models.Genero.objects.order_by('descricao')
        data_dict = {
            'form': form,
            'genero_records': genero_list
        }
        return render(request, 'genero/genero.html', data_dict)



