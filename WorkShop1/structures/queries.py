from config import db
from models import Building, Country, City, TypeBuilding
from sqlalchemy import func, desc
import csv 

result_all_table = (db.session.query(
 Building.title.label("Здание"),
 TypeBuilding.type.label("Тип"),
 Country.name.label("Страна"),
 City.name.label("Город"),
 Building.year.label("Год"),
 Building.height.label("Высота")
 )
 .select_from(Building)
 .join(City)
 .join(Country)
 .join(TypeBuilding)
 .order_by(Building.height.desc()) 
 .all()
)
#print(result)

print (f"Здание |  Тип  |  Страна  |  Город  |  Год  |  Высота")
print (f"-------------------------------------------------------------------------------")
for title, type, name_count, name_city, year, height in result_all_table:
    print(f"{title} | {type} | {name_count} | {name_city} | {year} | {height}")
    print (f"-------------------------------------------------------------------------------")

print (f"-------------------------------------------------------------------------------")
print (f"|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print (f"-------------------------------------------------------------------------------")
print (f"-------------------------------------------------------------------------------")

result_func_country = (db.session.query(
 func.max(Building.height).label("Максимальная высота"),
 func.min(Building.height).label("Минимальная высота"),
 func.avg(Building.height).label("Средняя высота"),
 Country.name.label("Страна")
 )
 .select_from(Building)
 .join(City)
 .join(Country)
 .group_by(Country.name)
 .order_by(Country.name.asc())
 .all()
)


print (f"Мин высота |  Макс высота  |  Сред высота  |  Страна")
print (f"-------------------------------------------------------------------------------")
for build_max, build_min, build_avg, name in result_func_country:
    print(f"{build_max} | {build_min} | {build_avg} | {name}")
    print (f"-------------------------------------------------------------------------------")

print (f"-------------------------------------------------------------------------------")
print (f"|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print (f"-------------------------------------------------------------------------------")
print (f"-------------------------------------------------------------------------------")

result_func_year = (db.session.query(
 func.max(Building.height).label("Максимальная высота"),
 func.min(Building.height).label("Минимальная высота"),
 func.avg(Building.height).label("Средняя высота"),
 Building.year.label("Год")
 )
 .select_from(Building)
 .group_by(Building.year)
 .order_by(Building.year.asc())
 .all()
)

print (f"Мин высота |  Макс высота  |  Сред высота  |  Год")
print (f"-------------------------------------------------------------------------------")
for build_max, build_min, build_avg, year in result_func_year:
    print(f"{build_max} | {build_min} | {build_avg} | {year}")
    print (f"-------------------------------------------------------------------------------")

print (f"-------------------------------------------------------------------------------")
print (f"|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print (f"-------------------------------------------------------------------------------")
print (f"-------------------------------------------------------------------------------")

result_func_type = (db.session.query(
 func.max(Building.height).label("Максимальная высота"),
 func.min(Building.height).label("Минимальная высота"),
 func.avg(Building.height).label("Средняя высота"),
 TypeBuilding.type.label("Тип")
 )
 .select_from(Building)
 .join(City)
 .join(Country)
 .join(TypeBuilding)
 .filter(TypeBuilding.type.contains("мачта")) 
 .group_by(TypeBuilding.type)
 .order_by(desc("Средняя высота"))
 .all()
)

print (f"Мин высота |  Макс высота  |  Сред высота  |  Тип")
print (f"-------------------------------------------------------------------------------")
for build_max, build_min, build_avg, type in result_func_type:
    print(f"{build_max} | {build_min} | {build_avg} | {type}")
    print (f"-------------------------------------------------------------------------------")

print (f"-------------------------------------------------------------------------------")
print (f"|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print (f"-------------------------------------------------------------------------------")

result_func_count_building = (db.session.query(
 func.max(Building.height).label("Максимальная высота"),
 func.min(Building.height).label("Минимальная высота"),
 func.avg(Building.height).label("Средняя высота"),
 func.count(Building.title).label("Количество зданий"),
 Country.name.label("Страна")
 )
 .select_from(Building)
 .join(City)
 .join(Country)
 .join(TypeBuilding)
 .group_by(Country.name)
 .having(func.count(Building.title) > 1)
 .all()
)

print (f"Мин высота |  Макс высота  |  Сред высота  |  Кол-во зданий  |  Страна")
print (f"-------------------------------------------------------------------------------")
for build_max, build_min, build_avg, count_build, name in result_func_count_building:
    print(f"{build_max} | {build_min} | {build_avg} | {count_build} | {name}")
    print (f"-------------------------------------------------------------------------------")

print (f"-------------------------------------------------------------------------------")
print (f"|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print (f"-------------------------------------------------------------------------------")


