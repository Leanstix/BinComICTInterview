from django.urls import path
from . import views

urlpatterns = [
    path('polling_unit/<int:uniqueid>/', views.polling_unit_result, name='polling_unit_result'),
    path('lga_results/', views.lga_results, name='lga_results'),
    path('add_polling_unit/', views.add_polling_unit_result, name='add_polling_unit_result'),
]