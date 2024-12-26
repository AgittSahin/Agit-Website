from django.shortcuts import render
from django.http import HttpResponse, Http404
from random import randint
from page.fake_db.pages import FAKE_DB_PAGES

# Create your views here.

FAKE_DB_CAROUSEL = [
    f"https://picsum.photos/id/{id}/1200/390" for id in range(60,64)
]

def home(request):
    # context = {"platform": f"Django Platform has been used. {randint(1,100)}"}
    page_title = ""
    hero_title = ""
    hero_content = """lorem ipsum soksum siksum sensum sidou seide hakli hakdel
    lorem ipsum soksum siksum sensum lensum denusi kenoli"""
    context = dict(
        hero_title=hero_title,
        page_title=page_title,
        hero_content=hero_content,
        #projects=FAKE_DB_PROJECTS,
        carousel=FAKE_DB_CAROUSEL,
        )
    return render(request, "page/home_page.html", context)

def about_us(request):
    page_title = "About"
    hero_title = ""
    hero_content = "lorem ipsum soksum siksum sensum lensum denusi kenoli sidou seide hakli hakdel"
    context = dict(
        hero_title=hero_title,
        hero_content=hero_content,
        page_title=page_title,
        #projects=FAKE_DB_PROJECTS
        )
    return render(request, "page/about_us.html", context)

def contact(request):
    page_title = "Contact"
    hero_title = ""
    hero_content = "lorem ipsum soksum siksum sensum lensum denusi kenoli sidou seide hakli hakdel"
    context = dict(
        hero_title=hero_title,
        hero_content=hero_content,
        page_title=page_title,
        #projects=FAKE_DB_PROJECTS
        )
    return render(request, "page/contact.html", context)

def vision(request):
    page_title = "Vision"
    hero_title = ""
    hero_content = "lorem ipsum soksum siksum sensum lensum denusi kenoli sidou seide hakli hakdel"
    context = dict(
        hero_title=hero_title,
        hero_content=hero_content,
        page_title=page_title,
        #projects=FAKE_DB_PROJECTS
        )
    return render(request, "page/vision.html", context)

def page_view(request, slug):

    result = list(filter(lambda x: (x['url'] == slug), FAKE_DB_PAGES))
    if result:
        context = dict(
            #projects=FAKE_DB_PROJECTS,
            hero_title=result[0]["hero_title"],
            page_title=result[0]["title"],
            detail=result[0]["detail"],
            hero_content=result[0]["hero_content"],
        )
        return render(request, "page/page_detail.html", context)
    raise Http404
