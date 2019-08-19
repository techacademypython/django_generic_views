import random
import string

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from news.forms import NewsForm
from .models import News
# class View(object):
#     method_names = ["GET", "POST"]
#
#     @staticmethod
#     def as_view(*args, **kwargs):
#         def wrapper(request, *args, **kwargs):
#             View.args = args
#             View.kwargs = kwargs
#             return View.dispatch(request, *args, **kwargs)
#         return wrapper
#
#     @staticmethod
#     def dispatch(request, *args, **kwargs):
#         if request.method in View.method_names:
#             handler = getattr(View, request.method.lower())
#             return handler(request, *args, **kwargs)
from django.views.decorators.csrf import csrf_exempt


# simple view example
class HomeView(generic.View):

    def get(self, *args, **kwargs):
        return HttpResponse("Get")

    def post(self, *args, **kwargs):
        return HttpResponse("Post")

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(HomeView, self).dispatch(request, *args, **kwargs)


# Template view
class HomePage(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = {}
        context["post_list"] = [1, 2, 3, 4]
        return context


class AddDataView(generic.View):

    def random_string(self, size):
        chars = string.ascii_letters
        return "".join([random.choice(chars) for _ in range(size)])

    def get(self, request):
        for x in range(100):
            News.objects.create(
                title=self.random_string(20),
                content=self.random_string(250)
            )
        return HttpResponse("oks")


# List view
class NewsListView(generic.ListView, LoginRequiredMixin):
    model = News
    ordering = ["-id"]
    template_name = "index.html"
    context_object_name = "news_list"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        context["test"] = [1, 2, 3]
        return context


class NewsDetailView(generic.DetailView):
    model = News
    template_name = "detail.html"


# create
class NewsCreateView(generic.CreateView):
    model = News
    form_class = NewsForm
    template_name = "news.html"
    success_url = "/list"


# Update
class NewsUpdateView(generic.UpdateView):
    model = News
    form_class = NewsForm
    template_name = "news.html"
    success_url = "/list"


# Delete View
class NewsDeleteView(generic.DeleteView):
    model = News
    form_class = NewsForm
    template_name = "news.html"
    success_url = "/list"


# Create your views here.
def home_view(request):
    return HttpResponse("Hello there")
