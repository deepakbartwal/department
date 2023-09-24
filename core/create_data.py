from collections import OrderedDict

from core.models import Location, Department, ProductCategory, ProductSubcategory, Product

def create_data():
    # ['Location', 'Department', 'Category', 'Subcategory'], [
    data = [['Perimeter', 'Bakery', 'Bakery Bread', 'Bagels'],
            ['Perimeter', 'Bakery', 'Bakery Bread', 'Baking or Breading Products'],
            ['Perimeter', 'Bakery', 'Bakery Bread', 'English Muffins or Biscuits'],
            ['Perimeter', 'Bakery', 'Bakery Bread', 'Flatbreads'],
            ['Perimeter', 'Bakery', 'In Store Bakery', 'Breakfast Cake or Sweet Roll'],
            ['Perimeter', 'Bakery', 'In Store Bakery', 'Cakes'],
            ['Perimeter', 'Bakery', 'In Store Bakery', 'Pies'],
            ['Perimeter', 'Bakery', 'In Store Bakery', 'Seasonal'],
            ['Center', 'Dairy', 'Cheese', 'Cheese Sauce'],
            ['Center', 'Dairy', 'Cheese', 'Specialty Cheese'],
            ['Center', 'Dairy', 'Cream or Creamer', 'Dairy Alternative Creamer'],
            ['Center', 'Dairy', 'Cream or Creamer', 'Whipping Creams'],
            ['Center', 'Dairy', 'Cultured', 'Cottage Cheese'],
            ['Center', 'Dairy', 'Refrigerated Baking', 'Refrigerated Breads'],
            ['Center', 'Dairy', 'Refrigerated Baking', 'Refrigerated English Muffins and Biscuits'],
            ['Center', 'Dairy', 'Refrigerated Baking', 'Refrigerated Hand Held Sweets'],
            ['Center', 'Dairy', 'Refrigerated Baking', 'Refrigerated Pie Crust'],
            ['Center', 'Dairy', 'Refrigerated Baking', 'Refrigerated Sweet Breakfast Baked Goods'],
            ['Perimeter', 'Deli and Foodservice', 'Self Service Deli Cold', 'Beverages'],
            ['Perimeter', 'Deli and Foodservice', 'Service Deli', 'Cheese All Other'],
            ['Perimeter', 'Deli and Foodservice', 'Service Deli', 'Cheese American'],
            ['Perimeter', 'Floral', 'Bouquets and Cut Flowers', 'Bouquets and Cut Flowers'],
            ['Perimeter', 'Floral', 'Gifts', 'Gifts'],
            ['Perimeter', 'Floral', 'Plants', 'Plants'],
            ['Center', 'Frozen', 'Frozen Bake', 'Bread or Dough Products Frozen'],
            ['Center', 'Frozen', 'Frozen Bake', 'Breakfast Cake or Sweet Roll Frozen'],
            ['Center', 'Frozen', 'Frozen Breakfast', 'Frozen Breakfast Entrees'],
            ['Center', 'Frozen', 'Frozen Breakfast', 'Frozen Breakfast Sandwich'],
            ['Center', 'Frozen', 'Frozen Breakfast', 'Frozen Egg Substitutes'],
            ['Center', 'Frozen', 'Frozen Breakfast', 'Frozen Syrup Carriers'],
            ['Center', 'Frozen', 'Frozen Desserts or Fruit and Toppings', 'Pies Frozen'],
            ['Center', 'Frozen', 'Frozen Juice', 'Frozen Apple Juice'],
            ['Center', 'Frozen', 'Frozen Juice', 'Frozen Fruit Drink Mixers'],
            ['Center', 'Frozen', 'Frozen Juice', 'Frozen Fruit Juice All Other'],
            ['Center', 'GM', 'Audio Video', 'Audio'],
            ['Center', 'GM', 'Audio Video', 'Video DVD'],
            ['Center', 'GM', 'Audio Video', 'Video VHS'],
            ['Center', 'GM', 'Housewares', 'Bedding'],
            ['Center', 'GM', 'Housewares', 'Candles'],
            ['Center', 'GM', 'Housewares', 'Collectibles and Gifts'],
            ['Center', 'GM', 'Housewares', 'Flashlights'],
            ['Center', 'GM', 'Housewares', 'Frames'],
            ['Center', 'GM', 'Insect and Rodent', 'Indoor Repellants or Traps'],
            ['Center', 'GM', 'Insect and Rodent', 'Outdoor Repellants or Traps'],
            ['Center', 'GM', 'Kitchen Accessories', 'Kitchen Accessories'],
            ['Center', 'GM', 'Laundry', 'Bleach Liquid'],
            ['Center', 'GM', 'Laundry', 'Bleach Powder'],
            ['Center', 'GM', 'Laundry', 'Fabric Softener Liquid'],
            ['Center', 'GM', 'Laundry', 'Fabric Softener Sheets'],
            ['Center', 'Grocery', 'Baking Ingredients', 'Dry or Canned Milk'],
            ['Center', 'Grocery', 'Baking Ingredients', 'Food Coloring'],
            ['Center', 'Grocery', 'Spices', 'Salt Cooking or Edible or Seasoned'],
            ['Center', 'Grocery', 'Spices', 'Salt Substitute'],
            ['Center', 'Grocery', 'Spices', 'Seasoning Dry'],
            ['Center', 'Grocery', 'Stuffing Products', 'Stuffing Products'],
            ['Perimeter', 'Seafood', 'Frozen Shellfish', 'Frozen Shellfish'],
            ['Perimeter', 'Seafood', 'Other Seafood', 'All Other Seafood'],
            ['Perimeter', 'Seafood', 'Other Seafood', 'Prepared Seafood Entrees'],
            ['Perimeter', 'Seafood', 'Other Seafood', 'Seafood Salads'],
            ['Perimeter', 'Seafood', 'Other Seafood', 'Smoked Fish'],
            ['Perimeter', 'Seafood', 'Other Seafood', 'Seafood Breading Sauces Dips']]

    # Create Location
    locations = [item[0].strip() for item in data]
    locations = list(OrderedDict.fromkeys(locations))
    location_objs = []

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    print(locations)

    for location in locations:
        location_objs.append(Location(name=location))

    Location.objects.bulk_create(location_objs)

    """ Crete Departments """
    departments = [item[1].strip() for item in data]
    departments = list(OrderedDict.fromkeys(departments))
    department_objs = []

    for department in departments:
        department_objs.append(Department(name=department))

    Department.objects.bulk_create(department_objs)

    """ Create product categories"""
    product_categories = [item[2].strip() for item in data]
    product_categories = list(OrderedDict.fromkeys(product_categories))
    product_category_objs = []

    for product_category in product_categories:
        product_category_objs.append(ProductCategory(name=product_category))
    product_category_objs.append(ProductCategory(name='Crackers'))

    ProductCategory.objects.bulk_create(product_category_objs)

    """ Create product sub-categorys"""
    product_sub_categories = [item[3].strip() for item in data]
    product_sub_categories = list(OrderedDict.fromkeys(product_sub_categories))
    product_subcategory_objs = []

    for product_subcategory in product_sub_categories:
        product_subcategory_objs.append(ProductSubcategory(name=product_subcategory))
    product_subcategory_objs.append(ProductSubcategory(name='Rice Cakes'))
    product_subcategory_objs.append(ProductSubcategory(name='Beeding'))
    product_subcategory_objs.append(ProductSubcategory(name='Salads'))
    product_subcategory_objs.append(ProductSubcategory(name='Bagels_duplicate'))
    product_subcategory_objs.append(ProductSubcategory(name='Beverages_duplicate'))
    product_subcategory_objs.append(ProductSubcategory(name='Bouquets and Cut Flowers duplicate'))
    product_subcategory_objs.append(ProductSubcategory(name='All Other duplicate'))
    product_subcategory_objs.append(ProductSubcategory(name='Bread or Dough Products Frozen duplicate'))

    # Extra subcategory
    product_subcategory_objs.append(ProductSubcategory(name='All Other'))

    ProductSubcategory.objects.bulk_create(product_subcategory_objs)

    # ['SKU', 'NAME', 'LOCATION', 'DEPARTMENT', 'CATEGORY', 'SUBCATEGORY'],
    product_data = [['1', 'SKUDESC1', 'Perimeter', 'Bakery', 'Bakery Bread', 'Bagels'],
                    ['2', 'SKUDESC2', 'Perimeter', 'Deli and Foodservice', 'Self Service Deli Cold', 'Beverages'],
                    ['3', 'SKUDESC3', 'Perimeter', 'Floral', 'Bouquets and Cut Flowers', 'Bouquets and Cut Flowers'],
                    ['4', 'SKUDESC4', 'Perimeter', 'Deli and Foodservice', 'Service Deli', 'All Other'],
                    ['5', 'SKUDESC5', 'Center', 'Frozen', 'Frozen Bake', 'Bread or Dough Products Frozen'],
                    ['6', 'SKUDESC6', 'Center', 'Grocery', 'Crackers', 'Rice Cakes'],
                    ['7', 'SKUDESC7', 'Center', 'GM', 'Audio Video', 'Audio'],
                    ['8', 'SKUDESC8', 'Center', 'GM', 'Audio Video', 'Video DVD'],
                    ['9', 'SKUDESC9', 'Perimeter', 'GM', 'Housewares', 'Beeding'],
                    ['10', 'SKUDESC10', 'Perimeter', 'Seafood', 'Frozen Shellfish', 'Frozen Shellfish'],
                    ['11', 'SKUDESC11', 'Perimeter', 'Seafood', 'Other Seafood', 'All Other Seafood'],
                    ['12', 'SKUDESC12', 'Perimeter', 'Seafood', 'Other Seafood', 'Prepared Seafood Entrees'],
                    ['13', 'SKUDESC13', 'Perimeter', 'Seafood', 'Other Seafood', 'Salads'],
                    ['14', 'SKUDESC14', 'Perimeter', 'Bakery', 'Bakery Bread', 'Bagels_duplicate'],
                    ['15', 'SKUDESC15', 'Perimeter', 'Deli and Foodservice', 'Self Service Deli Cold', 'Beverages_duplicate'],
                    ['16', 'SKUDESC16', 'Perimeter', 'Floral', 'Bouquets and Cut Flowers', 'Bouquets and Cut Flowers duplicate'],
                    ['17', 'SKUDESC17', 'Perimeter', 'Deli and Foodservice', 'Service Deli', 'All Other duplicate'],
                    ['18', ' SKUDESC18', ' Center', ' Frozen', ' Frozen Bake', 'Bread or Dough Products Frozen duplicate']]


    """ Crete Departments """

    for prod_data in product_data:
        print(prod_data)
        try:
            Product.objects.create(
                id=int(prod_data[0].strip()),
                skuid=prod_data[1].strip(),
                name=prod_data[5].strip(),
                location=Location.objects.get(name=prod_data[2].strip()),
                department=Department.objects.get(name=prod_data[3].strip()),
                product_category=ProductCategory.objects.get(name=prod_data[4].strip()),
                product_subcategory=ProductSubcategory.objects.get(name=prod_data[5].strip())
            )
        except Location.DoesNotExist:
            import pdb; pdb.set_trace()
        # except Department.DoesNotExist:
        #     import pdb; pdb.set_trace()
        # except ProductCategory.DoesNotExist:
        #     import pdb; pdb.set_trace()
        # except ProductSubcategory.DoesNotExist:
        #     import pdb; pdb.set_trace()