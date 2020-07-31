from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from uuid import uuid4

from .forms import *
from .scripts.translate_text import *
from .scripts.translate_file import *
# from .scripts.translate_speech import *

fs = FileSystemStorage()


# Create your views here.
def index(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "index.html")


def text_view(request):
    context = {'languages': CHOICES, 'source': '', 'destination': '', 'text': '', 'translated': ''}

    # render function takes argument  - request
    # and return HTML as response
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TextForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            print(form.cleaned_data)
            # process the data in form.cleaned_data as required
            source = form.data['source']
            destination = form.data['destination']
            text = form.cleaned_data['text_area']

            translated_text = translate_text(text, destination, source)

            context['source'] = source
            context['destination'] = destination
            context['text'] = text
            context['translated'] = translated_text

            # redirect to a new URL:
            return render(request, "text.html", context)
        else:
            print("Invalid Text Form!")
    else:
        print("Invalid Text Form Request!")

    return render(request, "text.html", context)


def file_view(request):
    context = {'languages': CHOICES, 'source': '', 'destination': '', 'translated': '', 'translated_file': ''}

    # render function takes argument  - request
    # and return HTML as response
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FileForm(request.POST, request.FILES)

        # check whether it's valid:
        if form.is_valid():
            print(form.data, request.FILES)
            # process the data in form.cleaned_data as required
            source = form.data['source']
            destination = form.data['destination']

            filename, translated_text = handle_uploaded_file(request.FILES['upload_file'], destination, source)

            context['source'] = source
            context['destination'] = destination
            context['translated'] = translated_text
            context['translated_file'] = filename

            # redirect to a new URL:
            return render(request, "file.html", context)
        else:
            print("Invalid File Form!")
    else:
        print("Invalid File Form Request!")

    return render(request, "file.html", context)


def handle_uploaded_file(file, destination, source):
    temp_filename = uuid4().hex + '.' + file.name.split('.')[-1]
    filename = fs.save(temp_filename, file)
    uploaded_file_url = fs.url(filename)

    if file.name.split('.')[-1] == "txt":
        filename, translated_text = translate_file(uploaded_file_url, destination, source)
    elif file.name.split('.')[-1] == "pdf":
        filename, translated_text = translate_pdf(uploaded_file_url, destination, source)
    else:
        filename, translated_text = translate_docs(uploaded_file_url, destination, source)

    return filename, translated_text


def speech_view(request):
    context = {'languages': SPEECH_CHOICES, 'source': '', 'destination': '', 'text': '', 'translated': ''}

    # render function takes argument  - request
    # and return HTML as response
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TextForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            print(form.cleaned_data)
            # process the data in form.cleaned_data as required
            source = form.data['source']
            destination = form.data['destination']
            text = form.cleaned_data['text_area']

            translated_text = translate_text(text, destination, source)

            context['source'] = source
            context['destination'] = destination
            context['text'] = text
            context['translated'] = translated_text

            # redirect to a new URL:
            return render(request, "speech.html", context)
        else:
            print("Invalid Speech Form!")
    else:
        print("Invalid Speech Form Request!")

    return render(request, "speech.html", context)

