## Тестирование проект online store Oscar Sandbox

### Запуск автотестов для разных языков интерфейса.
1. Для запуска автотеста необходимо установить библиотеку pytest-selenium
2. В файл conftest.py добавлен обработчик, который считывает из командной строки параметр language.
3. В файле conftest.py реализована логика запуска браузера с указанным языком пользователя.
4. Браузер объявлен в фикстуре browser и передается в тест как параметр.
5. Проверяется страница товара, доступная по http://selenium1py.pythonanywhere.com/
6. Тест запускается из консоли с параметром language следующей командой: pytest -v --tb=line --language=en test_main_page.py
7. Код работает только для браузера Сhrome.
8. По умолчанию установлен язык браузера - en .
