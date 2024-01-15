from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('⛔️ ObjectId Inválido')
        return str(v)

class Customer(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    name: str
    run: Optional[str] = None
    email: str
    whatsapp: str
    purchased: bool = False

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = { ObjectId: str }

class UpdateCustomer(BaseModel):
    name: Optional[str] = None
    run: Optional[str] = None
    email: Optional[str] = None
    whatsapp: Optional[str] = None
    purchased: Optional[bool] = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = { ObjectId: str }