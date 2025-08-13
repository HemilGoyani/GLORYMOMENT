from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Product

from django.contrib.auth.models import Group, User

# Unregister built-in models
admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.site_header = "Glory Moment"
admin.site.site_title = "GloryMoment Admin"
admin.site.index_title = "Manage Products & More"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'active', 'image_tag', 'action_buttons')
    list_filter = ('category', 'active')
    search_fields = ('name',)
    list_per_page = 10

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" style="object-fit: cover; border-radius: 5px;" />', obj.image.url)
        return "No Image"
    image_tag.short_description = 'Image'

    def action_buttons(self, obj):  # ✅ renamed from "actions"
        edit_url = reverse('admin:products_product_change', args=[obj.pk])
        delete_url = reverse('admin:products_product_delete', args=[obj.pk])
        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" style="color:red;" href="{}">Delete</a>',
            edit_url, delete_url
        )
    action_buttons.short_description = 'Actions'
    action_buttons.allow_tags = True