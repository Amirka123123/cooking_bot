import sqlite3

from constants import buttons_for_keyboard_japanese_kitchen_sql, sql_ingredients, check_name_food_sql, sql_insert_photo, \
    buttons_for_keyboard_european_kitchen_sql


def codes_for_utils(sql, params=()):
    conn = sqlite3.connect("kitchendatabasebot.db")
    cursor = conn.cursor()
    cursor.execute(sql, params)
    conn.commit()

    return cursor


def buttons_for_keyboard_japanese_kitchen():
    sql = buttons_for_keyboard_japanese_kitchen_sql()
    cursor = codes_for_utils(sql)
    data = cursor.fetchall()

    return data


def buttons_for_keyboard_european_kitchen():
    sql = buttons_for_keyboard_european_kitchen_sql()
    cursor = codes_for_utils(sql)
    data = cursor.fetchall()

    return data


def ingredients_for_foods(name_food):
    sql = sql_ingredients(name_food)
    cursor = codes_for_utils(sql)
    data = cursor.fetchone()

    return data


def check_name_food():
    sql = check_name_food_sql()
    cursor = codes_for_utils(sql)
    data = cursor.fetchall()
    data = [datum[0] for datum in data]
    return data


def insert_picture(file_name, name_food, table_name):
    sql = sql_insert_photo()
    picture = open(file_name, 'rb')
    ablob = picture.read()
    payload = {"table_name": table_name, "picture": ablob, "food_name": name_food}
    codes_for_utils(sql, payload)


def extract_picture(food_name):
    sql = """SELECT PICTURE FROM Japanese_food WHERE name_food = :name_food_
             UNION 
             SELECT PICTURE FROM European_food WHERE name_food = :name_food_
            """
    param = {'name_food_': food_name}
    cursor = codes_for_utils(sql, param)
    ablob = cursor.fetchone()

    return ablob


if __name__ == '__main__':

    # insert_picture('photos/download.jpeg', 'Sushi🍣')
    # insert_picture('photos/onigiri_39079_16x9.jpg', 'Onigiri🍙')
    # insert_picture('photos/ramen.jpg', 'Ramen 🍜')
    # insert_picture('photos/tempura.jpg', 'Tempura 🍤')
    # insert_picture('photos/yakitori.jpg', 'Yakitori🍢')

    insert_picture('photos_eu/images.jpeg', 'Eisbein🍖', 'European_food')
    insert_picture('photos_eu/Easiest-Pizza_22-2_11.jpg', 'Pizza🍕', 'European_food')
    insert_picture('photos_eu/Moules_frites.jpg', 'Moules frites🥘', 'European_food')
    insert_picture('photos_eu/Faves_a_la_Catalana.jpeg', 'Faves a la Catalana🧅', 'European_food')
    insert_picture('photos_eu/Fondue.jpg', 'Fondue🍵', 'European_food')