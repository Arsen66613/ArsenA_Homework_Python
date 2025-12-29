# Lesson 08: Yougile API Tests


## Требования
- Python 3.14+
- pytest
- requests


### Структура проекта

08_lesson/
├─ api/ # Класс ProjectsApi для работы с API
├─ tests/ # Тесты для всех методов проекта
└─ conftest.py # Фикстуры: projects_api, created_project


#### Инструкция по получению токена

https://ru.yougile.com/api-v2#/


##### Настройка токена (Все токены и пароли вынесены в переменные окружения)

Windows:

-powershell
setx YOUGILE_TOKEN "ВАШ_ТОКЕН"

Linux/MacOS:

-bash 
export YOUGILE_TOKEN="ВАШ_ТОКЕН"


##### Запуск тестов

pytest lesson_08