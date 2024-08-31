# fast-api-learning-project
 
# Подготовка проекта

- Установите Poetry, если он еще не установлен:
    ```bash
    # cmd (linux, macos, windows)
    curl -sSL https://install.python-poetry.org | python3 -
    # pwsh
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
    
    # не забудьте добавить в path - смотреть документацию
    # https://python-poetry.org/docs/#installing-with-the-official-installer
    ```
- Создайте виртуальное окружение и установите зависимости:

   ```bash
   poetry install
   ```
- Подготовьте СУБД (например, PostgreSQL) и создайте БД и пользователя с правами на эту БД
- Создайте .env файл в корне проекта и заполните в нем переменные окружения для защиты от посторонних глаз, ориентируясь на следующий пример:

    ```python
    DATABASE_URL="postgresql://login:password@ip-or-localhost/bdname"
    SECRET_KEY="your-secret-key"
    ```

# Запуск

- Перейдите в папку с кодом проекта:

   ```bash
   cd .\src
   ```
- Запустите FastAPI приложение:

   ```bash
   poetry run uvicorn main:app --reload
   ```
    