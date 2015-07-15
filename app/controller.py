from flask import request
import app.model, app.view

model = app.model
view = app.view

#
# Site
def site(page):
    pass

#
# Apmin
def admin(page):
    pass

#
# API
def methods(method):
    if method == "id.getUser":
        return view.response(
            model.id_get()
            )

    if method == "id.list":
        return view.response(
            model.id_list()
            )

    elif method == "game.getPost":
        return view.response(
            model.game_get()
            )
        
    if method == "game.list":
        return view.response(
            model.game_list()
            )

    elif method == "game.getCategory":
        return view.response(
            model.game_getCategory()
            )

    elif method == "game.getAuthor":
        return view.response(
            model.game_getAuthor()
            )

    elif method == "category.get":
        return view.response(
            model.category_get()
            )

    elif method == "category.list":
        return view.response(
            model.category_list()
            )
        
    else:
        return view.response(
            {
                "error":"invalid method"
            }
            )