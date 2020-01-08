from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, ListView
from posts.models import Post
from django.http import HttpResponse


def func_view(request):
    return HttpResponse("Function view response")


class ListPostView(ListView):
    model = Post
    template_name = 'post_list.html'


class PostView(View):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        return render(request, 'post_html.html', {"post": post})
