Test API
=============

## Локальное развёртывание проекта ##

Для работы с проектам, пожалуйста **форкните его**.


Вам также потребуется установить следующие программы на свой компьютер:
- Docker
- Docker Compose


Как развернуть проект локально
=============================

#### Подготовка ####
1. Найдите в корне проекта файл `env_example`. Создайте новый файл`.env` и скопируйте в него содержимое файла `env_example`. Откройте его и измените значения переменных окружения, если потребуется.

2. Создайте файл `docker-compose.yml` и скопируйте в неё содержимое файла `docker-compose-example.yml`. Также измените номер порта `8050` на свой

#### Билд и запуск проекта ####
1.  Откройте в терминале директорию проекта и выполните команду:

    ```
    docker-compose build
    ```
2.  Запустите контейнеры командой:
    ```
    docker-compose up -d
    ```

>Выполнив последнюю команду, Вы можете столкнуться со следующей ошибкой:
  __"Cannot start container: port has already been allocated"__
Чтобы исправить эту проблему измените номер порта контейнера в файле ```docker-compese.yml```.

 Чтобы убедиться, что контейнеры запущены, выполните команду:

```
docker-compose ps
```
Если все контейнеры запущены, вы можете перейти к работе с Django.

```
docker-compose exec web python manage.py migrate
```
Данная команда выполняет миграцию моделей в Вашу БД.

#### Доступ к проекту ####
После успешного выполнения всех предыдущих действий Ваш проект будет доступен по **http://localhost:номер_порта**


Описание запросов
==================

#### Регистрация ###

Для регистрации пользователя необходимо сделать **POST**-запрос на эндпоинт:
```http
POST /register/
```

Тело запроса 

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `username` | `string` | **обязательно** |
| `password` | `string` | **обязательно** |
| `password_confirmation` | `string` | **обязательно** |
| `first_name` | `string` | необязательно |
| `last_name` | `string` | необязательно |

**Ответ**
```
Status code: 201
"Successfully created"
```

#### Авторизация ####

Для авторизации пользователя необходимо сделать **POST**-запрос на эндпоинт:
```http
POST /login/
```

Тело запроса 

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `username` | `string` | **обязательно** |
| `password` | `string` | **обязательно** |


**Ответ**
```
Status code: 201
{
  "id": 1,
  "username": "cooluser",
  "first_name": "Ivan",
  "last_name": "Pupkin",
  "token": "6ce5e4a1ec6876064c7fe16b68e61739ec88e31b"
}
```


#### Создание приложения ####

```http
POST /app/
```

Заголовки

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `Authorization` | `string` | токен **обязательно** |


Тело запроса 

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `APP_ID` | `integer` | **обязательно** |
| `name` | `string` | **обязательно** |
| `description` | `string` | необязательно |


**Ответ**
```
Status code: 201
{
  "APP_ID": 12344,
  "name": "Test app",
  "description": "",
  "API_KEY": "Me9C54TI2rz9iYD4k3mf5Mkb2FMUwxvG"
}
```

#### Изменение приложения ####

```http
PATCH /app/
```

Заголовки

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `Authorization` | `string` | токен **обязательно** |


Тело запроса 

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `APP_ID` | `integer` | необязательно |
| `name` | `string` | необязательно |
| `description` | `string` | необязательно |


**Ответ**
```
Status code: 200
{
  "APP_ID": 12344,
  "name": "Test app",
  "description": "",
  "API_KEY": "Me9C54TI2rz9iYD4k3mf5Mkb2FMUwxvG"
}
```

#### Удаление приложения ####

```http
DELETE /app/{id}/
```

Заголовки

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `Authorization` | `string` | токен **обязательно** |


Тело запроса 
`
нет
`


**Ответ**
```
Status code: 204

```

#### Изменение API_KEY ####

```http
POST /app/{id}/create_api_key/
```

Заголовки

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `Authorization` | `string` | токен **обязательно** |


Тело запроса 
`
нет
`


**Ответ**
```
Status code: 200

"daadaw2412FW1AD"
```

#### Получение информации о приложении ####

```http
GET /api/test/
```

Заголовки

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `Authorization` | `string` | токен **обязательно** |
| `API_KEY` | `string` | API_KEY **обязательно** |



**Ответ**
```
Status code: 200
{
  "APP_ID": 12344,
  "name": "Test app",
  "description": "",
  "API_KEY": "Me9C54TI2rz9iYD4k3mf5Mkb2FMUwxvG"
}
```
