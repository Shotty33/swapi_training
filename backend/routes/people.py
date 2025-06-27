from flask import Blueprint, jsonify
from services.swapi_service import SwapiService

people_bp = Blueprint('people', __name__)
swapi_service = SwapiService()

@people_bp.route("/", methods=["GET"])
def get_people():
    people = swapi_service.get_people()
    return jsonify(people)
