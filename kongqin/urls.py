from django.urls import path

from . import views

urlpatterns = [
    path('lst', views.lst),
    path('content', views.article_content),
    path('', views.get_index_page),
    # path('detail', views.get_detail_page)
    path('detail/<int:article_id>', views.get_detail_page)
]