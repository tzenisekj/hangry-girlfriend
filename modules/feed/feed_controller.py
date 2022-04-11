from flask import Blueprint, request, jsonify
from flask.wrappers import Response
from modules.feed.services.feed import FeedService
import logging

from modules.models.feedings import Feedings

feed_api = Blueprint('feed_api', __name__)

feed_service = FeedService()

@feed_api.route('/feed', methods=['POST'])
def feed_girlfriend():
    feed_service.add(Feedings(request.json['amount']))