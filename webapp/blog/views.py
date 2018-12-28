from django.template import loader, Context
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import BlogPost


def archive(request):
    posts = BlogPost.objects.all()
    template = loader.get_template('blog/list.html')
    context = {'posts':posts}
    return HttpResponse(template.render(context))
