
from django.contrib import admin
from django.urls import path
from store.views import index,product_detail,add_to_cart,cart,delete_cart
from django.conf.urls.static import static
from shop import settings
from accounts.views import signup,logout_user,login_user

# chemin url

urlpatterns = [
    path('',index,name='index'),
    path('admin/', admin.site.urls),
    path('signup/', logout_user, name="logout"),
    path('logout/', signup, name="signup"),
    path('login/', login_user, name="login"),
    path('cart/', cart, name="cart"),
    path('cart/delete/', delete_cart, name="delete_cart"),
    path('product/<str:slug>/', product_detail,name="product"),
    path('product/<str:slug>/add-to-cart', add_to_cart,name="add-to-cart"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

