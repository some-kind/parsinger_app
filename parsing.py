class Measure:
    """
    Измерение ресурса
    """
    def __init__(self, name: str):
        """
        Init
        :param name: Имя ресурса, его тип
        """
        self._type = name
        self._measures = []  # все заменры данного измерения
        self._average = None  # среднее значение
        self._median = None  # медиана
        self._usage_type = None  # тип использования
        self._intensity = None  # интенсивность

    @property
    def type(self):
        return self._type

    def add_meas(self, number: int):
        """
        Добавить замеры к списку измерений
        :param number: замер
        :return:
        """
        self._measures.append(number)

    def calculate_average(self):
        """
        Вычислить среднее значение измерения
        :return:
        """
        self._average = sum(self._measures) / len(self._measures)

    def calculate_median(self):
        """
        Вычислить медиану
        :return:
        """
        if len(self._measures) % 2 == 1:
            self._median = self._measures[(len(self._measures) // 2)]
        else:
            self._median = ((self._measures[len(self._measures) // 2 - 1] + self._measures[(len(self._measures) // 2)]) / 2)
        if self._median == 0:
            self._median += 1

    def calculate_usage_type(self):
        """
        Определить тип использования
        :return:
        """
        procent = self._average / self._median
        if procent < 0.75:
            self._usage_type = "снижения"
        elif procent > 1.25:
            self._usage_type = "скачки"
        else:
            self._usage_type = "стабильная"

    def calculate_intensity(self):
        """
        Определить интенсивность
        :return:
        """
        if self._median <= 30:
            self._intensity = "низкая"
        elif self._median <= 60:
            self._intensity = "средняя"
        elif self._median <= 90:
            self._intensity = "высокая"
        else:
            self._intensity = "запредельная"

    def get_measure_data(self):
        """
        Получить данные в виде требуемого словаря
        :return: словарь данных об измерении
        """
        return {self._type:
                    {
                        "mean": round(self._average, 2),
                        "mediana": round(self._median, 2),
                        "usage_type": self._usage_type,
                        "intensity": self._intensity
                    }
                }


class Resource:
    """
    Ресурс
    """
    def __init__(self, res_id: str):
        """
        Init
        :param res_id: ID ресурса
        """
        self._res_id = res_id
        self._measures = {}  # словарь, содержащий информацию о измерениях

    @property
    def res_id(self):
        return self._res_id

    def add_measure(self, measure):
        """
        Добавить измерение к ресурсу
        :param measure: Сведения об измерении
        :return:
        """
        self._measures.update(measure)

    def get_resource_data(self):
        """
        Получить сведения о ресурсе в виде словаря
        :return: словарь данных
        """
        return {self._res_id: self._measures}


class Command:
    def __init__(self, name: str):
        self._name = name
        self._resources = {}

    @property
    def command_name(self):
        return self._name

    def add_resource(self, resource):
        """
        Добавить данные ресурса
        :param resource: Данные ресурса
        :return:
        """
        self._resources.update(resource)

    def get_command_data(self):
        """
        Получить данные команды в виде словаря
        :return: словарь данных
        """
        return {self._name: self._resources}