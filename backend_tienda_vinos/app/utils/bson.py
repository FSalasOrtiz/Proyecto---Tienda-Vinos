from bson import ObjectId

def to_object_id(id_str: str) -> ObjectId:
    if isinstance(id_str, ObjectId):
        return id_str
    return ObjectId(str(id_str))

def serialize_doc(doc: dict) -> dict:
    if not doc:
        return doc
    doc["id"] = str(doc.pop("_id"))
    return doc