from django.urls import path
from . import views

urlpatterns = [
    path("news/<int:pk>", views.SingleNews.as_view(), name="news"),
    path("news/", views.AllNews.as_view(), name="allnews"),
    path("contact/", views.Contact.as_view(), name="contact"),
    path("about/", views.About.as_view(), name="about"),
    path("fbk/", views.FBK.as_view(), name="fbk"),
    path("faculty/", views.AllFaculty.as_view(), name="allfaculty"),
    path("faculty/<int:pk>", views.SingleFaculty.as_view(), name="faculty"),
    path("faculty/<int:pk>/speciality/", views.AllSpeciality.as_view(), name="allspeciality"),
    path("faculty/<int:pk>/speciality/<int:pk2>", views.SingleSpeciality.as_view(), name="speciality"),
    path("totaladminsion/", views.Totaladmissionrules.as_view(), name="totaladmission"),
    path("from9adminsion/", views.From9admissionrules.as_view(), name="from9admissionrules"),
    path("from11adminsion/", views.From11admissionrules.as_view(), name="from11admissionrules"),
]
