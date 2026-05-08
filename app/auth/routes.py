from app.auth import bp

@bp.route('/login')
def login():
    return "Login page"

@bp.route('/register')
def register():
    return "Register page"
