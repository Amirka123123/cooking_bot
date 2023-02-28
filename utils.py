import sqlite3

from constants import buttons_for_keyboard_japanese_kitchen_sql


def buttons_for_keyboard_japanese_kitchen(id_, food_name, description, ingredients):
    sql = buttons_for_keyboard_japanese_kitchen_sql(id_, food_name, description, ingredients)

    conn = sqlite3.connect("kitchendatabasebot.db")
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

    data = cursor.fetchone()
    id_ = data[0]
    food_name = data[1]
    description = data[2]
    ingredients = data[3]

    return id_, food_name, description, ingredients
