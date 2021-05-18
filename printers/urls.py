from django.urls import path

from . import views


urlpatterns = [
    # принтеры
    path("info/", views.PrinterInfoView.as_view(), name="printer_info"),
    path("create/", views.PrinterCreateView.as_view(), name="printer_create"),
    path("list/", views.PrinterListView.as_view(), name="printer_list"),
    path("detail/<int:pk>/", views.PrinterDetailView.as_view(), name="printer_detail"),
    path("update/<int:pk>/", views.PrinterUpdateView.as_view(), name="printer_update"),
    path("delete/<int:pk>/", views.PrinterDeleteView.as_view(), name="printer_delete"),
    path("analytics/", views.PrinterAnalyticsListView.as_view(), name="printer_analytics_list"),
    path("analytics/update/<int:pk>/", views.PrinterAnalyticsUpdateView.as_view(), name="printer_analytics_update"),

    # autocomplete для картриджей
    path("black-cartridges-autocomplete/",
         views.BlackCartridgesAutocomplete.as_view(), name="black-cartridges-autocomplete"),
    path("blue-cartridges-autocomplete/",
         views.BlueCartridgesAutocomplete.as_view(), name="blue-cartridges-autocomplete"),
    path("yellow-cartridges-autocomplete/",
         views.YellowCartridgesAutocomplete.as_view(), name="yellow-cartridges-autocomplete"),
    path("purple-cartridges-autocomplete/",
         views.PurpleCartridgesAutocomplete.as_view(), name="purple-cartridges-autocomplete")
]

