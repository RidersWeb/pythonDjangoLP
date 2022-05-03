from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import CmsSlider

class CmsAdm(admin.ModelAdmin):
    list_display = ('cms_title', 'cms_text', 'cms_css', 'getImage')
    list_display_links = ('cms_title',)
    list_editable = ('cms_css',)
    fields = ('cms_title', 'cms_text', 'cms_css', 'cms_img', 'getImage')
    readonly_fields = ('getImage',)

    def getImage(self, obj):
        if obj.cms_img:
            return mark_safe(f'<img src="{obj.cms_img.url}" width="80px"')
        else:
            return 'НЕТ КАРТИНКИ, ДОБАВТЕ В АДМИНКЕ'

    getImage.short_description = 'Миниатюра'

# Register your models here.
admin.site.register(CmsSlider, CmsAdm)