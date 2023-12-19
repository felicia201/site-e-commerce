from django.db import models
from shop.settings import AUTH_USER_MODEL
from django.utils  import timezone


# Create your models here.
"""
Product
-Nom (text)
-Prix(int,float)
-La quantité en stock(nombre entier)
-Description(chaine caratere)
-Images

"""
class Product(models.Model):
    name= models.CharField(max_length=128)
    slug= models.SlugField(max_length=128) # caratere
    price=models.FloatField(default=0.0)
    stock= models.IntegerField(default=0)
    description=models.TextField(blank=True)
    thumbnail=models.ImageField(upload_to="products",blank=True,null=True)

    def __str__(self):
        return self.name
    
    # article(order)
    """
    -utilisateur
    -produit
    -quantité (booléen)
    -commendé ou nom
    """
class Order(models.Model):
    user= models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True,null=True)


    def __str__(self):
        return f"{self.product.name} ({self.quantity})"



    #panier(Cart)
    """
    -utilisateur
    -Articles
    -Commandé ou nom
    -Date de la commande
    """

class Cart(models.Model):
        user= models.OneToOneField(AUTH_USER_MODEL,on_delete=models.CASCADE)
        orders= models.ManyToManyField(Order)
      

        def __str__(self) :
             return self.user.username
        
        def delete(self,*args,**Kwargs):
             for order in self.orders.all():
                  order.ordered= True
                  order.ordered_date = timezone.now() # utc: temps universel
                  order.save()

             self.orders.clear()   
             super().delete(*args,**Kwargs)

