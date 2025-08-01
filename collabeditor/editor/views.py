from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
import language_tool_python
from django.http import JsonResponse
from .models import Document , DocumentVersion
import requests
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from textblob import TextBlob


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'editor/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'editor/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    documents = Document.objects.filter(owner=request.user)
    return render(request, 'editor/dashboard.html', {'documents': documents})


@login_required
def document_editor(request, doc_id):
    document = get_object_or_404(Document, pk=doc_id)
    return render(request, 'editor/editor.html', {'document': document, 'doc_id': doc_id})


@login_required
def dashboard(request):
    documents = Document.objects.filter(owner=request.user)
    return render(request, 'editor/dashboard.html', {'documents': documents})

@login_required
def create_document(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content', '')
        doc = Document.objects.create(title=title, content=content, owner=request.user)
        return redirect('document_editor', doc_id=doc.id)
    return render(request, 'editor/create_document.html')


def grammar_suggestions(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        blob = TextBlob(text)
        corrected = str(blob.correct())

        suggestions = []
        if corrected != text:
            suggestions.append({
                'message': 'Spelling/Grammar suggestion',
                'replacements': [corrected],
                'offset': 0,
                'length': len(text)
            })

        return JsonResponse({'suggestions': suggestions})