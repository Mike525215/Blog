from django.urls import path
from blog.views import *

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('sign_up/', sign_up_user, name='sign_up_user'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout'),
    path('create_blog/', CreateBlog.as_view(), name='create_blog'),
    path('personal_blogs/', PersonalBlogs.as_view(), name='personal_blogs'),
    path('blog/detail/<int:blog_id>/', BlogDetail.as_view(), name='blog_detail'),
    path('blog/modified/<int:blog_id>/', modified_blog, name='modified_blog'),
    path('blog/delete/<int:blog_id>/', delete_blog, name='delete_blog')
]