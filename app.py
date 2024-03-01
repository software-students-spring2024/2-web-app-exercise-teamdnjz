from flask import Flask, render_template, request, redirect, url_for
import os
import pymongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
import datetime
load_dotenv()

app = Flask(__name__)

connection = pymongo.MongoClient(os.getenv('MONGO_URI'))
db = connection[os.getenv('MONGO_DBNAME')]

@app.route('/')
def home():
    user = db.get_collection("users").find_one({"username": "admin2"})
    tasks = user['tasks']
    return render_template('index.html', tasks=tasks, user=user)

@app.route('/edit/<user_id>/<task_id>')
def edit(task_id, user_id):
    user = db.users.find_one({"_id": ObjectId(user_id)})
    index = find_index_by_id(user['tasks'], ObjectId(task_id))
    task = user['tasks'][index]
    title = task['title']
    course = task['course']
    date = task['date']
    return render_template('edit.html', title=title, course=course, date=date, task=task, user=user)

def find_index_by_id(task_list, id):
    for index, task in enumerate(task_list):
        if task["_id"] == id:
            return index
    return -1

@app.route('/edit/<user_id>/<task_id>', methods=['POST'])
def edit_task(task_id, user_id):
    title = request.form["title"]
    course = request.form["course"]
    date = request.form["date"]
    
    updated_task = {
        "_id": ObjectId(task_id),
        "title": title,
        "course": course,
        "date": date
    }

    db.users.update_one(
    {"_id": ObjectId(user_id), "tasks._id": ObjectId(task_id)},
    {"$set": {"tasks.$": updated_task}}
)
    return redirect(
        url_for("home")
    )

@app.route('/delete/<user_id>/<task_id>')
def delete(task_id, user_id):
    user = db.users.find_one({"_id": ObjectId(user_id)})
    index = find_index_by_id(user['tasks'], ObjectId(task_id))
    task = user['tasks'][index]
    title = task['title']
    course = task['course']
    date = task['date']
    return render_template('delete.html', title=title, course=course, date=date, task=task, user=user)

@app.route('/delete/<user_id>/<task_id>', methods=['POST'])
def delete_task(task_id, user_id):
    db.users.update_one(
        {"_id": ObjectId(user_id)},
        {"$pull": {"tasks": {"_id": ObjectId(task_id)}}}
    )
    return redirect(
        url_for("home")
    )


if __name__ == '__main__':
    app.run()



