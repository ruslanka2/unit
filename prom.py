import pytest
from list_comparator import ListComparator
class ListComparator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def calculate_average(self, lst):
        if len(lst) == 0:
            return 0
        return sum(lst) / len(lst)

    def compare_lists(self):
        avg1 = self.calculate_average(self.list1)
        avg2 = self.calculate_average(self.list2)

        if avg1 > avg2:
            return "Первый список имеет большее среднее значение"
        elif avg1 < avg2:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"
        


def test_compare_lists():
    # Тест с разными средними значениями
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    comparator = ListComparator(list1, list2)
    assert comparator.compare_lists() == "Второй список имеет большее среднее значение"

    # Тест с одинаковыми средними значениями
    list1 = [1, 2, 3]
    list2 = [4, 5, 6, 7]
    comparator = ListComparator(list1, list2)
    assert comparator.compare_lists() == "Средние значения равны"

    # Тест с пустыми списками
    list1 = []
    list2 = []
    comparator = ListComparator(list1, list2)
    assert comparator.compare_lists() == "Средние значения равны"
