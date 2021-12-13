from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from django.utils.translation import check_for_language

from about.models import News, Category, Specialty, Faculty, Admissionrules, About, Dateofcreate

admin.site.register([News, Category, Specialty])

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_display = (
        'title', 
 
        )
    readonly_fields = ("get_facultyofspecialty",)
    fields = (
        'title', 
        'description',
        'image',
        'get_facultyofspecialty'
        )

    # def get_readonly_fields(self, request, obj=None):
    #     if obj:                      
    #         return self.readonly_fields + ('title',)
    #     return self.readonly_fields
    
    
    def get_facultyofspecialty(self, obj):
        html = """
        <table class="table">
                <thead class="thead-dark">
                    <tr>
                    
                    <th scope="col">adları</th>
                    </tr>
                </thead>
                <tbody>
        """
        for i in obj.specialty_faculty.all():
            html +=f'''
                    <tr>
                        <td>{i.title}</td>
                    </tr>
            '''
        return format_html(html + "</tbody></table>")
    get_facultyofspecialty.short_description = 'FBK-da olan ixtisaslar'

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    fields = (
        'description',
        'image',
        )
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return True


@admin.register(Admissionrules)
class AdmissionrulesAdmin(admin.ModelAdmin):
    fields = (
        'total_rules',
        'from_9_rules',
        'from_11_rules',
        )
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return True
    
    
@admin.register(Dateofcreate)
class DateofcreateAdmin(admin.ModelAdmin):
    fields = (
        'description',
        )
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return True
    