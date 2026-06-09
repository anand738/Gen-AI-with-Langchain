from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name:str='Anand'
    age:Optional[int]=None
    email:EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')

    
new_student = {'age':'32','email':'anand@gmail.com'}

student = Student(**new_student)
student_dict = student.model_dump()   # Pydantic v2

print(student_dict['age'])

# print(student.name)
# print(student)