# Project Title

Projekt na zaliczenie


## Authors

- [@Damian Murawski](https://www.github.com/dmurawski)
- [@Daniel Nieznański](https://www.github.com/imhart)


## Endpointy
- @127.0.0.1:8000/ - bazowy url
- 127.0.0.1:8000/admin - Panel Administracyjny 
- 127.0.0.1:8000/todolist - Url bazowy do aplikacji
- todolist/ task/ [name='task'] - wyświetlanie zadań
- todolist/ task/add/ [name='task_post'] - dodawanie zadań
- todolist/ task/complete/ [name='task_list_complete'] - wyświetlanie ukończonych zadań dla zalogowanego użytkownika
- todolist/ task/uncomplete/ [name='task_list_uncomplete'] - wyświetlanie nieukończonych zadań dla zalogowanego użytkownika
- todolist/ task/<int:pk>/ [name='task_detail'] - wyświetlanie konkretnego zdania po id dla zalogowanego użytkownika
- todolist/ task/put/<int:pk>/ [name='task_update'] - aktualizacja danego zdania po id dla zalogowanego użytkownika
- todolist/ task/delete/<int:pk>/ [name='task_delete'] - usunięcie danego zdania po id



## Running Tests
Aby uruchomić testy należy wpisać w konsole:

```bash
  python manage.py test ToDoList.tests
```

