from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse

ENTRIES = []

def index(request):
    return render(request, 'index.html', {'entries': ENTRIES})

def add_entry(request):
    if request.method == "POST":
        content = request.POST.get('content')
        name = request.POST.get('name')
        name = name.capitalize()
        entry_id = len(ENTRIES) + 1
        ENTRIES.append({'id': entry_id, 'name': name, 'content': content})
        return redirect('/')
    return render(request, 'add_entry.html')

def entry(request, entry_id):
    try:
        entry = ENTRIES[int(entry_id) - 1]
        return JsonResponse(entry)
    except (IndexError, ValueError):
        return JsonResponse({'error': 'Entry not found.'})