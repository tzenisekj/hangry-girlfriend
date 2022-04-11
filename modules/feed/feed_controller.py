from flask import Blueprint, request, jsonify
from flask.wrappers import Response
from modules.exceptions.negative_food_exception import NegativeFoodException
from modules.feed.services.feed_impl import FeedServiceImpl
import logging

from modules.models.feedings import Feedings

feed_api = Blueprint('feed_api', __name__)

feed_service = FeedServiceImpl()

@feed_api.route('/feed', methods=['POST'])
def feed_girlfriend():
    try:
        feed_service.add(Feedings(request.json['amount']))
        return jsonify({
            'status': "Success"
            })
    except NegativeFoodException as e:
        return Response("You really shouldn't be taking food away from the girlfriend", 400)