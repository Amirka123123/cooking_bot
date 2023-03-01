import sqlite3

from constants import buttons_for_keyboard_japanese_kitchen_sql, sql_ingredients, check_name_food_sql


def codes_for_utils(sql):
    conn = sqlite3.connect("kitchendatabasebot.db")
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

    return cursor


def buttons_for_keyboard_japanese_kitchen():
    sql = buttons_for_keyboard_japanese_kitchen_sql()
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

if __name__ == '__main__':
    print('Sushi🍣' in check_name_food())