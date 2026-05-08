from app.admin import bp

@bp.route('/')
def index():
    return "Admin index"
