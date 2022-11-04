from django.shortcuts import render
from post_textbook.models import Department, Textbook
from django.views.generic import ListView
from django.db.models import Q


def index_view(request):
    departments = Department.objects.order_by('name')
    context = {
        'departments': departments,
    }
    return render(request, 'index.html', context)


class SearchResultsView(ListView):
    model = Textbook
    template_name = 'search_results.html'

    def get_queryset(self):
        q = self.request.GET.get('q')
        object_list = Textbook.objects.filter(
            Q(title__icontains=q) | Q(author__icontains=q)
        )
        return object_list
