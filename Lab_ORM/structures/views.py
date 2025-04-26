from app import app
from flask import render_template
from structures.models import get_all_buildings, get_type_buildings, get_country_buildings, get_year_buildings, get_year_between_buildings


@app.route('/')
def index():

    [buildings_head, buildings_body] = get_all_buildings()
    [build_type_head, build_type_body] = get_type_buildings()
    [build_country_head, build_country_body] = get_country_buildings()
    [build_year_head, build_year_body] = get_year_buildings()
    [build_year_bet_head, build_year_bet_body] = get_year_between_buildings()

    html = render_template(
        'index.html',
        buildings_head=buildings_head,
        buildings_body=buildings_body,
        build_type_head=build_type_head,
        build_type_body=build_type_body,
        build_country_head=build_country_head,
        build_country_body=build_country_body,
        build_year_head=build_year_head,
        build_year_body=build_year_body,
        start_date=2000,
        end_date=2018,
        build_year_bet_head=build_year_bet_head,
        build_year_bet_body=build_year_bet_body
    )

    return html