from django.shortcuts import render
from post_textbook.models import Department, Textbook
from django.views.generic import ListView
from django.db.models import Q
from save_textbook.models import Favorites


def index_view(request):
    departments = Department.objects.order_by('name')
    if request.user.is_authenticated:
        try:
            favorites = Favorites.objects.get(user=request.user)
        except:
            favorites = Favorites(user=request.user)
            favorites.save()
        favorites = favorites.textbooks.all()
    else:
        favorites = None
    context = {
        'departments': departments,
        'favorites': favorites,
    }
    return render(request, 'index.html', context)




def search(request):
    q = request.GET.get('q')
    object_query = Q(title__icontains=q) | Q(author__icontains=q) | Q(publisher__icontains=q) | Q(department__name__icontains=q) | Q(course__name__icontains=q)
    object_query |= Q(course__instructor__icontains=q)
    
    try:
        object_query |= Q(ISBN=int(q))
    except ValueError:
        pass
    try:
        object_query |= Q(year=int(q))
    except ValueError:
        pass
    try:
        object_query |= Q(edition=int(q))
    except ValueError:
        pass
    
    textbooks = Textbook.objects.filter(object_query)
    departments = {}
    for textbook in textbooks:
        if not textbook.department in departments:
            departments[textbook.department] = {textbook.course: []}
        departments[textbook.department][textbook.course].append(textbook)
    return render(request, 'search_results.html', {'departments': departments})
