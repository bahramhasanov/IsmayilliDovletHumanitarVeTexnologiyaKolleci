from django.urls import path
from . import views

urlpatterns = [
    path("news/<int:pk>", views.SingleNews.as_view(), name="news"),
    path("news/", views.AllNews.as_view(), name="allnews"),
    path("events/", views.EventsView.as_view(), name="allevents"),
    path("contact/", views.Contact.as_view(), name="contact"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("fbk/", views.FBK.as_view(), name="fbk"),
    path("faculty/", views.AllFaculty.as_view(), name="allfaculty"),
    path("faculty/<int:pk>", views.SingleFaculty.as_view(), name="faculty"),
    path("faculty/<int:pk>/speciality/", views.AllSpeciality.as_view(), name="allspeciality"),
    path("faculty/<int:pk>/speciality/<int:pk2>", views.SingleSpeciality.as_view(), name="speciality"),
    path("totaladminsion/", views.Totaladmissionrules.as_view(), name="totaladmission"),
    path("from9adminsion/", views.From9admissionrules.as_view(), name="from9admissionrules"),
    path("from11adminsion/", views.From11admissionrules.as_view(), name="from11admissionrules"),
    path("dateofcreate/", views.DateofcreateView.as_view(), name="dateofcreate"),
    path("practies/", views.AllPractic.as_view(), name="allpractic"),
    path("practies/<int:pk>", views.SinglePractic.as_view(), name="singlepractic"),
    path('galleries/', views.GalleryView.as_view(), name='galleries'),
    path('faq/', views.FAQView.as_view(), name='faq'),
]
