from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    full_name=models.CharField(max_length=50, null=True)
    email =models.EmailField(unique=True)
    password=models.CharField(max_length=25)
   
    # return the string representation of the object
    def __str__(self):
        return self.username
    
class Category(models.Model):
    man_shirt = models.CharField(max_length=25)
    dress = models.CharField(max_length=25)
    Man_work_equipment = models.CharField(max_length=25, default='abc')
    woman_bag = models.CharField(max_length=25)  # Consider adding a default value here if appropriate
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    # create choices
    MALE='M'
    FEMALE='F'
    UNISEX='U'
    CATEGORY_CHOICES=(
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('UNISEX', 'Unisex')
    )
    XTRA='X'
    MEDIUM='M'
    LARGE='L'
    XTRA_LARGE='XL'
    XTRA_XTRA_LARGE='XXL'
    SIZE_CHOICES=(
        ('XTRA','Xtra'),
        ('MEDIUM','Medium'),
        ('LARGE','Large'),
        ('XTRA_LARGE','Xtra_large'),
        ('XTRA_XTRA_LARGE','Xtra_xtra_large'),
    )
    product_name=models.CharField(max_length=30)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    quantity=models.IntegerField()
    category = models.CharField(max_length=6, choices=CATEGORY_CHOICES)
    image=models.ImageField(upload_to='product_images/', blank=True, null=True)
    date_added=models.DateTimeField(auto_now_add=True)
    size=models.CharField(max_length=25, choices=SIZE_CHOICES,default=None)

    def __str__(self):
        return self.product_name

class FavouriteProduct(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    date_added=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product

class FlashScale(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    is_discount=models.BooleanField(default=False)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')])

    def __str__(self):
        return self.status
    
class OrderItem(models.Model):
      
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    
    quantity=models.PositiveIntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.order



class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    items=models.ManyToManyField(Product)
    created_at=models.DateTimeField(auto_now_add=True)
    item_quantity=models.PositiveIntegerField(default=1)
    completed = models.BooleanField(default=False)
    session_id = models.CharField(max_length=100, default=1)
    def __str__(self):
        return self.items
    
class Address(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    street=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=50)
    def __str__(self):
        return self.street







