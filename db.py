from flask import Flask, render_template, request, redirect, url_for
import os
import pymongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
import datetime
load_dotenv()

connection = pymongo.MongoClient(os.getenv('MONGO_URI'))
db = connection[os.getenv('MONGO_DBNAME')]

# create test DB
doc1 = {
    "username": "admin",
    "password": "123456",
    "tasks": [
        {
            "_id": ObjectId(),
            "title": "Task 1",
            "course": "Agile Development & DevOps",
            "date": datetime.datetime.now()
        },
        {
            "_id":ObjectId(),
            "title": "Task 2",
            "course": "Software Engineering",
            "date": datetime.datetime.now()
        }
    ]
}
doc2 = {
    "username": "admin2",
    "password": "654321",
    "tasks": [
        {
            "_id": ObjectId(),
            "title": "Task A",
            "course": "Computer Graphics",
            "date": datetime.datetime.now()
        },
        {
            "_id":ObjectId(),
            "title": "Task B",
            "course": "Computer Virsion",
            "date": datetime.datetime.now()
        },
        {
            "_id": ObjectId(),
            "title": "Task C",
            "course": "Computer Graphics",
            "date": datetime.datetime.now()
        },
        {
            "_id": ObjectId(),
            "title": "Task D",
            "course": "Computer Graphics",
            "date": datetime.datetime.now()
        },
        {
            "_id": ObjectId(),
            "title": "Task E",
            "course": "Computer Graphics",
            "date": datetime.datetime.now()
        },
        {
            "_id": ObjectId(),
            "title": "Task F",
            "course": "Computer Graphics",
            "date": datetime.datetime.now()
        },
        {
            "_id": ObjectId(),
            "title": "Task G",
            "course": "Computer Graphics",
            "date": datetime.datetime.now()
        },
    ]
}

mongoid = db.get_collection("users").insert_one(doc1)
mongoid = db.get_collection("users").insert_one(doc2)