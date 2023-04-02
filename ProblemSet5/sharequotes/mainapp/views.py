from django.shortcuts import render, redirect
from django.http import JsonResponse
from mainapp.models import Person, Quote
from mainapp.forms import QuoteForm

def index(request):
    return render(request, 'index.html', {'entries': Quote.objects.all()})

def add_entry(request):
    form = QuoteForm()
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.person = form.cleaned_data['person']
            quote.save()
            return redirect('index')
    return render(request, 'add_entry.html', {'form': form})

def entry(request, quote_id):
    try:
        quote = Quote.objects.get(id=quote_id)
        return JsonResponse({'id': quote.id, 'person': quote.person.name, 'content': quote.content})
    except Quote.DoesNotExist:
        return JsonResponse({'error': 'Quote not found.'})