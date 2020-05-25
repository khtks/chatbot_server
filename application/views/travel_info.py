import os
import tempfile

import requests
from PIL import Image
from application import db, api
from application.models.travel_info import TravelInfo
from application.schemata.travel_info import TravelInfoSchema
from flask import Blueprint, request, Response, make_response, render_template, url_for, current_app
from flask_restful import Resource

travel_info_bp = Blueprint("info", __name__, url_prefix='/info')
info_schema = TravelInfoSchema()
session = db.session
api = api(travel_info_bp)


class Info(Resource):
    def get(self, contentID=None):
        if contentID is None:
            return make_response(render_template('display_result.html', title='no data', addr='no data', phone_number='no data', overview='no data', image='no data'), 200)
        result = TravelInfo.query.get(contentID)

        title = result.get_title()
        addr = result.get_addr()
        phone_number = result.get_phone_number()
        img = result.get_img()
        if img != 'No firstimage':
            with tempfile.NamedTemporaryFile(mode="wb") as image:
                response = requests.get(img, stream=True)
                image.write(response.content)
                image.close()

            # import requests
            #
            # url = "http://craphound.com/images/1006884_2adf8fc7.jpg"
            # response = requests.get(url)
            # if response.status_code == 200:
            #     with open("/Users/apple/Desktop/sample.jpg", 'wb') as f:
            #         f.write(response.content)


        overview = result.get_overview()
        overview = [x.lstrip() + '.' for x in overview.split('.')][:-1]

        print(result)

        path = os.path.join('static', 'photo')
        full_filename = os.path.join(path, 'sample_image.png')
        return make_response(render_template('display_result.html', title=title, addr=addr, phone_number=phone_number, overview=overview, image=full_filename), 200)


api.add_resource(Info, '/<string:contentID>')

