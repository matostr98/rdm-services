# PeselGen

## Requirements 
#TODO: ADD REQUIREMENTS 

## Run  
### python manage.py makemigrations \<appname\>   
where \<appname\> could be 'person' or 'metrics'  
  
### python manage.py migrate  
### python manage.py runserver  

## Endpoints  
/person - method: GET - shows generated persons  
/metrics - method: GET - shows generated patient metrics  
/generate - method: POST - generates persons then metrics  
/generate/flush - method: PUT - deletes all records from both database tables  
/generate/flush/\<table\> - method: PUT - deletes all records from specified table, could be 'person' or 'metrics'  
  
## Data model 
#TODO: ADD DATA MODEL DESCRIPTION 

## How it works?
#TODO: ADD SERVICE DESCRIPTION 

## Aouut us 
#TODO: ADD ABOUT 
