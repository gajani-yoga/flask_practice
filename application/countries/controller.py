from flask import jsonify, request
from werkzeug import exceptions
from .models import Country
from .. import db

def index():
     countries = Country.query.all()
     try:
        data = []
        for country in countries:
            data.append(country.json)

        return jsonify({
            "data": [c.json for c in countries] }), 200
     except:
        raise exceptions.InternalServerError(f"We are working on it")

def show(id):
    print('id', type(id))
    country = Country.query.filter_by(id=id).first()
    try:
        return jsonify({ "data": country.json }), 200
    except:
        raise exceptions.NotFound(f"You get it")

def create():
    try:
        name, population, capital_city = request.json.values()
        new_country = Country(name, population, capital_city)

        db.session.add(new_country)
        db.session.commit()
        return jsonify({ "data": new_country.json }), 201
    except:
         raise exceptions.BadRequest(f"We cannot process your request")

def update(id):
    data = request.json
    country = Country.query.filter_by(id=id).first()

    for (attribute, value) in data.items():
        if hasattr(country, attribute):
            setattr(country, attribute, value)
    db.session.commit()
    return jsonify({ "data": country.json })

def destroy(id):
    country = Country.query.filter_by(id=id).first()
    db.session.delete(country)
    db.session.commit()
    return "Country deleted", 204