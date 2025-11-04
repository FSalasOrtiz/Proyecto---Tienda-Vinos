from fastapi import APIRouter, HTTPException
from app.database import db
from app.utils.bson import serialize_doc, to_object_id

router = APIRouter(prefix="/users", tags=["Usuarios"])

@router.get("/")
async def list_users():
    users = await db.usuarios.find().to_list(100)
    return [serialize_doc(u) for u in users]

@router.post("/")
async def create_user(user: dict):
    res = await db.usuarios.insert_one(user)
    doc = await db.usuarios.find_one({"_id": res.inserted_id})
    return serialize_doc(doc)

@router.put("/{user_id}")
async def update_user(user_id: str, data: dict):
    await db.usuarios.update_one({"_id": to_object_id(user_id)}, {"$set": data})
    updated = await db.usuarios.find_one({"_id": to_object_id(user_id)})
    return serialize_doc(updated)

@router.delete("/{user_id}")
async def delete_user(user_id: str):
    await db.usuarios.delete_one({"_id": to_object_id(user_id)})
    return {"msg": "Usuario eliminado"}