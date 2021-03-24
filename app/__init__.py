#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import flask

app = Flask(__name__)

from app import routes
