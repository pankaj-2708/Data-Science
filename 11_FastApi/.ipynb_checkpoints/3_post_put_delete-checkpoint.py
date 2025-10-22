from pydantic import BaseModel,Field,computed_field
from typing import Literal,Annotated,Optional
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
app=FastAPI()

# pydantic fields validtator

class Patient_Create(BaseModel):
    name:str=Field(...,name="Name",description="Enter your full name")
    city:str=Field(...,name="City")
    age:int=Field(...,ge=0)
    gender:Literal['male','female','others']=Field(...,name="Gender",description="Enter male,female or others")
    height:float=Field(...,name="Height",description="Enter height in meters",gt=0)
    weight:float=Field(...,name="Weight",description="Enter weight in kg",gt=0)
    
    @computed_field
    def bmi(self)->float:
        return round(self.weight/self.height**2,2)
    
    @computed_field
    def verdict(self)->str:
        if self.bmi<18.5:
            return "Underweight"
        elif self.bmi<25:
            return "Normal"
        elif self.bmi<30:
            return "Overweight"
        else:
            return "Obese"
    
#endpoint
# here fast api works very closely with pydantic so we dont have to define the request body type explicitly it infers the type from the pydantic model and validates the data 
# if we will not be using fastapi then we will have to define the request body type explicitly like eg
@app.post("/create")
def create_patient(patient:Patient_Create):
    patients={}
    with open("patients.json",'r') as f:
        patients=json.loads(f.read())
    key=list(patients.keys())[-1]
    patients[f"{key[0]+"{:03d}".format(int(key[1:])+1)}"]=patient.model_dump()
    with open("patients.json",'w') as f:
        json.dump(fp=f,obj=patients)
    return JSONResponse(status_code=201,content={"message":f"patient created with id {key[0]+"{:03d}".format(int(key[1:])+1)} "})

    
#Put - put method is generally used for update quereis

class Patient_Update(BaseModel):
    name:Optional[str]=Field(name="Name",description="Enter your full name",default=None)
    city:Optional[str]=Field(name="City",default=None)
    age:Optional[int]=Field(ge=0,default=None)
    gender:Optional[Literal['male','female','others']]=Field(name="Gender",description="Enter male,female or others",default=None)
    height:Optional[float]=Field(name="Height",description="Enter height in meters",gt=0,default=None)
    weight:Optional[float]=Field(name="Weight",description="Enter weight in kg",gt=0,default=None)
    
        
@app.put("/edit/{patientid}")
def edit_patient(patientid:str,patientData:Patient_Create):
    patients={}
    with open("patients.json",'r') as f:
        patients=json.loads(f.read())
    keys=list(patients.keys())
    
    if patientid not in keys:
        return JSONResponse(status_code=404,content={"message":"user not found"})
    
    orignal_patient=patients[patientid]
    new_patient=patientData.model_dump(exclude_unset=True) #it wont include the fields which are not updated/setted

    for key in new_patient.keys():
        orignal_patient[key]=new_patient[key]
    
        
    # now we will create an object of patient_create  so that computed field will be updated automatically
    
    patient_n=Patient_Create(**orignal_patient).model_dump()
    
    patients[patientid]=patient_n
    
    with open("patients.json",'w') as f:
        json.dump(fp=f,obj=patients)
        
    return JSONResponse(status_code=200,content={"message":"patient updated"})



@app.put("/delete/{patientid}")
def delete_patient(patientid:str):
    patients={}
    with open("patients.json",'r') as f:
        patients=json.loads(f.read())
    keys=list(patients.keys())
    
    if patientid not in keys:
        return JSONResponse(status_code=404,content={"message":"user not found"})
    
    del patients[patientid]

    with open("patients.json",'w') as f:
        json.dump(fp=f,obj=patients)
        
    return JSONResponse(status_code=200,content={"message":"patient deleted"})
