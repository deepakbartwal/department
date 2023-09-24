from django.urls import path
from . import views

urlpatterns = [
    path('location/', views.LocationViewSet.as_view({'get': 'list'})),
    path('location/<int:location_id>/department/', views.DepartmentByLocationViewSet.as_view({'get': 'list'}),
         name='location_details'),
    path('location/<int:location_id>/department/<int:department_id>/category/',
         views.CategoryByDepartmentAndLocationViewSet.as_view({'get': 'list'}),
         name='location_details'),
    path('location/<int:location_id>/department/<int:department_id>/category/<int:category_id>/subcategory/',
         views.SubcategoryByCategoryAndDepartmentAndLocationViewSet.as_view({'get': 'list'}),
         name='location_details'),
    path(
        'location/<int:location_id>/department/<int:department_id>/category/<int:category_id>/subcategory/'
        '<int:subcategory_id>/',
        views.ProductBySubcategoryAndCategoryAndDepartmentAndLocationViewSet.as_view({'get': 'list'}),
        name='location_details'),
    path('department/', views.DepartmentViewSet.as_view({'get': 'list'})),
    path('location/', views.LocationViewSet.as_view({'get': 'list'})),
    path('product/', views.ProductViewSet.as_view({'post': 'list'})),
]
