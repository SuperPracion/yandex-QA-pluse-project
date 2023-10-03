import configuration
import requests

#создание заказа
def post_create_order(body):
    """
    возвращает ответ в виде:\n
    HTTP/1.1 201 Created {track: 124124}
    """
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)
    
def get_info_about_order(track):
    """
    возвращает информацию по заказу основываясь на переданном номере
    """
    
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_INFO +
                        f"?t={track}")
    