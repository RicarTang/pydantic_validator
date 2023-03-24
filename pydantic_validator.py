from pydantic import BaseModel,Field
from typing import Optional

class Curtime(BaseModel):
    """定义pydantic模型"""
    curtime: Optional[int] = None

class User(BaseModel):
    name: str = Field(min_length=2)
    age: int = Field(ge=0)

def validator(model):
    """定义验证装饰器

    Args:
        model (PydanticModel): 带参数的装饰器，传入pydantic模型
    """
    def decorate(func):
        def wrapper(data):
            try:
                pydantic_obj = model(**data)
                return func(pydantic_obj)
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
user({"name":"tang","age":9})



