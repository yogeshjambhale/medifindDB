from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser






class Products(models.Model):
    product_name= models.CharField(max_length=100, blank = True, null = True)
    drug_name= models.CharField(max_length=100, blank = True, null = True)
    company= models.CharField(max_length=100, blank = True, null = True)
    manufacturer=models.CharField(max_length=100, blank = True, null = True)
    mrp= models.CharField(max_length=20, blank = True, null = True)
    discount= models.CharField(max_length=20, blank = True, null = True)
    image = models.CharField(max_length=200, blank = True, null = True)
    qty= models.CharField(max_length=20, blank = True, null = True)
    soldQty= models.CharField(max_length=20, blank = True, null = True)
    avlQty= models.CharField(max_length=20, blank = True, null = True)

    def _str_(self):
        return self.product_name
        

class CartData(models.Model):
    product_name= models.CharField(max_length=100, blank = True, null = True)
    drug_name= models.CharField(max_length=100, blank = True, null = True)
    company= models.CharField(max_length=100, blank = True, null = True)
    manufacturer=models.CharField(max_length=100, blank = True, null = True)
    mrp= models.CharField(max_length=20, blank = True, null = True)
    discount= models.CharField(max_length=20, blank = True, null = True)
    image = models.CharField(max_length=200, blank = True, null = True)
    qty= models.CharField(max_length=20, blank = True, null = True)
    soldQty= models.CharField(max_length=20, blank = True, null = True)
    avlQty= models.CharField(max_length=20, blank = True, null = True)
    quantity= models.CharField(max_length=20, blank = True, null = True)
    userId= models.IntegerField( blank = True, null = True)
    productId= models.IntegerField( blank = True, null = True)

    def _str_(self):
        return self.product_name

class UserSignup(models.Model):   
    name= models.CharField(max_length=100, blank = True, null = True)
    email= models.EmailField()
    quetion= models.CharField(max_length=100, blank = True, null = True)
    password=models.CharField(max_length=100, blank = True, null = True)

    def _str_(self):
        return self.name

class AdminSignup(models.Model):   
    name= models.CharField(max_length=100, blank = True, null = True)
    email= models.EmailField()
    quetion= models.CharField(max_length=100, blank = True, null = True)
    password=models.CharField(max_length=100, blank = True, null = True)

    def _str_(self):
        return self.name

class Address(models.Model):   
    name= models.CharField(max_length=100, blank = True, null = True)
    address= models.CharField(max_length=100, blank = True, null = True)
    state=models.CharField(max_length=100, blank = True, null = True)
    city= models.CharField(max_length=100, blank = True, null = True)
    pincode=models.CharField(max_length=100, blank = True, null = True)
    mobile= models.CharField(max_length=100, blank = True, null = True)
    userId=models.IntegerField( blank = True, null = True)

    def _str_(self):
        return self.name
    
class Orders(models.Model):
    product_name= models.CharField(max_length=100, blank = True, null = True)
    drug_name= models.CharField(max_length=100, blank = True, null = True)
    company= models.CharField(max_length=100, blank = True, null = True)
    manufacturer=models.CharField(max_length=100, blank = True, null = True)
    mrp= models.CharField(max_length=20, blank = True, null = True)
    discount= models.CharField(max_length=20, blank = True, null = True)
    image = models.CharField(max_length=200, blank = True, null = True)
    qty= models.CharField(max_length=20, blank = True, null = True)
    quantity= models.CharField(max_length=20, blank = True, null = True)
    userId= models.IntegerField( blank = True, null = True)
    productId= models.IntegerField( blank = True, null = True)

    def _str_(self):
        return self.product_name

class hotel(models.Model):
    hotel_name= models.CharField(max_length=250, blank = True, null = True)
    staytypes= models.CharField(max_length=250, blank = True, null = True)
    aminities= models.CharField(max_length=250, blank = True, null = True)
    description=models.CharField(max_length=250, blank = True, null = True)
    address= models.CharField(max_length=200, blank = True, null = True)
    images= models.CharField(max_length=300, blank = True, null = True)

    def _str_(self):
        return self.hotel_name

class rooms(models.Model):
    hotel= models.ForeignKey('medifindapp.hotel', on_delete=models.CASCADE, related_name='room')
    bedtypes= models.CharField(max_length=250, blank = True, null = True)
    roomtypes= models.CharField(max_length=250, blank = True, null = True)
    aminities= models.CharField(max_length=250, blank = True, null = True)
    totalbeds=models.CharField(max_length=250, blank = True, null = True)
    price= models.CharField(max_length=20, blank = True, null = True)
    images= models.CharField(max_length=300, blank = True, null = True)

    def _str_(self):
        return self.roomtypes
# custom user manager

class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, password2=None):
        """
        Creates and saves a User with the given email, name and password.
        """
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, password2=None):
        """
        Creates and saves a superuser with the given email, name and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# custom user model

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email ',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



