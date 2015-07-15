from . import api
from flask import jsonify, request, abort
import database as db

@api.route('/id.getUser')
def get_user():
    user_id = request.args.get("user_id")
    if user_id == None or user_id == "":
        return jsonify({"error": "invalid 'user_id' key"})
    return jsonify(db.printColumn("id", user_id)[1])

@api.route('/id.list')
def id_list():
    start_id = request.args.get("start_id")
    limit = request.args.get("limit")
    if start_id == None or start_id == "":
        return jsonify({"error": "invalid 'start_id' key"})
    if limit == None or limit == "":
        return jsonify({"error": "invalid 'limit' key"})
    return jsonify(db.listColumsSecret("id", start_id, limit))

@api.route('/game.getPost')
def game_getpost():
    post_id = request.args.get("post_id")
    if post_id == None or post_id == "":
        return jsonify({"error": "invalid 'post_id' key"})
    return jsonify(db.printColumn("game", post_id))

@api.route('/game.getList')
def game_list():
    start_id = request.args.get("start_id")
    limit = request.args.get("limit")
    if start_id == None or start_id == "":
        return jsonify({"error": "invalid 'start_id' key"})
    if limit == None or limit == "":
        return jsonify({"error": "invalid 'limit' key"})
    return jsonify(db.listColums("game", start_id, limit))

@api.route('/game.getCategory')
def game_getCategory():
    post_id = request.args.get("post_id")
    if post_id == None or post_id == "":
        return jsonify({"error": "invalid 'post_id' key"})
    post = db.printColumn("game", post_id)
    return jsonify(db.printColumn("category", post["category"]))

@api.route('/game.getAuthor')
def game_getAuthor():
    post_id = request.args.get("post_id")
    if post_id == None or post_id == "":
        return jsonify({"error": "invalid 'post_id' key"})
    post = db.printColumn("game", post_id)
    return jsonify(db.printColumn("id", post["author"])[1])

@api.route('/category.get')
def category_get():
    category_id = request.args.get("category_id")
    if category_id == None or category_id == "":
        return jsonify({"error": "invalid 'category_id' key"})
    post = db.printColumn("game", category_id)
    return jsonify(db.printColumn("category", post["category"]))

@api.route('/category.list')
def category_list():
    start_id = request.args.get("start_id")
    limit = request.args.get("limit")
    if start_id == None or start_id == "":
        return jsonify({"error": "invalid 'start_id' key"})
    if limit == None or limit == "":
        return jsonify({"error": "invalid 'limit' key"})
    return jsonify(db.listColums("category", start_id, limit))

