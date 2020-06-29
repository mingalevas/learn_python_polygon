from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView


class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context
