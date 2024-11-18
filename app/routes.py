from flask import Blueprint, jsonify, render_template
from app.models import get_random_pokenea
from app.models import POKENEAS
import os

routes = Blueprint("routes", __name__)

@routes.route("/")
def index():
    container_id = os.environ.get("HOSTNAME", "Desconocido")
    return render_template("index.html", pokeneas=POKENEAS, container_id=container_id)

@routes.route("/pokenea/<int:pokenea_id>")
def pokenea_detail(pokenea_id):
    pokenea = next((p for p in POKENEAS if p.id == pokenea_id), None)
    container_id = os.environ.get("HOSTNAME", "Desconocido")
    if pokenea:
        return render_template("pokenea.html", pokenea=pokenea, container_id=container_id)
    return "<h1>Pokenea no encontrado</h1>", 404


@routes.route("/api/random_pokenea", methods=["GET"])
def random_pokenea_json():
    pokenea = get_random_pokenea()
    container_id = os.environ.get("HOSTNAME", "Desconocido")
    return jsonify({
        "pokenea": pokenea.to_json(),
        "container_id": container_id
    })

@routes.route("/random_pokenea", methods=["GET"])
def random_pokenea_page():
    pokenea = get_random_pokenea()
    container_id = os.environ.get("HOSTNAME", "Desconocido")
    return render_template("pokenea.html", pokenea=pokenea, container_id=container_id)
