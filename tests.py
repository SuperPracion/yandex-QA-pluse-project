import sender_stand_request
import create_orders

# Мария Иванова, 1-я когорта — Финальный проект. Инженер по тестированию плюс
# Шутка
# Ахметов Тимур, 9-я когорта — Финальный проект. Инженер по тестированию плюс

def test_check_create_order():
    pattern = create_orders.create_order()
    response = sender_stand_request.post_create_order(pattern)
    
    assert sender_stand_request.get_info_about_order(response.json()['track']).status_code == 200

#вызов функции проверки трекера в базе
test_check_create_order()