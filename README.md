"# QA-trainee-assignment-winter-2025_Avdokushin" 
## Структура проекта:
```
├─── test_task_1                                  # папка с первым заданием
│    └─── BUGS.md                                 # баг-репорты задания 1  
│
│
└─── test_task_2_1                                # папка со вторым заданием
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
    ├── requirements.txt                          # файл с зависимостями
    │
    ├── BUGS.md                                   # баг-репорты задания 2.1   
    │
    └─── TESTCASES.md                             # тест-кейсы задания 2.1
```

### Инструкция по запуску тестов
## Требования
Python версии 3.8

## Быстрый старт
1. Склонируйте к себе репозиторий, в котором хранится проект тестового задания, через выполнение команды в терминале
    ```
    git clone https://github.com/Stasnislav121/QA-trainee-assignment-winter-2025_Avdokushin.git
    ```
    Или скачайте zip архив по [ссылке](https://github.com/Stasnislav121/QA-trainee-assignment-winter-2025_Avdokushin/archive/refs/heads/main.zip) и распакуйте его


2. Перейти в директорию склонированного проекта: `cd Avito_training\test_task_2_1`
3. Создать и активировать виртуальное окружение: 
   - `<venv>` заменить на путь до директории с виртуальным окружением
      - **Windows**: `python -m venv <venv> & <venv>\Scripts\activate`
      - **Linux**: `python -m venv <venv> && <venv>/bin/activate`
4. Установите необходимые зависимости из файла `requirements.txt`, выполнив команду  
   ```
   pip install -r requirements.txt
   ```
   если она не выполняется, то попробуйте
   ```
   pip3 install -r requirements.txt
   ```
5. Запустите тесты, выполнив команду: 
   ```
   pytest -v Avito_training\test_task_2_1
   ```
   Либо для запуска теста с формированием Allure-отчета: 
   ```
   pytest -v Avito_training\test_task_2_1 --alluredir allure-results
   ```
   Геренация Allure-отчета после прохождения тестов: 
   ```
   allure serve allure-results
   ```
=======
