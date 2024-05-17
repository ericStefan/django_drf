
from django.urls import path
from course import views

urlpatterns = [
    path("fbv/list/",views.course_list, name='fbv-list'),
    path("fbv/detail/<int:pk>/", views.course_detail, name="fbv-detail"),

    # Class Based View
    path("cbv/list/", views.CourseList.as_view(), name="cbv-list"),
    path("cbv/dtail/<int:pk>/",views.CourseDetail.as_view(), name="cbv-detail")
]