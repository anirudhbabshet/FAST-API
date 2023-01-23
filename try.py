from pydantic import BaseModel

class User(BaseModel):
    id: int
    name = 'Jane Doe'

user = User(id='123')
user_x = User(id='1234')

assert user.id == 123
assert user_x.id == 1234
assert isinstance(user_x.id, int)  # Note that 123.45 was casted to an int and its value is 123