from django.urls import path

from . import views

app_name = "zapis"

urlpatterns = [
    path("list/", views.zapis_by_tag, name="list"),
    path("list/tag/<slug:tag_slug>", views.zapis_by_tag, name="list_by_tag"),
    path("create/", views.ZapisCreateView.as_view(), name="create"),
    path("add-zapis/", views.add_zapis, name="api-add-zapis"),
    path("complete/<int:uid>", views.complete_zapis, name="complete"),
    path("delete/<int:uid>", views.delete_zapis, name="delete"),
    path("details/<int:pk>", views.ZapisDetailsView.as_view(), name="details"),
    path("edit/<int:pk>", views.ZapisEditView.as_view(), name="edit"),
    path("export/", views.ZapisExportView.as_view(), name="export"),
]
