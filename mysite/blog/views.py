from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse,Http404
from blog.models import Blogpost
# Create your views here.
class BlogpostView(View):
    def get(self,request):
        posts=Blogpost.objects.all()
        response=[
            "{id}.{title} by {author}".format(id=p.id,title=p.title,author=p.author) for p in posts
        ]
        return HttpResponse(response)


class BlogpostDetails(View):
    def get(self,request,id):
        try:
            p=Blogpost.objects.get(id=id)
        except Blogpost.DoesNotExist:
            raise Http404
        else:
            response="""
            {id}.{title} 
            ----
            <br><br>
            by {author} """.format(id=p.id,title=p.title,author=p.author)
            return HttpResponse(response)
