from django.shortcuts import render
from .models import Food
from django.views import generic

# Create your views here.
def show(request):
    posts = Food.objects.all()
    context = {'posts': posts}
    return render(request, 'webs/index.html', context)


class PostDetail(generic.DetailView):
    model = Food
    template_name = 'webs/detail.html'
    context_object_name = 'posts'