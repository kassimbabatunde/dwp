# DWP API Implementation
 
The repo consist of backend DWP API implementation.  
## Backend Implementation  
The backend in implemented using python3.9 with FastAPI framework.    
Run pip command to install FastAPI and the required python library for FastApi using following command:  
```pip install -r requirements.txt```  
Next run the following command to start the appliation:  
```uvicorn main:app --host 0.0.0.0 --port 8000```  
This will start the backend server.
Check the localhost on 127.0.0.0:8000/docs to see available APIs

## Implemented APIs
1. The first impementation is root ("/") which serve as default to 127.0.0.0/8000   
2. The second API get the list of all people  
3. The third API get people listed as either living in a {city} deafult:London, or whose current coordinates are within 50 miles default of London.
