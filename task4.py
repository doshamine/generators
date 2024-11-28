import types


def flat_generator(list_of_list):
    stack = [0] # стек хранит полный путь (в индексах) к текущему элементу списка

    while len(stack) > 0:  # получаем текущий список
        local_list = list_of_list
        for level in stack[:-1]:
            local_list = local_list[level]

        if stack[-1] >= len(local_list): # если текущий список закончился
            stack.pop(-1)
            if len(stack) > 0:
                stack[-1] += 1 # переходим к следующему
            continue

        index = stack[-1]
        if isinstance(local_list[index], list): # если элемент является списком
            stack.append(0) # заходим в список
            continue
        else:
            yield local_list[index] # иначе возвращаем элемент
            stack[-1] += 1


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
