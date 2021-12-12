from django.contrib import admin
# Register your models here.
from django.utils.html import format_html

from staff.models import Teacher, Subject, PDF

admin.site.register([Teacher, PDF])

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_display = (
        'title', 
 
        )
    readonly_fields = ("get_subjectofteacher",)
    fields = (
        'title', 
        'get_subjectofteacher'
        )

    def get_subjectofteacher(self, obj):
        html = """
        <table class="table">
                <thead class="thead-dark">
                    <tr>
                    <th scope="col">adları</th>
                    </tr>
                </thead>
                <tbody>
        """
        for i in obj.subject_teachers.all():
            html +=f'''
                    <tr>
                        <td>{i.full_name}</td>
                    </tr>
            '''
        return format_html(html + "</tbody></table>")
    get_subjectofteacher.short_description = 'FBK-dakı ixtisaslar'

