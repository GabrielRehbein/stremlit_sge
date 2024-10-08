from services.brand_service import BrandService
from services.category_service import CategoryService
from services.inflow_service import InflowService
from services.outflow_service import OutflowService
from services.product_service import ProductService
from services.supplier_service import SupplierService
import streamlit as st

brand_client = BrandService()
st.title("Sistema Gestão de Estoque")

# Seção para criar nova marca
st.header("Adicionar Nova Marca")
name = st.text_input("Nome da Marca")
description = st.text_input("Descrição")
if st.button("Adicionar"):
    if name:
        data: dict = {
            'name': name,
            'description': description
        }
        brand_client.create_brand(data=data)
        st.success(f"Marca '{name}' adicionada com sucesso!")
    else:
        st.error("O nome da marca não pode estar vazio")

# Seção para listar marcas
st.header("Marcas Cadastradas")
brands = brand_client.get_all_brands()
brand_results = brands.get('results')

for brand in brand_results:
   st.write(f"ID: {brand.get('id')} | Nome: {brand.get('name')} | Descrição: {brand.get('description')}")


# Seção para atualizar uma marca
st.header("Atualizar Marca")
brand_id = st.number_input("ID da Marca a ser atualizada", min_value=1)
new_name = st.text_input("Novo Nome da Marca")
if st.button("Atualizar"):
    if new_name:
        data: dict = {
            'name': new_name,
        }
        updated_brand = brand_client.update_brand(id=brand_id, data=data)
        if updated_brand:
            st.success(f"Marca atualizada para '{new_name}'")
        else:
            st.error("Marca não encontrada")
    else:
        st.error("O novo nome não pode estar vazio")

# Seção para deletar uma marca
st.header("Deletar Marca")
delete_id = st.number_input("ID da Marca a ser deletada", min_value=1, key='delete')
if st.button("Deletar"):
    brand_client.delete_brand(delete_id)
    st.success(f"Marca com ID '{delete_id}' deletada com sucesso")
