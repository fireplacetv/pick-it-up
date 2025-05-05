from flask import Blueprint, request, jsonify, render_template

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/notify", methods=["POST"])
def notify():
    data = request.json
    unit_number = data.get("unit_number")
    # TODO: insert notification logic here
    print(f"TODO: Notify resident in {unit_number}")

    return jsonify({"status": "success", "message": f"Notificaiton sent to {unit_number}."})

