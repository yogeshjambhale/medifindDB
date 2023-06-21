from django.contrib import admin
from medifindapp.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from medifindapp.models import Products
from medifindapp.models import CartData,hotel,rooms



# Register your models here.

admin.site.register(Products)
admin.site.register(CartData)

@admin.register(hotel)
class hotelAdmin(admin.ModelAdmin):
    list_display = ('id','hotel_name','address')

@admin.register(rooms)
class roomsAdmin(admin.ModelAdmin):
    list_display = ('id','roomtypes','aminities','price')
# Register your models here.
class UserModelAdmin(BaseUserAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id','email', 'name', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email','id')
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserModelAdmin)
