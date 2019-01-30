from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.detail import DetailView

from .models import Game


def page_not_found(request):
    return HttpResponse("<h1>404</h1>")

def server_error(request):
    return HttpResponse("<h1>500</h1>")


@csrf_exempt
def index(request):
    return HttpResponse("Index")


def detail(request, pk):
    return HttpResponse("Detail")


def test(request):
    return HttpResponseRedirect(reverse('app:index'))


@require_POST
def post_only(request):
    return HttpResponse("Post only")


class NormalView(View):
    template_name = 'normal_vi.html'

    def get(self, request):
        return render(request, self.template_name, {'hahaha': 'get get get'})

    def post(self, request):
        return render(request, self.template_name, {'hahaha': 'post post post'})


class TempVi(TemplateView):
    template_name = 'temp_vi.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hihi'] = "get get get get"
        return context


class ReVi(RedirectView):
    # url = '/' # hard code
    pattern_name = 'app:index'


class DeVi(DetailView):
    model = Game
    template_name = 'de_vi.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hihi'] = "get get get get"
        return context


class LiVi(ListView):
    model = Game
    template_name = 'li_vi.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hihi'] = "get get get get"
        return context
