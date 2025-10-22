from fastapi import FastAPI,Path,HTTPException,Query
import json
app=FastAPI()


patients=None
with open("patients.json",'r') as f:
    patients=json.loads(f.read())

#for viewing all data
@app.get("/view")
def view():
    return patients
        
# endpoit for viewing data of any customer by customer id
# here patientid is a path parameter which is used to identify the patient
# Path parameters are used to identify a specific resource in the URL
# We can use Path function to define the path parameter and its properties like description,example etc.
# If the patientid is not found in the patients dictionary, we will raise an HTTPException with status code 400 and detail message
# here ... indicate that they are required paramaters
@app.get("/patient/{patientid}")
def viewpatient(patientid:str=Path(...,description="ID of patient",example="P001")):
    if patientid in patients:
        return patients[patientid]
    
    raise HTTPException(status_code=400,detail="No user found")


# query parameters these are parameters that are passed in the URL in the form of key-value pairs separated by '&' these are optional parameters
# and can be used to filter the data,search the data, or perform other operations We can use Query function as we use Path function for path parameters
    
@app.get("/allPatients")
def getPatients(sortby:str = Query(...,description="Sort on the basis of - bmi , height, wieght"),
                order:str=Query(default="asc",description='Set order - asc or desc')):
    
    sortValues=['height','weight','bmi']
    if sortby not in sortValues:
        raise HTTPException(status_code=400,detail=f'Invalid field selected for sortby select from {sortValues}')
    
    ordValues=['asc','desc']
    if order not in ordValues:
        raise HTTPException(status_code=400,detail=f'Invalid field selected for order select from {ordValues}')

    ans=sorted(patients,key=lambda x:patients[x][sortby],reverse=False if ordValues=='asc' else True)
    

    return {i:patients[i] for i in ans}
