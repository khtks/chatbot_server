from application import db, api
from application.models.travel_info import TravelInfo
from application.schemata.travel_info import TravelInfoSchema
from flask import Blueprint, request, Response, make_response, render_template, url_for, current_app
from flask_restful import Resource
import datetime

travel_info_bp = Blueprint("info", __name__, url_prefix='/info')
info_schema = TravelInfoSchema()
session = db.session
api = api(travel_info_bp)
headers = {'Content-Type': 'text/html'}


class Info(Resource):
    def get(self):
        pass
