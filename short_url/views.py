from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from short_url.models import Shortener
from short_url.forms import ShortenerForm


def homepage_view(request):
    template = "pages/home.html"

    context = {}

    context["form"] = ShortenerForm()

    if request.method == "GET":
        return render(request, template, context)

    elif request.method == "POST":

        used_form = ShortenerForm(request.POST)

        if used_form.is_valid():
            shortened_object = used_form.save()

            new_url = request.build_absolute_uri("/") + shortened_object.short_url

            full_url = shortened_object.full_url

            context["new_url"] = new_url
            context["full_url"] = full_url

            return render(request, template, context)

        context["errors"] = used_form.errors

        return render(request, template, context)


def redirect_url_view(request, shortened_part):
    try:
        shortener = Shortener.objects.get(short_url=shortened_part)

        shortener.times_followed += 1

        shortener.save()

        return HttpResponseRedirect(shortener.full_url)

    except:
        raise Http404("Sorry this link is broken :(")
