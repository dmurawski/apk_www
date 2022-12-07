# Project Title

Projekt na zaliczenie


## Authors

- [@Damian Murawski](https://www.github.com/dmurawski)
- [@Daniel Nieznański](https://www.github.com/imhart)


## Endpointy
- `127.0.0.1:8000/swagger` - swagger
- `127.0.0.1:8000/` - bazowy url
- `127.0.0.1:8000/admin` - Panel Administracyjny 
- `127.0.0.1:8000/todolist` - Url bazowy do aplikacji
## Zadania
- `todolist/task/` - wyświetlanie zadań
- `todolist/task/title` - wyświetlanie zadań filtrowanie po tytule
- `todolist/task/list` - wyświetlanie zadań filtrowanie po nazwie listy
- `todolist/task/desc` - wyświetlanie zadań filtrowanie po opisie
- `todolist/task/add/` - dodawanie zadań
- `todolist/task/complete/` - wyświetlanie ukończonych zadań dla zalogowanego użytkownika
- `todolist/task/uncomplete/` - wyświetlanie nieukończonych zadań dla zalogowanego użytkownika
- `todolist/task/<int:pk>/` - wyświetlanie konkretnego zdania po id dla zalogowanego użytkownika
- `todolist/task/put/<int:pk>/` - aktualizacja danego zdania po id dla zalogowanego użytkownika
- `todolist/task/delete/<int:pk>/` - usunięcie danego zdania po id
## Lista
- `todolist/list/` - wyświetlanie list
- `todolist/list/name/` - wyświetlanie list i filtrowanie po nazwie
- `todolist/list/add/` - dodawanie listy
- `todolist/list/put/<int:pk>/` - aktualizacja danej listy
- `todolist/list/delete/<int:pk>/` - usuwanie danej listy
- `todolist/list/date/` - wyświetlanie list i filtrowanie po data utworzenia




## Running Tests
Aby uruchomić testy należy wpisać w konsole:

```bash
  python manage.py test ToDoList.tests
```

