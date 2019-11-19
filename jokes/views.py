from django.shortcuts import render

from jokes.models import Joke


def joke_index(request):
    jokes = Joke.objects.all()
    context = {"jokes": jokes}
    return render(request, "joke_index.html", context)


def joke_category(request, joketype):
    jokes = Joke.objects.filter(joketype__name__contains=joketype)
    context = {"joketype": joketype, "jokes": jokes}
    return render(request, "joke_category.html", context)


def joke_detail(request, pk):
    joke = Joke.objects.get(pk=pk)

    context = {"joke": joke}
    return render(request, "joke_detail.html", context)