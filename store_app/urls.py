from django.urls import path
from .views import ProductView,UpdateDeleteProduct, UserListCreateView,UserRetrieveUpdateDeleteView

urlpatterns=[
    path('products/', ProductView.as_view(), name='listproduct'),
    path('products/<str:pk>/', UpdateDeleteProduct.as_view(),name='product_detail'),
    path('users/', UserListCreateView.as_view(), name='userlist' ),
    path('users/<str:pk>/', UserRetrieveUpdateDeleteView.as_view(), name='user-update'),

]