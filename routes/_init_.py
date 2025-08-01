from .login_route import login_routes

def register_route(app):
    app.register_blueprint(login_routes)
   
