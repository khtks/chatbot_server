from flask_marshmallow import Marshmallow
from application import ma
from application.models.travel_info import *


class TravelInfoSchema(ma.ModelSchema):
    class Meta:
        model = TravelInfo
