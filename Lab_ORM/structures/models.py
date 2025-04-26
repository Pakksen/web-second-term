from config import db 
from models import Country, City, Building, TypeBuilding
from sqlalchemy import func

def get_all_buildings():
    query = (
        db.session.query(
            Building.title.label("Здание"),
            TypeBuilding.type.label("Тип"),
            Country.name.label("Страна"),
            City.name.label("Город"),
            Building.year.label("Год"),
            Building.height.label("Высота")
          )
        .select_from(Building)
        .join(TypeBuilding)
        .join(City)
        .join(Country)
        
    )
    return [query.statement.columns.keys(), query.all()]

def get_type_buildings():
    query_t = (
        db.session.query(
          TypeBuilding.type.label("Тип"),
          func.max(Building.height).label("Максимальная высота"),
          func.min(Building.height).label("Минимальная высота"),
          func.avg(Building.height).label("Средняя высота")
        )
        .select_from(TypeBuilding)
        .join(Building)
        .group_by(TypeBuilding.type)
      )
    return [query_t.statement.columns.keys(), query_t.all()]

def get_country_buildings():
    query_c = (
        db.session.query(
          Country.name.label("Тип"),
          func.max(Building.height).label("Максимальная высота"),
          func.min(Building.height).label("Минимальная высота"),
          func.avg(Building.height).label("Средняя высота")
        )
        .select_from(TypeBuilding)
        .join(Building)
        .join(City)
        .join(Country)
        .group_by(TypeBuilding.type)
      )
    return [query_c.statement.columns.keys(), query_c.all()]

def get_year_buildings():
    query_y = (
        db.session.query(
          Building.year.label("Тип"),
          func.max(Building.height).label("Максимальная высота"),
          func.min(Building.height).label("Минимальная высота"),
          func.avg(Building.height).label("Средняя высота")
        )
        .select_from(TypeBuilding)
        .join(Building)
        .group_by(TypeBuilding.type)
      )
    return [query_y.statement.columns.keys(), query_y.all()]

def get_year_between_buildings():
    query_b = (
        db.session.query(
          Building.title.label("Здание"),
          Building.year.label("Год"),
          Building.height.label("Высота"),
          TypeBuilding.type.label("Тип"),
          Country.name.label("Страна"),
          City.name.label("Город")
        )
        .select_from(TypeBuilding)
        .join(Building)
        .join(City)
        .join(Country)
        .filter(
              Building.year >= 2000,
              Building.year <= 2018
          )
      )
    return [query_b.statement.columns.keys(), query_b.all()]