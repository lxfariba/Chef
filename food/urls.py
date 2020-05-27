from django.conf.urls import url
from . import views
from Chef.views import cart


urlpatterns = [
    url(r'^menu_food/$', views.menu_food_view, name='menu_food'),
    url(r'^detail/(?P<slug>[-\w]+)-(?P<rid>\w+)$', views.detail_food_view, name='detail'),
    url(r'^add/cart/$', cart.add_to_cart_view, name='add_to_cart'),
    url(r'^cart/$', cart.cart_view, name='cart'),
    url(r'cart/delete/$', cart.cart_item_delete_view, name='delete_item'),
    url(r'^cart/checkout/$', cart.checkout_view, name='checkout')

]