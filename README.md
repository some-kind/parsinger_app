This program parses logs from the input in a certain form and outputs them to report files

The monitoring file (monitoring_module.py) simulates the receipt of logs in a certain form.
For this simulator to work, you need to install dependencies with the command "pip3 install -r requirements.txt"
Then run the module with the command "python3 monitoring_module.py"

In the directory with the program, you need to create a "results" folder in which report files will be generated.

The reports have the following structure:
- the file name is the command
- next, the file is a table of the name (ID) of the resource, measuring its impact on a particular system and conclusions about what to do with this process.

To transfer these logs to the program, use the command "curl localhost:21122/monitoring/infrastructure/using/summary/1 | python3 app.py"
The number at the end can be changed to get different results.

#######  RUSSIAN  ########

Эта программа анализирует логи из входных данных в определенной форме и выводит их в файлы отчетов

Файл мониторинга (monitoring_module.py) имитирует получение логов в определенной форме.
Чтобы этот симулятор заработал, вам нужно установить зависимости командой "pip3 install -r requirements.txt"
Затем запустить модуль командой "python3 monitoring_module.py"

В каталоге с программой вам нужно создать папку "results", в которой будут сгенерированы файлы отчетов.

Отчеты имеют следующую структуру:
- имя файла - это команда
- далее файл представляет собой таблицу с названием (ID) ресурса, измеряющую его влияние на конкретную систему и выводы о том, что делать с этим процессом.

Чтобы перенести эти логи в программу, используйте команду "curl localhost:21122/monitoring/infrastructure/using/summary/1 | python3 app.py"
Число в конце можно изменить, чтобы получить другие результаты.


---------------------------------------------------------------------------------------------------------------
Данная программа создана как решение задачи в ходе изучения программирования на Python

