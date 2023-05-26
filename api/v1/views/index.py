#!/usr/bin/python3
"""This module implement a rule responsible for returning the
    status of the application"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": "OK"})
