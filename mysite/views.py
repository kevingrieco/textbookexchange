import requests

from django.views.generic import ListView
from django.db.models import Q

from post_textbook.models import Textbook

class HomePageView(ListView):
    model = Textbook
    template_name = 'index.html'

class SearchResultsView(ListView):
    model = Textbook
    template_name = 'search_results.html'

    def get_queryset(self):
        q = self.request.GET.get('q')
        object_list = Textbook.objects.filter(
            Q(title__icontains=q) | Q(author__icontains=q)
        )
        return object_list