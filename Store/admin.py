from django.contrib import admin
from .models import Category,Product, OrderItem, Order

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(Category,CategoryAdmin )

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20

admin.site.register(Product, ProductAdmin)

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    fieldsets = [
        ('Product',{'fields': ['product'],}),
        ('Quantity', {'fields': ['quantity'], }),
        ('Price', {'fields': ['price'], }),
    ]
    readonly_fields = ['product', 'quantity', 'price']
    can_delete = False
    max_num = 0
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'billingName', 'email', 'created']
    list_display_links = ('id', 'billingName')
    search_fields = ['id', 'email', 'billingName']
    readonly_fields = ['id', 'token', 'total', 'email', 'created','billingName', 'billingAddress1', 'billingCity', 'billingPostCode' , 'billingCountry', 'shippingName','shippingAddress1', 'shippingCity', 'shippingPostcode', 'shippingCountry']
    fieldsets = [
        ('ORDER INFORMATION', {'fields': ['id', 'token', 'total', 'created']}),
        ('Billing INFORMATION', {'fields': ['billingName', 'billingAddress1', 'billingCity', 'billingPostCode','billingCountry', 'email']}),
        ('Shipping INFORMATION', {'fields': [ 'shippingName','shippingAddress1', 'shippingCity', 'shippingPostcode', 'shippingCountry' ]}),
    ]

    inlines = [OrderItemAdmin]
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False






