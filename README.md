# Random Data Maker
## Overview
Random Data Maker is a REST webservice for defined data sets, including personal data and medical metrics data for machine learning.

## Requirements 
##### Software: 
* Python 3.7.5
* MySQL 8.0 with Docker support provided
##### Frameworks & libraries:
* Django 2.2.7
* django-cors-headers 3.1.1
* djangorestframework 3.10.3
* enum34 1.1.6
* jsonfield 2.0.2
* mysqlclient 1.4.5
* sqlparse 0.3.0

## Run  
To run this app you will need MySQL database that you can create from dockerfile inside project `docker-compose.yml`. Then you must do migrations: 
* `python manage.py makemigrations <appname> `
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; where \<appname\> could be 'person' or 'metrics'  
* `python manage.py migrate`

And run app: 
* `python manage.py runserver`

## Endpoints  
`/person` - method: GET - returns generated persons  
`/metrics` - method: GET - returns generated patient metrics  
`/generate` - method: POST - generates persons then metrics and attributes
`/generate/flush` - method: PUT - deletes all records from both database tables  
`/generate/flush/<table>` - method: PUT - deletes all records from specified table, could be 'person' or 'metrics'  
`/attributes` - method:POST - generates attributes from model
`/attributes` - method:GET - returns attributes records
  
## Data model 
Data model is in JSON format. It is used to specify what kind of data app should generate. It is generated in a form of the list of objects with predefined attributes:
* `key` - string value representing object name
* `count` - integer value representing how many times this data should be generated
* `array` - array of values from whitch data will be generated
* `weight` - array of integers showing the probability of occurance of element from attribute array
* `minimum` - smallest value that will be generated
* `maximum` - biggest value that will be generated
* `type` - type of generated date e.g *float* 
* `floating_points` - number of digits after decimal point

## How it works?
Random Data Maker is a rest api app and has defined endpoints to communicate with it. It has three kinds of endpoints: generating number of random records (POST), getting them from database in the form of JSON (GET) and flushing tables (PUT). When post method is used it generates random data e.g personal data, metrics data using apps own random data generator and saves it in database. This random data generator takes JSON file with defined data model and uses it to generate new data. When data is in a database it can be accessed with get methods. Project was originally made as support for medical machine learning system OCULUS Project

## About us 
We're Computer Science students at Poznan University of Technology. We like programming and had a lot of fun creating this project.  
[Artur Bałczyński](https://github.com/arturbalcz)  
[Mateusz Ostrowski](https://github.com/matostr98)  
[Adam Przywuski](https://github.com/adamprzywuski)  
[Maciej Stosik](https://github.com/SaronTetra)  
