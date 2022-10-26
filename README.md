<head> 
  <style>
   p {
    text-indent: 20px;
   }
  </style>
</head> 
<h1>Задание Monq Digital Lab</h1>
<br>
<img src = "https://mrselenium.com/wp-content/uploads/2020/02/seleniumlogo.png" height = "100">
<img src = "https://unipython.com/wp-content/uploads/2020/04/pytest-framework-min.png" height = "100">
<br>
<br>
<h2>Содержание</h2>
<ul>
 <li><a href="#description">Описание</a>
 <li><a href="#requirements">Предварительная установка библиотек</a>
 <li><a href="#start">Запуск кода</a>
 <li><a href="#bug_report">Оформленный баг-репорт и тест-кейс</a>
</ul>

<h2 id = description>Описание проекта</h2>
Автотест направлен на проверку возможности изменения имени в профиле участника. В качестве тестовой площадки выбран сайт clockify.me.
Авторизация и переход к настройкам профиля выполняется автоматически.
Задание выполнено с применением <code>pytest</code> и <code>selenium</code>.

<h2 id = requirements>Предварительная установка билиотек</h2>
Для начала работы следует установить pytest и Selenium
для этого в терминале IDE вбиваем команды:<br>
- <code>pip3 install pytest</code> и нажимаем клавишу <code>enter</code><br>
- <code>pip install selenium</code> и нажимаем клавишу <code>enter</code>.<br>
После каждого нажатия <code>enter</code> следует дождаться установки библиотек. Об окончании процесса установки будет свидетельствовать появление курсора ввода.

<h2 id = start>Запуск кода</h2>
Для начала работы автотеста открываем папку<code>tests</code> и далее открываем <code>test_auth.py</code> после чего в терминале прописываем команду <code>pytest -s -v</code>.

<h2 id = bug_report>Оформленный баг-репорт и тест-кейс</h2>
Ссылка на тест-кейс и баг-репорт https://docs.google.com/spreadsheets/d/15hA9__t8f83FjfiMZTG--BToHnZO7buTOdAGuDJSxVk/edit#gid=1052414719

