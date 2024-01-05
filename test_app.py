from application import app # app from __init__.py
import json

def test_get_countries(app):
    res = app.get('/countries')
    assert res.json == {'countries': [{'id': 1, "name": "France",
    "population": 64756584, "capital_city": "Paris"}, {'id': 2, "name": "Netherlands",
    "population": 17938053, "capital_city": "Amsterdam"}]}

def test_get_country(app):
    res = app.get('/countries/2')
    assert res.json['data']['name'] == 'Netherlands'

def test_post_country(app):
    mock_data = json.dumps({'name': 'Austria', 'population': 12353253, 'capital_city': 'Vienna'})
    mock_headers = {'Content-Type': 'application/json'}
    res = app.post('/countries', data=mock_data, headers=mock_headers)
    assert res.json['data']['id'] == 6

def test_api_not_found(app):
    res = app.get('/bob')
    assert res.status == '404 NOT FOUND'
    assert 'Oops!' in res.json['message']