import requests

from parsing import Command
from parsing import Resource
from parsing import Measure


def parsing(log: str):
    """
    Parsing logs to dict
    :param log: logs string
    :return: parsed dictionary
    """
    parsed_data = {}
    for command in log.split("$"):

        resources = command.split("|")[-1]

        example_res_id = resources.split(";")[0].strip("()").split(",")[0]
        example_mes_type = resources.split(";")[0].strip("()").split(",")[1]

        one_command = Command(command.split("|")[0])
        one_resource = Resource(example_res_id)
        one_measure = Measure(example_mes_type)

        for resource in resources.split(";"):
            resource = resource.strip("()").split(",")
            # разложение на составляющие скобок
            res_id = resource[0]
            mes_type = resource[1]
            # datetime = resources[2]
            load = int(resource[3])
            if res_id == example_res_id:
                if mes_type == example_mes_type:
                    # добавляем измерение
                    one_measure.add_meas(load)
                else:
                    # рассчёт всех параметров и передача их в ресурс
                    one_measure.calculate_average()
                    one_measure.calculate_median()
                    one_measure.calculate_usage_type()
                    one_measure.calculate_intensity()
                    one_resource.add_measure(one_measure.get_measure_data())
                    # пересоздание обхекта измерения и переназначение примера
                    one_measure = Measure(mes_type)
                    example_mes_type = mes_type
            else:
                # рассчёт всех параметров и передача их в ресурс
                one_measure.calculate_average()
                one_measure.calculate_median()
                one_measure.calculate_usage_type()
                one_measure.calculate_intensity()
                one_resource.add_measure(one_measure.get_measure_data())
                # пересоздание обхекта измерения и переназначение примера
                one_measure = Measure(mes_type)
                example_mes_type = mes_type
                # запись ресурса в команду
                one_command.add_resource(one_resource.get_resource_data())
                # пересоздание объекта и переназначение примера
                one_resource = Resource(res_id)
                example_res_id = res_id

        parsed_data.update(one_command.get_command_data())
    return parsed_data


def report_to_file(dict_data: dict):
    for command in dict_data:
        with open(f"results/{command}.txt", "w") as file:
            file.write("  Ресурс  |"
                       " Измерение |"
                       " Среднее значение |"
                       " Медиана |"
                       " Тип использования |"
                       " Интенсивность |"
                       " Решение \n\n")
            len_res = 10
            len_mes = 11
            len_ave = 18
            len_med = 9
            len_type = 19
            len_int = 15
            for resource in dict_data[f"{command}"]:
                for measure in dict_data[f"{command}"][f"{resource}"]:
                    data = dict_data[f"{command}"][f"{resource}"][f"{measure}"]
                    decision = None
                    if data["intensity"] == "низкая":
                            decision = "Отказ от ресурса"
                    elif data["intensity"] == "средняя":
                        if data["usage_type"] == "снижения":
                            decision = "Отказ от ресурса"
                        else:
                            decision = "Ресурс без изменений"
                    elif data["intensity"] == "высокая":
                        if data["usage_type"] == "скачки":
                            decision = "Ресурс необходимо усилить"
                        else:
                            decision = "Ресурс без изменений"
                    elif data["intensity"] == "запредельная":
                            decision = "Ресурс необходимо усилить"

                    file.write(f" {resource}" + (" " * (len_res - len(resource) - 1)) + "|" +
                               f" {measure}" + (" " * (len_mes - len(measure) - 1)) + "|" +
                               f" {data["mean"]}" + (" " * (len_ave - len(str(data["mean"])) - 1)) + "|" +
                               f" {data["mediana"]}" + (" " * (len_med - len(str(data["mediana"])) - 1)) + "|" +
                               f" {data["usage_type"]}" + (" " * (len_type - len(data["usage_type"]) - 1)) + "|" +
                               f" {data["intensity"]}" + (" " * (len_int - len(data["intensity"]) - 1)) + "|" +
                               f" {decision}\n")


def main():
    logs_number = input("Введите число: ")
    try:
        log = requests.get(url="http://127.0.0.1:21122/monitoring/infrastructure/using/summary/" + logs_number)
        parsed_data = parsing(log.text)
        report_to_file(parsed_data)
    except requests.ConnectTimeout:
        print("Приложение недоступно, запустите monitoring_module.py")


if __name__ == '__main__':
    main()
