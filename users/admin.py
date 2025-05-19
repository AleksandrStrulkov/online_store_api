from django.contrib import admin
from users.models import User


# Register your models here.
@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('last_name',
                    'first_name',
                    'email',
                    'phone',
                    'is_activated',
                    # 'is_staff'
                    # 'is_active'
                    'date_joined'
                    )
    list_filter = ('email',)
    search_fields = ('email',)
