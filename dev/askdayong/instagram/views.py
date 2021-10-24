from django.contrib.auth.decorators import login_required
from django.views.generic.dates import ArchiveIndexView
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from typing import Pattern
from django.db.models.query import QuerySet
from django.http import response
from django.http.response import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Post
from instagram import models


#post_lsit = ListView.as_view(models=Post)
pattern_name = 'instagram'

# post_list = ListView.as_view(model=Post, paginate_by=10)


# @method_decorator(login_required, name='dispatch')
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 10


post_list = PostListView.as_view()

# @login_required
# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')
#     if q:
#         qs = qs.filter(message__icontains=q)
#     # instagram/templates/instagram/post_list.html
#     return render(request, 'instagram/post_list.htm',{
#         'post_list': qs,
#         'q':q,
#     } )


# def post_detail(request: HttpResponse, pk:int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'instagram/post_detail.htm', {
#         'post':post,
#     })


# 클래스 기반으로 작성 위의 함수와 동일 기능
# post_detail = DetailView.as_view(
#     model=Post,
#     queryset=Post.objects.filter(is_public=True))

class PostDetailView(DetailView):
    model = Post

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)

        return qs


post_detail = PostDetailView.as_view()


# def archives_year(request, year):
#     return HttpResponse(f"{year}년 archives")


post_archive = ArchiveIndexView.as_view(
    model=Post, date_field='created_at', paginate_by=10)
