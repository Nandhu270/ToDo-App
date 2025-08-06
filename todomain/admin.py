from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('user','content','is_completed','updated_at')
    search_fields = ('user__username','content')
    list_filter = ('is_completed',)
    list_per_page = 15
    

admin.site.register(Todo, TodoAdmin)