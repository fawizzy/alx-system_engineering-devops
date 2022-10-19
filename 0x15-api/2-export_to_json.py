#!/usr/bin/python3

import requests
import sys
import json
URL = "https://jsonplaceholder.typicode.com/"
id = sys.argv[1]
no_of_tasks = 0
task_done = 0
title_done = []
title = []
dict_list = []
dict_obj = {}
if __name__ == "__main__":
    users = URL + "users/" + id
    todos = URL + "todos"
    user_json = requests.get(users)
    todos_json = requests.get(todos)
    name = user_json.json()["name"]
    username = user_json.json()["username"]
    for v in todos_json.json():
        if v["userId"] == int(id):
            dict_task = {"task": v["title"],
             "completed" : v["completed"],
             "username": username}
            dict_list.append(dict_task)
    dict_obj[id] = dict_list
    with open(f'{id}.json','w') as file:
        json.dump(dict_obj, file)
    