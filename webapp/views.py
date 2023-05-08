from django.shortcuts import HttpResponse, render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages


# use class based views from the models instead of functional, e.g for a Post in models:
#from .models import Post

# class PostList(generic.ListView):
#     model = Post
#     queryset = Post.objects.filter(status=1).order_by("-created_on")
#     template_name = "index.html"
#     paginate_by = 6

# Create your views here.

class PlaceholderView(View):
    message = 'Placeholder HTML from class view.'
    
    def get(self, request):
        return HttpResponse(self.message)