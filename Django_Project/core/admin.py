from django.contrib import admin
from core.models import Category, Product

# Register your models here.
# admin.site.register([Category, Product])

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "quantity", "get_total_price", "available", "category", "views")
    list_display_links = ("name",)
    # list_filter = ("price", "quantity", "available", "category")
    # list_per_page = 3
    list_editable = ("price", "quantity")
    search_fields = ("name",)
    actions = ("change_available_false", "change_available_true")
    readonly_fields = ("created_at", "updated_at", "views")

    @admin.action(description="Make Not Available")
    def change_available_false(self, request, queryset):
        queryset.update(available=False)

    @admin.action(description="Make Available")
    def change_available_true(self, request, queryset):
        queryset.update(available=True)

    @admin.display(description="Total Price")
    def get_total_price(self, obj):
        return obj.price * obj.quantity