# Структура проекта:
```                            
└─── tests                                      
    ├─── library                                  # общий пакет с базовым клиентом, клиентами ручек, данные, фикстуры запроса\ответа
    │   ├─── api                                  # основной пакет с базовым клиентом, клиентами ручек, данные 
    │   │   ├─── json_requests                    # пакет с телами запросов
    │   │   │   └─── item_requests.py             # модуль с телами запросов для item
    │   │   ├─── response_handlers                # пакет с хэндлерами для обработки ответа
    │   │   │   └─── response_handler.py          # модуль с хэндлерами для ответа
    │   │   ├─── response_schemas                 # пакет с json-схемами ответа
    │   │   │   └─── common_schemas.py            # модуль с общими схемами ответа
    │   │   │   └─── item_schemas.py              # модуль со схемами ответа для items
    │   │   │   └─── seller_id_item_schemas.py    # модуль со схемами ответа для seller_id
    │   │   │   └─── statistic_shemas.py          # модуль со схемами ответа для statistic
    │   │   ├─── services                         # пакет с клиентами для ручек
    │   │   │   └─── item_api.py
    │   │   │   └─── seller_id_item_api.py
    │   │   │   └─── statistic_api.py
    │   │   ├─── api_const.py                     # модуль с тестовыми контантами
    │   │   ├─── base_api_client.py               # описание базовых методов
    │   └─── fixtures                             # пакет с фикстурами
    │       └─── item_fixtures.py          
    ├─── tests                                    # пакет с тестами 
    │   ├─── item                                 # модуль с тестами ручки POST /api/1/item
    │   │   ├─── id                               # модуль с тестами ручки GET /api/1/item/:id
    │   ├─── sellerID                             # модуль с тестами ручки GET /api/1/:sellerID/item
    │   └─── statistic                            # модуль с тестами ручки GET /api/1/statistic/:id
    └─── requirements.txt                          # файл с зависимостями
```
=======
