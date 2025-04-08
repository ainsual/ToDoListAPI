*   **Создание задачи (Create Task):**
    *   Метод: POST
    *   URL: `/tasks/`
    *   Входные данные (Request Body - JSON):
        *   `title` (string, required): Заголовок задачи.
        *   `description` (string, optional): Описание задачи. Может быть пустым.
        *   `status` (boolean, optional, default=false): Статус задачи (выполнена или нет). По умолчанию `false` (не выполнена).
    *   Выходные данные (Response Body - JSON):
        *   `id` (integer): Уникальный идентификатор задачи.
        *   `title` (string): Заголовок задачи.
        *   `description` (string): Описание задачи.
        *   `status` (boolean): Статус задачи.
*   **Получение задачи (Get Task):**
    *   Метод: GET
    *   URL: `/tasks/{task_id}`
    *   Входные данные:
        *   `task_id` (integer, required): Идентификатор задачи.
    *   Выходные данные (Response Body - JSON):
        *   `id` (integer): Уникальный идентификатор задачи.
        *   `title` (string): Заголовок задачи.
        *   `description` (string): Описание задачи.
        *   `status` (boolean): Статус задачи.
    *   Обработка ошибок:
        *   Если задача с указанным `task_id` не найдена, возвращать HTTP-код 404 (Not Found) с информативным сообщением.
*   **Получение списка задач (Get All Tasks):**
    *   Метод: GET
    *   URL: `/tasks/`
    *   Входные данные:
        *   Нет.
    *   Выходные данные (Response Body - JSON):
        *   Список JSON-объектов, представляющих задачи (как описано в "Получение задачи").
*   **Редактирование задачи (Update Task):**
    *   Метод: PUT или PATCH (на ваш выбор)
    *   URL: `/tasks/{task_id}`
    *   Входные данные (Request Body - JSON):
        *   `title` (string, optional): Новый заголовок задачи.
        *   `description` (string, optional): Новое описание задачи.
        *   `status` (boolean, optional): Новый статус задачи.
    *   Выходные данные (Response Body - JSON):
        *   `id` (integer): Уникальный идентификатор задачи.
        *   `title` (string): Обновленный заголовок задачи.
        *   `description` (string): Обновленное описание задачи.
        *   `status` (boolean): Обновленный статус задачи.
    *   Обработка ошибок:
        *   Если задача с указанным `task_id` не найдена, возвращать HTTP-код 404 (Not Found).
*   **Удаление задачи (Delete Task):**
    *   Метод: DELETE
    *   URL: `/tasks/{task_id}`
    *   Входные данные:
        *   `task_id` (integer, required): Идентификатор задачи.
    *   Выходные данные (Response Body - JSON):
        *   `{"message": "Task deleted successfully"}` (или аналогичное сообщение об успехе).
    *   Обработка ошибок:
        *   Если задача с указанным `task_id` не найдена, возвращать HTTP-код 404 (Not Found).