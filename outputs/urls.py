from django.urls import path
from outputs.views import OutputsView, OutputsListView, SelectCategoryView


urlpatterns = [
    path('', OutputsView.as_view(), name='outputs_info'),
    path('list/', OutputsListView.as_view(), name='output_list'),
    path('crate_template/', SelectCategoryView.as_view(), name='outputsCreateTemplateView'),

]
