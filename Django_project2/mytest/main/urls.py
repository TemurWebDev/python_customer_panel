from django.urls import path
from .views import index_view,customer_delete_view,customer_edit_view,customer_add_view

urlpatterns = [
    path('', index_view,name='index-url'),
    path('add',customer_add_view,name='customer-add-url'),
    path('<int:customer_id>/delete',customer_delete_view,name='customer-delete-url'),
    path('<int:customer_id>/edit',customer_edit_view,name='customer-edit-url'),
]