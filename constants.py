def get_kitchen_query_japan():
    sql = f"""SELECT name_food from Japanese_food"""
    return sql


def buttons_for_keyboard_japanese_kitchen_sql():
    sql = f"SELECT _id, name_food, description, ingredients from Japanese_food"
    return sql


def buttons_for_keyboard_european_kitchen_sql():
    sql = f"SELECT _id, name_food, description, ingredients from European_food"
    return sql


def sql_ingredients(name_food):
    sql = f"""SELECT description, ingredients FROM Japanese_food WHERE name_food == '{name_food}'
            UNION
            SELECT description, ingredients, city FROM Japanese_food WHERE name_food == '{name_food}'
            """
    return sql


def check_name_food_sql():
    sql = f"""SELECT name_food FROM Japanese_food
              UNION
              SELECT name_food FROM European_food
            """
    return sql


def sql_insert_photo():
    sql = '''UPDATE :table_name
        SET PICTURE = :picture
        WHERE name_food = :food_name;
        '''

    return sql
