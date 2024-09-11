from django.contrib import admin

from .forms import BinPackingDemoForm
from .models import BinPackingDemo


class BinPackingDemoAdmin(admin.ModelAdmin):
    form = BinPackingDemoForm
    list_display = ('algorithm', 'bin_capacity', 'item_list')
    search_fields = ('algorithm',)
    list_filter = ('algorithm',)


admin.site.register(BinPackingDemo, BinPackingDemoAdmin)
# Register your models here.
