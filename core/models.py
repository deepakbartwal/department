from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Location(models.Model):
    name = models.CharField(max_length=50, unique=True)


class ProductCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)


class ProductSubcategory(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Product(models.Model):
    skuid = models.CharField(max_length=16, unique=True)
    name = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_subcategory = models.ForeignKey(ProductSubcategory, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'location', 'department', 'product_category', 'product_subcategory'],
                name='unique product')
        ]
