from django.urls import path
from blog.views import (
    create_blog_view,
    detail_blog_view,
    edit_blog_view,
    delete_blog_post,
    create_tag_view,
    delete_tag,
    update_tag_view,
)

app_name = 'blog'

urlpatterns = [
    path('createtag/', create_tag_view, name="createtag"),
    path('updatetag/', update_tag_view, name="updatetag"),
    path('create/', create_blog_view, name="create"),
    path('<slug>/', detail_blog_view, name="detail"),
    path('<slug>/edit/', edit_blog_view, name="edit"),
    path('delete/<int:id>/', delete_blog_post, name="delete"),
    path('deletetag/<int:id>/', delete_tag, name="deletetag"),
]
