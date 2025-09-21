from django.urls import path
from main.views import show_main, add_product, show_product, show_json, show_xml, show_json_by_id, show_xml_by_id, register, login_user, logout_user

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-product/', add_product, name='add_product'),
    path('product/<uuid:product_id>/', show_product, name='show_product'),
    path('json/', show_json, name='show_json'),
    path('xml/', show_xml, name='show_xml'),
    path('json/<uuid:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('xml/<uuid:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]