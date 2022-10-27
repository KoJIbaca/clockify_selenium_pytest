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
 <li><a href="#environment">Настройка окружения</a>
 <li><a href="#start">Запуск кода</a>
 <li><a href="#bug_report">Оформленный баг-репорт и тест-кейс</a>
</ul>

<h2 id = description>Описание проекта</h2>
<p style="text-indent: 20px;">Автотест направлен на проверку возможности изменения имени в профиле участника.
В качестве тестовой площадки выбран сайт clockify.me.
Авторизация и переход к настройкам профиля выполняется автоматически.
Задание выполнено с применением <code>pytest</code> и <code>selenium</code>.</p>

<h2 id = requirements>Предварительная установка билиотек</h2>
<p style="text-indent: 20px;"> Для начала работы следует установить pytest, библиотеку requests и Selenium
для этого в терминале IDE вбиваем команды:<br>
- <code>pip3 install pytest</code> и нажимаем клавишу <code>enter</code><br>
- <code>pip install selenium</code> и нажимаем клавишу <code>enter</code>.<br>
- <code>pip3 install requests</code> и нажимаем клавишу <code>enter</code><br>
После каждого нажатия <code>enter</code> следует дождаться установки библиотек.
Об окончании процесса установки будет свидетельствовать появление курсора ввода.</p>

<h2 id = environment>Настройка окружения</h2>
<p style="text-indent: 20px;">Перед запуском кода следует настроить перменные среды прописать электронную почту учетной записи и пароль от нее.
Переменные принимают следующий вид: EMAIL = 'email', PASSWORD = 'pwd', где вместо email указываете почту, а вместо pwd - пароль.
В случае если этого не сделать - тест "рухнет" с сообщением в терминале ввести переменные.</p>

<h2 id = start>Запуск кода</h2>
<p style="text-indent: 20px;"> Для начала работы автотеста открываем папку<code>tests</code> и далее открываем <code>test_auth.py</code> после чего в терминале прописываем команду <code>cd tests</code>.
Как только в терминале произойдет переход в папку tests прописываем в терминале <code>pytest -s -v</code>.
Начнется выполнение кода и запустится браузер, далее (по завершению исполнения кода) он закроется - тест завершился.
Информация о пройденных тестах появится в терминале IDE.</p>

<h2 id = bug_report>Оформленный баг-репорт и тест-кейс</h2>
Ссылка на тест-кейс и баг-репорт https://docs.google.com/spreadsheets/d/15hA9__t8f83FjfiMZTG--BToHnZO7buTOdAGuDJSxVk/edit#gid=1052414719

