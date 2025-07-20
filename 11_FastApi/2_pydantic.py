from fastapi import FastAPI
import json
from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator,computed_field
from typing import List,Dict,Optional,Annotated

# pydantic is used for data validation and settings management using Python type annotations
# app=FastAPI()

class Patient(BaseModel):
    name: str =Field(max_length=50)  # it ensure max length of 50 
    age: int 
    email:Optional[EmailStr]=None # it ensure that email is in email format
    profilepic:Optional[AnyUrl]=None # it ensure that it is in url format
    weight: float =Field(gt=0,lt=100)  # it ensure weight is >0 and <100
    bmi: float = None  #setting default value
    married:Optional[bool]=None # optional field (by default all fields are required in pydantic) with default value none 
    disease:List[str]   # we are not using only list because we also want to validate that disease must be a string of list and same for dict
    contac_details:Optional[Dict[str,str]]=None 
    height: Annotated[int,Field(title="Height in cms",description='enter height and dont enter unit',examples=["165",'123'],strict=True)] # by setting stric=True we ensure that pydantic do not do type conversion otherwise it will allow '30' as a valid int 

def addPatient(patient:Patient):
    print(patient.name)    
    print(patient.age)    
    print(patient.weight)    
    print(patient.bmi)
    print(patient.disease)
    print(patient.contac_details)
    
    
patient_info={"name":"pankaj","age":20,"weight":60,"bmi":18,"disease":['disease1','disease2'],"contac_details":{"email":"abc@gmail.com","phone":'22345'},"height":123}

patient_info_err={"name":"pankaj","age":'twenty',"weight":60,"bmi":18,"disease":['disease1','disease2']}
patient_info2={"name":"pankaj","age":'20',"weight":60,"disease":['disease1','disease2'],"height":20}

addPatient(Patient(**patient_info))

# it will raise error due to age field
# addPatient(Patient(**patient_info_err))


# here it won't raise any error because pydantic will do type conversion by itself for age field
addPatient(Patient(**patient_info2))



# feild validator - by using feild validator we can add custom checking like

class Patient2(BaseModel):
    name:str
    email:EmailStr
    
    @field_validator('email')
    @classmethod
    def verify_meail(cls,email):
        valid_domain='iiitk.ac.in'
        if email.split('@')[-1]==valid_domain:
            return email
        raise ValueError("Not a valid domain")
    
    
    @field_validator('name')
    @classmethod
    def capitaliseName(cls,name):
        return name.capitalize()
    
    
def func(patient:Patient2):
    print(patient.name)
    print(patient.email)

# Field validator has two mode 1-before validation and 2-after validation
# default value of mode is after
# if we want to run before validation then we can use @field_validator('email',mode='before')

# after validation give values to fieldvalidator after type conversion and validation
# before validation give values to fieldvalidator before type conversion and validation

patient={"name":"pankaj","email":"aba@iiitk.ac.in"}
func(Patient2(**patient))


# MODEL VALIDATOR

# we want to ensure that if age of patient>60 then there must be a emergency contact no
class Patient3(BaseModel):
    name:str
    age:int
    emergenyNo:Optional[int]=None
    
    @model_validator(mode="after")
    def validate_emergencyNo(cls,model):
        if model.age>60 and model.emergenyNo is None:
            raise ValueError("patient age 60 must have an emergy contact")
        return model

def func(patient:Patient3):
    print(patient.name)
    print(patient.age)
    print(patient.emergenyNo)
    
        
patient_old={"name":"oldman","age":80,"emergenyNo":2285}
patient_old_err={"name":"oldman","age":80}
patient_young={"name":"youngman","age":20}

func(Patient3(**patient_old))
# func(Patient3(**patient_old_err))
func(Patient3(**patient_young))



# ComputedField

class Patient3(BaseModel):
    
    height:float
    weight:float

    
    @computed_field
    def bmi(self)->float:
        return round(self.weight/self.height**2,2)
    # a new field will be created of name bmi
    
def func(patient:Patient3):
    print(patient.height)
    print(patient.weight)
    print(patient.bmi)
    
        
patient1={"height":1.7,"weight":60}

func(Patient3(**patient1))


#NESTED PYDANTIC MODELS

class Address(BaseModel):
    city:str
    state:str
    pincode:int
    
class Patient5(BaseModel):
    name:str
    age:Optional[int]=None
    address:Address
    
def func(patient:Patient5):
    print(patient.name)
    print(patient.address)
    print(patient.age)
    
address1=Address(**{"city":'rmr','state':"ap","pincode":518002})
patient1=Patient5(**{"name":"abc","address":address1})
func(patient1)

# serilization/Exporting

print(patient1.model_dump())
print(type(patient1.model_dump()))
print(patient1.model_dump(include=['name']))
print(patient1.model_dump(exclude=['name']))
print(patient1.model_dump(exclude={"address":['state']}))
print(patient1.model_dump(exclude_unset=True))       # it excludes all fields that are not created while creating an object
