from model.product import product,ProductUpdate
from DbConfig.db import product_collection
from fastapi import HTTPException
from bson import ObjectId
from bson.errors import InvalidId


async def create_product(product: product):
    try:
        result = await product_collection.insert_one(product.dict())
        
        if result.acknowledged and result.inserted_id:
            return {
                "message": "Product created successfully",
                "data": {
                    **product.dict(),
                    "_id": str(result.inserted_id)
                }
            }
        else:
            raise HTTPException(status_code=500, detail="Product insertion failed. Try again.")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")



async def get_all_products():
    products = []
    async for product in product_collection.find():
        product["_id"] = str(product["_id"])
        products.append(product)
    return products


async def delete_product(product_id: str):
    if not ObjectId.is_valid(product_id):
        raise HTTPException(status_code=400, detail="This porduct is not exist")
    

    result=await product_collection.delete_one({"_id": ObjectId(product_id)})

    if result.deleted_count==1:
        return{
            "message":"Product delete successfully"
        }
    else:
        raise HTTPException(status_code=404, detail='internal server error')
    

async def update_product(product_id: str, product: ProductUpdate):
    try:
        obj_id = ObjectId(product_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid product ID format")

    update_data = {k: v for k, v in product.dict().items() if v is not None}

    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")

    result = await product_collection.update_one(
        {"_id": obj_id},
        {"$set": update_data}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")

    updated_product = await product_collection.find_one({"_id": obj_id})
    updated_product["_id"] = str(updated_product["_id"]) 
    return {
        "message": "Product updated successfully",
        "product": updated_product
    }
