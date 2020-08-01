from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from uuid import uuid4
from django.http import JsonResponse

from .forms import *
from .scripts.translate_text import *
from .scripts.translate_file import *
from .scripts.translate_speech import *

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
        print("GET Request!")

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
            # process the data in form.cleaned_data as required
            source = form.data['source']
            destination = form.data['destination']

            filename, translated_text = handle_text_file(request.FILES['upload_file'], destination, source)

            context['source'] = source
            context['destination'] = destination
            context['translated'] = translated_text
            context['translated_file'] = filename

            # redirect to a new URL:
            return render(request, "file.html", context)
        else:
            print("Invalid File Form!")
    else:
        print("GET Request!")

    return render(request, "file.html", context)


def rename_and_store(file, binary=False):
    if binary:
        temp_filename = uuid4().hex + ".wav"
    else:
        temp_filename = uuid4().hex + '.' + file.name.split('.')[-1]

    filename = fs.save(temp_filename, file)
    uploaded_file_url = fs.url(filename)
    return uploaded_file_url


def handle_text_file(file, destination, source):
    uploaded_file_url = rename_and_store(file)

    if file.name.split('.')[-1] == "txt":
        filename, translated_text = translate_file(uploaded_file_url, destination, source)
    elif file.name.split('.')[-1] == "pdf":
        filename, translated_text = translate_pdf(uploaded_file_url, destination, source)
    else:
        filename, translated_text = translate_docs(uploaded_file_url, destination, source)

    return filename, translated_text


def speech_view(request):
    context = {'languages': SPEECH_CHOICES}
    print("GET Request!")
    return render(request, "speech.html", context)


def translate_speech_view(request):
    # return JSON as response with status code
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = SpeechForm(request.POST, request.FILES)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            source = form.data['source']
            destination = form.data['destination']

            filename, translated_text = handle_audio_file(request.FILES['audio_file'], destination, source)

            response = {
                'translated': translated_text,
                'translated_file': filename
            }

            # send to client side
            return JsonResponse(response, status=200, safe=False)
        else:
            # some form errors occurred
            return JsonResponse({"error": form.errors}, status=400)
    else:
        print("GET Request!")


def handle_audio_file(binary_file, destination, source):
    uploaded_file_url = rename_and_store(binary_file, binary=True)

    filename, translated_text = translate_speech(uploaded_file_url, destination, source)

    return filename, translated_text
