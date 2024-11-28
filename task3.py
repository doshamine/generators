class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.stack = [0] # стек хранит полный путь (в индексах) к текущему элементу списка
        return self

    def __next__(self):
        while len(self.stack) > 0: # получаем текущий список
            local_list = self.list_of_list
            for level in self.stack[:-1]:
                local_list = local_list[level]

            if self.stack[-1] >= len(local_list): # если текущий список закончился
                self.stack.pop(-1)
                if len(self.stack) > 0:
                    self.stack[-1] += 1 # переходим к следующему
                continue

            index = self.stack[-1]
            if isinstance(local_list[index], list): # если элемент является списком
                self.stack.append(0) # заходим в список
                continue
            else:
                self.stack[-1] += 1
                return local_list[index] # иначе возвращаем элемент

        raise StopIteration




def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()