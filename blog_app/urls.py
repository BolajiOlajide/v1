"""URL Definition for Bucketlist application."""
from django.urls import re_path

from blog_app.views import index

urlpatterns = [
    re_path(r'^$', index, name="homepage"),
    # url(r'^dashboard/$', views.dashboard, name="dashboard"),
    # url(r'^bucketlist/(?P<bucketlist_id>[0-9]+)/$',
    #     views.bucketlist_details, name="details"),
    # url(r'^bucketlist/(?P<bucketlist_id>[0-9]+)/delete/$',
    #     views.delete_bucketlist, name="delete_bucketlist"),
    # url(r'^logout/$', views.logout_view, name="auth_logout")
]
