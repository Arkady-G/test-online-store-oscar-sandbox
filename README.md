## Тестирование проект online store Oscar Sandbox

### Запуск автотестов для разных языков интерфейса.
1. Для запуска автотеста необходимо установить библиотеку pytest-selenium
2. В файл conftest.py добавлен обработчик, который считывает из командной строки параметр language.
3. В файле conftest.py реализована логика запуска браузера с указанным языком пользователя.
4. Браузер объявлен в фикстуре browser и передается в тест как параметр.
5. Код работает только для браузера Сhrome.
6. По умолчанию установлен язык браузера - en .
7. Импорт из папки pages без точки! Например - from pages.main_page import MainPage (вместо from .pages.main_page import MainPage)
