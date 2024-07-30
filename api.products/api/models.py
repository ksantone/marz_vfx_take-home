from peewee import *
import os

db = MySQLDatabase(
    'marz',
    user='interviewer',
    password='changeme',
    host=os.environ.get('MYSQL_HOST', 'localhost'),
    port=int(os.environ.get('MYSQL_PORT', 3306))
)

class BaseModel(Model):
    class Meta:
        database = db

class Products(BaseModel):
    ProductID = AutoField()
    ProductName = CharField(max_length=100)
    ProductPhotoURL = CharField(max_length=255)
    ProductStatus = CharField(max_length=20)