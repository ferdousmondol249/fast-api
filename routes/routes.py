from fastapi import APIRouter
from model.product import product
from controller.productController import create_product, get_all_products, delete_product, update_product
from model.product import ProductUpdate
from model.information import person
from controller.informationController import create_person
from fastapi import Form, UploadFile, File
from model.register import register_model
from controller.registerController import registration_user
from controller.loginController import login_user


router=APIRouter()

@router.post('/add-product')

async def add_product(product:product):
    return await create_product(product)

@router.get('/all-product')
async def get_product():
    return await get_all_products()


@router.delete('/delete/{product_id}')
async def del_product(product_id: str):
    return await delete_product(product_id)


@router.patch('/update-product/{product_id}')
async def updation(product_id :str, product:ProductUpdate):
    return await update_product(product_id, product)



@router.post('/create-person')
async def create_person_route(name: str = Form(...), age: float = Form(...), image: UploadFile = File(...)):
    return await create_person(name, age, image)



@router.post('/registration')
async def registration_router(reg:register_model):
    return await registration_user(reg)


@router.post('/login')
async def login_router(email: str, password: str):
    return await login_user(email, password)
