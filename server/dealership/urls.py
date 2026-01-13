"""
URL configuration for dealership project.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    # Landing page (shows first)
    path('', TemplateView.as_view(template_name='Landing.html'), name='landing'),
    
    # Authentication
    path('login/', TemplateView.as_view(template_name='Login.html'), name='login'),
    path('welcome/', TemplateView.as_view(template_name='LoggedIn.html'), name='logged_in'),
    
    # Main pages
    path('dealerships/', TemplateView.as_view(template_name='Dealerships.html'), name='dealerships'),
    path('about/', TemplateView.as_view(template_name='About.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='Contact.html'), name='contact'),
    
    # Dealer details and review pages
    re_path(r'^dealer/(?P<dealer_id>\d+)/$', TemplateView.as_view(template_name='DealerDetails.html'), name='dealer_details'),
    re_path(r'^dealer/(?P<dealer_id>\d+)/review/$', TemplateView.as_view(template_name='ReviewForm.html'), name='dealer_review'),
    
    # Admin and API
    path('admin/', admin.site.urls),
    path('djangoapp/', include('djangoapp.urls')),
]
