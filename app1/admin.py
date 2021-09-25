from django.contrib import admin
from.models import Post,employee,salary,novel,author,Member,club
class Postadmin(admin.ModelAdmin):
    fields=['name','created_date','student_updated','new_content','email','Profile_pic','Resume','adress','comment','rating',]
    readonly_fields=['created_date','student_updated','new_content']
    def new_content(self,obj,*args,**kwargs):
        return str(obj.name)
    class Meta:
        model=Post
admin.site.register(Post,Postadmin)
admin.site.register(employee)
admin.site.register(salary)
admin.site.register(novel)
admin.site.register(author)
admin.site.register(Member)
admin.site.register(club)



# Register your models here.
