# здесь объявляются все необходимые классы
class Graph:
    def __init__(self, data):
        self.data = data[:]
        self.is_show = True

    def set_data(self, data):
        self.data = data[:]

    def _get_str_data(self):
        return " ".join(map(str, self.data))

    def _show_closed_graph(self):
        print("Отображение данных закрыто")

    def show_table(self):
        if self.is_show:
            print(self._get_str_data())
        else:
            self._show_closed_graph()

    def show_graph(self):
        if self.is_show:
            print(f"Графическое отображение данных: {self._get_str_data()}")
        else:
            self._show_closed_graph()

    def show_bar(self):
        if self.is_show:
            print(f"Столбчатая диаграмма: {self._get_str_data()}")
        else:
            self._show_closed_graph()

    def set_show(self, fl_show):
        self.is_show = fl_show


# считывание списка из входного потока (эту строку не менять)
data_graph = list(map(int, input().split()))

# здесь создаются объекты классов и вызываются нужные методы
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()
