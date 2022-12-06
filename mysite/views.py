from django.shortcuts import render
from post_textbook.models import Department, Textbook
from django.views.generic import ListView
from django.db.models import Q
from save_textbook.models import Favorites


def index_view(request):
    departments = Department.objects.order_by('name')
    try:
        favorites = Favorites.objects.get(user=request.user)
    except:
        favorites = Favorites(user=request.user)
        favorites.save()
    favorites = favorites.textbooks.all()
    context = {
        'departments': departments,
        'favorites': favorites,
    }
    return render(request, 'index.html', context)


class SearchResultsView(ListView):
    model = Textbook
    template_name = 'search_results.html'

    def get_queryset(self):
        q = self.request.GET.get('q')
        object_list = Textbook.objects.filter(
            Q(title__icontains=q) | Q(author__icontains=q) | Q(publisher__icontains=q) | Q(department__name__icontains=q) | Q(course__name__icontains=q)
        )
        return object_list
