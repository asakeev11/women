from django.urls import path, re_path, register_converter
from . import views
from . import convertors


register_converter(convertors.FourDigitYearConvertor, 'year4')
urlpatterns = [
    path('', views.WomenHome.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.AddPage.as_view(), name='addpage'),
    path('contact/', views.contact, name='contact'),
    # path('login/', login_user, name='login'),
    path('post/<slug:post_slug>/', views.ShowPOst.as_view(), name='post'),
    path('category/<slug:category_slug>/', views.WomenCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.ShowTagPostList.as_view(), name='tag'),
    path('edit/<int:pk>/', views.UpdatePage.as_view(), name='edit'),

]
