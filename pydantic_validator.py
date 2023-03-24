from pydantic import BaseModel,Field
from typing import Optional

class Curtime(BaseModel):
    curtime: Optional[int] = None

class User(BaseModel):
    name: str = Field(min_length=2)
    age: int = Field(ge=80)

def validator(model):
    def decorate(func):
        def wrapper(data):
            try:
                time = model(**data)
                return func(time)
            except ValueError as e:
                print(e.json())
                return None
        return wrapper
    return decorate

@validator(model=Curtime)
def t_time(curtime: Optional[Curtime] = None):
    print(curtime.curtime)
    
@validator(model=User)
def user(user: User):
    print(user)

# t_time({"curtime":1})
user({"name":"t","age":81})



