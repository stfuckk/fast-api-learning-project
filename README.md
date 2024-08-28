# fast-api-learning-project
 
# Подготовка проекта

- Установите нужные пакеты:

   ```python
   pip install -r requirements.txt
   ```
- Подготовьте СУБД (например, PostgreSQL) и создайте БД и пользователя с правами на эту БД
- Создайте .env файл в корне проекта и заполните в нем переменные окружения для защиты от посторонних глаз, ориентируясь на следующий пример:

    ```python
    DATABASE_URL="postgresql://login:password@ip-or-localhost/bdname"
    SECRET_KEY="your-secret-key"
    ```

# Запуск

- Перейдите по следующему пути находясь в корне проекта:

   ```python
   cd .\src
   ```
- Запустите FastAPI приложение:

   ```python
   uvicorn main:app --reload
   ```

> Запуск также можно произвести, создав виртуальное окружение venv и установив пакеты в нем:
> 
>  ```python
>  python -m venv venv
>  ```
>
> Запустить скрипт:
>
> ```
> venv\Scripts\activate.bat - для Windows
> source venv/bin/activate - для Linux и MacOS
> ```
>
> Приглашение оболчки изменится и появится (venv) - это значит, что мы находимся внутри виртуального окружения.
> 
> Далее выполняем установку пакетов python
> ```
> pip install -r requirements.txt
> ```
>
> и запускаем приложение находясь в .\src
>
> ```python
> uvicorn main:app
> ```
   
    