from django.urls import path
from page.views import (
    home,
    about_us,
    contact,
    vision,
    page_view
)

urlpatterns = [
    path('', home, name='home'),
    # path("about/", about_us, name='about_us'),
    # path("contact/", contact, name='contact'),
    # path("vision/", vision, name='vision'),
    path("<slug:slug>/", page_view),
]
