from about.models import News, Category, Specialty, Faculty, Admissionrules, About, Event, Subscriber, Dateofcreate, Practic, PracticPlace, Gallery, CareerSupport
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
admin.site.register([Subscriber,
                    Practic, PracticPlace, Gallery, CareerSupport])


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('title',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    exclude = ('title', 'description',)


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    exclude = ('title', 'description',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    exclude = ('title', 'description',)


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    exclude = ('title', 'description',)
    list_display = (
        'title',
    )
    readonly_fields = ("get_facultyofspecialty",)
    
    # def get_readonly_fields(self, request, obj=None):
    #     if obj:
    #         return self.readonly_fields + ('title',)
    #     return self.readonly_fields

    def get_facultyofspecialty(self, obj):
        name = _("Adları")
        html = f"""
        <table class="table">
                <thead class="thead-dark">
                    <tr>
                    
                    <th scope="col">{name}</th>
                    </tr>
                </thead>
                <tbody>
        """
        for i in obj.specialty_faculty.all():
            html += f'''
                    <tr>
                        <td>{i.title}</td>
                    </tr>
            '''
        return format_html(html + "</tbody></table>")
    get_facultyofspecialty.short_description = _('FBK-da olan ixtisaslar')


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    fields = (
        'description',
        'image',
    )

    def has_add_permission(self, request):
        return True

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
        return True

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
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return True
