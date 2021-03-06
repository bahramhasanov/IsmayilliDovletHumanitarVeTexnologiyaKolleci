from django.urls import path
from . import views

urlpatterns = [
    path("news/<slug:slug>", views.SingleNews.as_view(), name="news"),
    path("events/<slug:slug>", views.SingleEvent.as_view(), name="event"),
    path("news/", views.AllNews.as_view(), name="allnews"),
    path("events/", views.EventsView.as_view(), name="allevents"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("about/", views.AboutView.as_view(), name="about"),
    # path("fbk/", views.FBKView.as_view(), name="fbk"),
    path("faculty/", views.AllFaculty.as_view(), name="allfaculty"),
    path("faculty/<slug:slug>", views.SingleFaculty.as_view(), name="faculty"),
    path("faculty/<slug:slug>/speciality/", views.AllSpeciality.as_view(), name="allspeciality"),
    path("faculty/<slug:slug>/speciality/<slug:slug5>", views.SingleSpeciality.as_view(), name="speciality"),
    path("totaladminsion/", views.Totaladmissionrules.as_view(), name="totaladmission"),
    path("from9adminsion/", views.From9admissionrules.as_view(), name="from9admissionrules"),
    path("from11adminsion/", views.From11admissionrules.as_view(), name="from11admissionrules"),
    path("dateofcreate/", views.DateOfCreateView.as_view(), name="dateofcreate"),
    path("practies/", views.AllPractic.as_view(), name="allpractic"),
    path("practies/<slug:slug>", views.SinglePractic.as_view(), name="singlepractic"),
    path('galleries/', views.GalleryView.as_view(), name='galleries'),
    path('faq/', views.FAQView.as_view(), name='faq'),
    path('careersupport/', views.CareerSupportView.as_view(), name='careersupport')
]