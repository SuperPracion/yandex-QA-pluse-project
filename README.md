#### Прошу обратить внимание, что перед запуском - необходимо актуализировать URL вашего стенда. Сделать это необходимо в файле configuration.
#### Вставьте ссылку на ваш ресурс в значение URL_SERVICE="<СЮДА>".

| Имя файла | Назначение |
|-----|-----|
| configuration.py | Файл хранения оконечных ссылок и точек взаимодействия|
| create_orders.py | Хранит функцию для работы с заказами|
| data.py | Хранит шаблоны для запросов|
| sender_stand_request.py | Хранит функции обращающиеся к API|
| tests.py | Хранит тесты на проверку. **Вызвать именно его через pytest**|
| SQL-requests | Запросы к PostgreSQL с нытьём |
| result-of-testing | Информация о результате тестирования |
