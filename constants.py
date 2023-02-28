def get_kitchen_query_japan():
    sql = f"""SELECT name_food from Japanese_food"""
    return sql


def buttons_for_keyboard_japanese_kitchen_sql(id_, food_name, description, ingredients):
    sql = f"SELECT id_, food_name, description, ingredients from Japanese_food " \
          f"WHERE id_ = {id_}, food_name = {food_name}, description = {description}, ingredients = {ingredients}"
