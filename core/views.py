from core.models import Location, Department, Product
from core.serializers import LocationSerializer, DepartmentSerializer, DepartmentByLocationSerializer, \
    CatogoryByDepartmentAndLocationSerializer, SubcategoryByCategoryAndDepartmentAndLocationSerializer, \
    ProductBySubcategoryAndCategoryAndDepartmentAndLocationSerializer, ProductSerializer

from rest_framework import viewsets


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('id')
    serializer_class = LocationSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all().order_by('id')
    serializer_class = DepartmentSerializer


class DepartmentByLocationViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentByLocationSerializer

    def get_queryset(self):
        return Product.objects.filter(location=self.kwargs['location_id']).order_by('id')


class CategoryByDepartmentAndLocationViewSet(viewsets.ModelViewSet):
    serializer_class = CatogoryByDepartmentAndLocationSerializer

    def get_queryset(self):
        return Product.objects.filter(location=self.kwargs['location_id'],
                                      department=self.kwargs['department_id']).order_by('id')


class SubcategoryByCategoryAndDepartmentAndLocationViewSet(viewsets.ModelViewSet):
    serializer_class = SubcategoryByCategoryAndDepartmentAndLocationSerializer

    def get_queryset(self):
        return Product.objects.filter(location_id=self.kwargs['location_id'],
                                      department_id=self.kwargs['department_id'],
                                      product_category_id=self.kwargs['category_id']).order_by('id')


class ProductBySubcategoryAndCategoryAndDepartmentAndLocationViewSet(viewsets.ModelViewSet):
    serializer_class = ProductBySubcategoryAndCategoryAndDepartmentAndLocationSerializer

    def get_queryset(self):
        return Product.objects.filter(location_id=self.kwargs['location_id'],
                                      department_id=self.kwargs['department_id'],
                                      product_category_id=self.kwargs['category_id'],
                                      product_subcategory_id=self.kwargs['subcategory_id']).order_by('id')


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('id')
    serializer_class = LocationSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all().order_by('id')
        if self.request.data.get('location_id'):
            queryset = queryset.filter(location_id=self.request.data['department_id'])
        if self.request.data.get('department_id'):
            queryset = queryset.filter(department_id=self.request.data['department_id'])
        if self.request.data.get('category_id'):
            queryset = queryset.filter(product_category_id=self.request.data['category_id'])
        if self.request.data.get('subcategory_id'):
            queryset = queryset.filter(product_subcategory_id=self.request.data['subcategory_id'])
        return queryset
