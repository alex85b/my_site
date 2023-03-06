from django.shortcuts import render
from django.views import View

# Create your views here.


class IndexView(View):
    def get(self, request):
        return render(request, "portfolio/index.html")

    def post(self, request):
        # This should be reconsidered !
        return render(request, "portfolio/index.html")