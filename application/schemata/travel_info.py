from application import ma
from application.models.travel_info import *


class TravelInfoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TravelInfo
