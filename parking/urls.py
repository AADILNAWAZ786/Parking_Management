from django.urls import path

# Register your models here
from . import views
urlpatterns = [
    path('',views.login_view, name='login'),
    path('category/',views.Test_case3,name='category'),
    path('add_category',views.Test_case3_1,name='add_category'),
    path('delete/<int:id>/', views.Test_case3_2, name='delete'),
    path('vehicle_entry/',views.Test_case4,name='vehicle_entry'),
    path('add_vehicle/',views.Test_case4_1,name='add_vehicle'),
    path('Manage_Vehicles/',views.Test_case5,name='Manage_Vehicles'),
    path('action/<int:id>/',views.vehicle_entry_status,name='action'),
    path('Search/',views.Test_case6,name='Search'),
    path('Accounts/',views.accountSetting,name='Accounts'),
    path('dashboard',views.dashboard, name="dashboard"),
    path('logout',views.logouts,name='logout'),
    path('edit/',views.edit,name='edit'),
]    