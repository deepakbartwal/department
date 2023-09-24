from rest_framework import serializers
from core.models import Location, Department, Product, ProductCategory, ProductSubcategory


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSubcategory
        fields = '__all__'


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    location_name = serializers.CharField(source='location.name', read_only=True)
    department_name = serializers.CharField(source='department.name', read_only=True)
    product_category_name = serializers.CharField(source='product_category.name', read_only=True)
    product_subcategory_name = serializers.CharField(source='product_subcategory.name', read_only=True)

    class Meta:
        model = Product
        fields = (
            'id', 'skuid', 'location_id', 'location_name', 'department_id', 'department_name', 'product_category_id',
            'product_category_name', 'product_subcategory_id', 'product_subcategory_name')


class DepartmentByLocationSerializer(serializers.ModelSerializer):
    location_name = serializers.CharField(source='location.name', read_only=True)
    department_name = serializers.CharField(source='department.name', read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'location_id', 'location_name', 'department_id', 'department_name')


class CatogoryByDepartmentAndLocationSerializer(serializers.ModelSerializer):
    location_name = serializers.CharField(source='location.name', read_only=True)
    department_name = serializers.CharField(source='department.name', read_only=True)
    product_category_name = serializers.CharField(source='product_category.name', read_only=True)

    class Meta:
        model = Product
        fields = (
            'id', 'location_id', 'location_name', 'department_id', 'department_name', 'product_category_id',
            'product_category_name')


class SubcategoryByCategoryAndDepartmentAndLocationSerializer(serializers.ModelSerializer):
    location_name = serializers.CharField(source='location.name', read_only=True)
    department_name = serializers.CharField(source='department.name', read_only=True)
    product_category_name = serializers.CharField(source='product_category.name', read_only=True)
    product_subcategory_name = serializers.CharField(source='product_subcategory.name', read_only=True)

    class Meta:
        model = Product
        fields = (
            'id', 'location_id', 'location_name', 'department_id', 'department_name', 'product_category_id',
            'product_category_name', 'product_subcategory_id', 'product_subcategory_name')


class ProductBySubcategoryAndCategoryAndDepartmentAndLocationSerializer(serializers.ModelSerializer):
    location_name = serializers.CharField(source='location.name', read_only=True)
    department_name = serializers.CharField(source='department.name', read_only=True)
    product_category_name = serializers.CharField(source='product_category.name', read_only=True)
    product_subcategory_name = serializers.CharField(source='product_subcategory.name', read_only=True)

    class Meta:
        model = Product
        fields = (
            'id', 'skuid', 'location_id', 'location_name', 'department_id', 'department_name', 'product_category_id',
            'product_category_name', 'product_subcategory_id', 'product_subcategory_name')
