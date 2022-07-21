from pydantic import BaseModel, Field, validator
from typing import List


class RequestPairString(BaseModel):
    id: int
    string1: str = Field(max_length=20,
                         description='String with length less than 20',
                         example='Hello')
    string2: str = Field(max_length=20,
                         description='String with length less than 20',
                         example='Helio')


class ResponsePairString(BaseModel):
    id: int
    score: float


class User(BaseModel):
    first_name: str
    last_name: str
    address: str
    zip: int = 100000

    @validator('zip')
    def val_len(cls, v: int) -> int:
        if len(str(v)) != 6:
            raise ValueError('len of zip must be 6')
        return v

    @validator('first_name', 'last_name', 'address')
    def lower(cls, v: str) -> str:
        return v.lower()

    def concatenate(self):
        return f'{self.first_name} {self.last_name} {self.address}'


class RequestScoring(BaseModel):
    user: User
    candidates: List[User]
    limit: int = 5


class ResponseUser(BaseModel):
    concat: str
    score: float
    index: int


class ResponseScoring(BaseModel):
    users: List[ResponseUser]
