from flask import request
import database
db = database

#
# API methods
#
def id_get():
    user_id = request.args.get("user_id")
    if user_id == None or user_id == "":
        return {"error": "invalid 'user_id' key"}
    return db.printColumn("id", user_id)[1]

def id_list():
    start_id = request.args.get("start_id")
    limit = request.args.get("limit")
    if start_id == None or start_id == "":
        return {"error": "invalid 'start_id' key"}
    if limit == None or limit == "":
        return {"error": "invalid 'limit' key"}
    return db.listColumsSecret("id", start_id, limit)

def game_get():
    post_id = request.args.get("post_id")
    if post_id == None or post_id == "":
        return {"error": "invalid 'post_id' key"}
    return db.printColumn("game", post_id)

def game_list():
    start_id = request.args.get("start_id")
    limit = request.args.get("limit")
    if start_id == None or start_id == "":
        return {"error": "invalid 'start_id' key"}
    if limit == None or limit == "":
        return {"error": "invalid 'limit' key"}
    return db.listColums("game", start_id, limit)

def game_getCategory():
    post_id = request.args.get("post_id")
    if post_id == None or post_id == "":
        return {"error": "invalid 'post_id' key"}
    post = db.printColumn("game", post_id)
    return db.printColumn("category", post["category"])

def game_getAuthor():
    post_id = request.args.get("post_id")
    if post_id == None or post_id == "":
        return {"error": "invalid 'post_id' key"}
    post = db.printColumn("game", post_id)
    return db.printColumn("id", post["author"])[1]

def category_get():
    category_id = request.args.get("category_id")
    if category_id == None or category_id == "":
        return {"error": "invalid 'category_id' key"}
    post = db.printColumn("game", category_id)
    return db.printColumn("category", post["category"])

def category_list():
    start_id = request.args.get("start_id")
    limit = request.args.get("limit")
    if start_id == None or start_id == "":
        return {"error": "invalid 'start_id' key"}
    if limit == None or limit == "":
        return {"error": "invalid 'limit' key"}
    return db.listColums("category", start_id, limit)
#
# End
#