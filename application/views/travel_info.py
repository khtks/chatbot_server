import os
import tempfile

import requests
from PIL import Image
from application import db, api
from application.models.travel_info import TravelInfo
from application.schemata.travel_info import TravelInfoSchema
from flask import Blueprint, request, Response, make_response, render_template, url_for, current_app
from flask_restful import Resource

import boto3
from boto3.dynamodb.conditions import Key, Attr

travel_info_bp = Blueprint("info", __name__, url_prefix='/info')
info_schema = TravelInfoSchema()
session = db.session
api = api(travel_info_bp)

dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-2')
TableInformation = dynamodb.Table('ChatBotForInformation')
TableSearch = dynamodb.Table('ChatBotForSearch')


class Info(Resource):
    def get(self, contentID=None):
        if contentID is None:
            return make_response(render_template('display_result.html', title='no data', addr='no data', phone_number='no data', overview='no data', image='no data'), 200)

        result = TableInformation.get_item(Key={'contentID': contentID})
        res = result.get('Item')

        title = res.get('title')
        addr = res.get('addr')
        phone_number = res.get('tel')
        img = res.get('firstImage')
        if img != 'No firstimage':
            # with tempfile.NamedTemporaryFile(mode="wb") as image:
            #     response = requests.get(img, stream=True)
            #     image.write(response.content)
            #     image.close()
            pass

        overview = img = res.get('overview')
        # overview = [x.lstrip() + '.' for x in overview.split('.')][:-1]

        path = os.path.join('static', 'photo')
        full_filename = os.path.join(path, 'sample_image.png')
        return make_response(render_template('display_result.html', title=title, addr=addr, phone_number=phone_number, overview=overview, image=full_filename), 200)


api.add_resource(Info, '/<int:contentID>')

