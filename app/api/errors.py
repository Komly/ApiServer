from flask import abort, jsonify
from . import api

# fix for flask handling 404 on blueprint level
@api.route('/', defaults={'path': None})
@api.route('/<path:invalid_path>')
def handle_unmatchable(*args, **kwargs):
    abort(404)

@api.errorhandler(404)
def method_not_found(e):
    return jsonify({"error":"invalid method"}), 404
