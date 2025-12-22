from django.contrib import admin
from .models import Task,Person
# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    #Pour personnaliser l'affichage de formulaire
    fieldsets=(
        (None,{
            "fields":("title","description","assigned_to")

        }),
        ("Status Information",{
            "fields":("status","due_date"),
            "classes":("collapse",)

        }),
    )
    list_display=('title', 'assigned_to',
                  'due_date','status')
    @admin.display(boolean=True, 
                   description='Overdue?')
    def is_overdue(self,obj):
        from django.utils import timezone
        if obj.due_date:
            return obj.due_date <timezone.now().date() and obj.status != 'DONE'
            return False
        
    list_filter=('status','due_date')
    search_fields=('title','description')
    ordering=('-due_date',)

    def set_status_done(self, request,queryset):
        queryset.update(status='DONE')
        self.message_user(request,"Selected tasks have been marked as Done.")
        
    set_status_done.short_description="Mark Selected tasks  as Done. "
    actions=[set_status_done]


# admin.site.register(Task, TaskAdmin)


#si je veux personaliser l'affichage , je crée la classe suivante puis faire l'appel dans admin.ite.register:
class PersonAdmin(admin.ModelAdmin):
    list_display=('username','email','first_name','last_name','task_count')
    search_fields=('username','email')

    @admin.display(description='Tasks Assigned')
    def task_count(self,obj):
        return obj.tasks.count()

admin.site.register(Person,PersonAdmin)

