from flask import Blueprint, request, jsonify

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return "Pick-It-Up is running."

@bp.route("/notify", methods=["POST"])
def notify():
    data = request.json
    apt = data.get("unit_number")
    # TODO: insert notification logic here
    print(f"Notify resident in Unit {apt}")
    return jsonify({"status": "success", "message": f"Notificaiton sent to {apt}."})

