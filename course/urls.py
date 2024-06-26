
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from course import views

# DRF viewsets的第二种路由方式
router = DefaultRouter()
router.register(prefix="viewsets", viewset=views.CourseViewSet)

urlpatterns = [
    # Function Based View
    path("fbv/list/",views.course_list, name='fbv-list'),
    path("fbv/detail/<int:pk>/", views.course_detail, name="fbv-detail"),

    # Class Based View
    path("cbv/list/", views.CourseList.as_view(), name="cbv-list"),
    path("cbv/detail/<int:pk>/",views.CourseDetail.as_view(), name="cbv-detail"),

    # Generic Class Based View
    path("gcbv/list/", views.GCourseList.as_view(), name="gcbv-list"),
    path("gcbv/detail/<int:pk>/", views.GCourseDetail.as_view(), name="gcbv-detail"),

    # DRF viewssets
    path("viewsets/", views.CourseViewSet.as_view({
        "get": "list", "post": "create"
    }), name="viewsets-list"),
    path("viewsets/<int:pk>/", views.CourseViewSet.as_view({
        "get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"
    }), name="viewsets-detail"),

    # DRF viewsets的第二种路由方式
    path("", include(router.urls))
]