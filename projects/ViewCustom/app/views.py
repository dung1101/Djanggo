import csv
import io
from random import randrange

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.template import Context, loader
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic.base import View, TemplateView, RedirectView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView
from reportlab.pdfgen import canvas

from .forms import BuyForm
from .models import Game, Manufacturer


def page_not_found(request):
    return HttpResponse("<h1>404</h1>")


def server_error(request):
    return HttpResponse("<h1>500</h1>")


@csrf_exempt
def index(request):
    man_num = randrange(1, Manufacturer.objects.all().count()+1)
    game_num = randrange(1, Game.objects.all().count()+1)
    return render(request, "index.html", {'man_num': man_num, 'game_num': game_num})


def detail(request, pk):
    return HttpResponse("Detail")


def test(request):
    return HttpResponseRedirect(reverse('app:index'))


@require_POST
def post_only(request):
    return HttpResponse("Post only")


def csv_render_python_library(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="test_file.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response


def csv_render_template(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    csv_data = (
        ('First row', 'Foo', 'Bar', 'Baz'),
        ('Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"),
    )

    t = loader.get_template('csv_render_template.txt')
    c = {
        'data': csv_data,
    }
    response.write(t.render(c))
    return response


def pdf_render(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


"""
*********************************** Chú ý *************************************************************
*                                                                                                     *
* Nếu chỉ muốn class có sẵn mà ko viết lại gì cả có thể gọi trực tiếp ở urls.py và truyền tham số vào *
*                                                                                                     *
*******************************************************************************************************
"""


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
    """
    mặc định bên dưới templete sử dụng biến object để lấy giá trị 
    có thể đổi tên biên bằng thuộc tính content_object_name 
    
    content_object_name = game
    """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hihi'] = "get get get get"
        return context


class LiVi(ListView):
    model = Manufacturer
    template_name = 'li_vi.html'
    """
    Mặc định sẽ get all có thể thay đổi bằng thuộc tính queryset
    
    queryset = Manufacturer.objects.filter(...)
    """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hihi'] = "get get get get"
        return context


class FormVi(FormView):
    template_name = 'form_vi.html'
    form_class = BuyForm
    success_url = reverse_lazy('app:index')
    """
        Nếu không khai báo success_url thì trong model phải viết hàm get_absolute_url()
        
        def get_absolute_url(self):
            return reverse('app:index', kwargs={'pk': self.pk})
    """

    def form_invalid(self, form):
        print('invalid')
        return super().form_invalid(form)

    def form_valid(self, form):
        print('valid')
        return super().form_valid(form)


class CreateVi(CreateView):
    model = Manufacturer
    fields = ['name', 'money']
    template_name = 'create_vi.html'
    success_url = reverse_lazy('app:list_view')


class UpdateVi(UpdateView):
    model = Manufacturer
    fields = ['money']
    template_name = 'update_vi.html'
    success_url = reverse_lazy('app:list_view')


class DeleteVi(DeleteView):
    model = Manufacturer
    template_name = 'delete_vi.html'
    success_url = reverse_lazy('app:list_view')


class ArchiveIndexVi(ArchiveIndexView):
    """
    A top-level index page showing the “latest” objects, by date.
    Objects with a date in the future are not included unless you set allow_future to True.
    """
    pass


class YearArchiveVi(YearArchiveView):
    """
    A yearly archive page showing all available months in a given year.
    Objects with a date in the future are not displayed unless you set allow_future to True.
    """
    queryset = Game.objects.all()
    date_field = "release"
    make_object_list = True
    allow_future = True
    template_name = "year_archive_vi.html"


"""
Mixin là gì:

"""