from config import db
from models import Building, Country, City, TypeBuilding
from sqlalchemy import func
import csv 

result_func_typeBuilding = (db.session.query(
 func.max(Building.height).label("Максимальная высота"),
 func.min(Building.height).label("Минимальная высота"),
 func.avg(Building.height).label("Средняя высота"),
 TypeBuilding.type.label("Страна")
 )
 .select_from(TypeBuilding)
 .join(TypeBuilding)
 .group_by(TypeBuilding.id)
 .all()
)