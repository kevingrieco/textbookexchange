from django.shortcuts import render, redirect
from post_textbook.models import Department, Course, Textbook
from .models import Favorites

# Create your views here.
def save_textbook(request, pk):
    textbook = Textbook.objects.get(pk=pk)
    try:
        favorites_list = Favorites.objects.get(user=request.user)
    except:
        favorites_list = Favorites(user=request.user)
        favorites_list.save()
    in_favorites = request.POST.get('in_favorites') == 'True'
    if in_favorites:
        favorites_list.textbooks.remove(textbook)
    else:
        favorites_list.textbooks.add(textbook)
    return redirect('save_textbook:favorites')

def favorites(request):
    try:
        favorites_list = Favorites.objects.get(user=request.user)
    except:
        favorites_list = Favorites(user=request.user)
        favorites_list.save()
    favorites_list = favorites_list.textbooks.all()
    departments = {}
    for textbook in favorites_list:
        if not textbook.department in departments:
            departments[textbook.department] = {textbook.course: []}
        departments[textbook.department][textbook.course].append(textbook)
    return render(request, 'save_textbook/favorites.html', {'departments': departments, 'empty': len(departments)==0})


