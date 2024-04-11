# 1. Написать функцию, которая принимает на вход список целых чисел и возвращает новый список, содержащий только уникальные элементы из исходного списка.

def unique(new_list):
    result = []
    for item in new_list:
        if not item in result:
            result.append(item)
    return result

# 2. Написать функцию, которая принимает на вход два целых числа (минимум и максимум) и возвращает список всех простых чисел в заданном диапазоне.
def range_func(min, max):
    return list(range(min, max + 1))

# 3. Создать класс Point, который представляет собой точку в двумерном пространстве. Класс должен иметь методы для инициализации координат точки, вычисления расстояния до другой точки, а также для получения и изменения координат.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_to(self, x2, y2):
        import math
        return math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2)
    
    def get_coords(self):
        return (self.x, self.y)
    
    def modify_coords(self, x, y):
        self.x = x
        self.y = y
        return (self.x, self.y)

# 4. Написать программу, которая сортирует список строк по длине, сначала по возрастанию, а затем по убыванию.
def sort(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    return result
    
def merge_sort(array):

    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    return sort(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))

def sort_choice(list, flag=None):
    if flag:
        return merge_sort(list)
    else:
        return merge_sort(list)[::-1]
        
list = [1,2,4,5,6,7,9]
print(sort_choice(list))
print(sort_choice(list, True))
