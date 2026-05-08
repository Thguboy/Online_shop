from flask import jsonify
from app.api import bp

@bp.route('/status')
def status():
    return jsonify({"status": "ok"})
