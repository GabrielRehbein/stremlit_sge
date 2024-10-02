from services import category_service, category_service
from services.brand_service import BrandService
from utils.urls import UrlManager


# client_category = category_service.CategoryService()
# print(client_category.get_all_categories())


# product_client = product_service.ProductService()

# print(product_service.get_url('products', id=2))



# print(product_client.get_product(2))
# print()
# print(product_client.get_all_products())

#TODO SEGUIR NO FORMATO DE BRAND TODOS OS OUTROS SERVICES
brand_client = BrandService()
print(brand_client.get_all_brands())
print()
print(brand_client.get_brand(11))
print()
data={'description': 'cb'}
print(brand_client.update_brand(id=11, data=data))
print(brand_client.get_brand(11))
