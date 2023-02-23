# https://app.betrybe.com/learn/course/5e938f69-6e32-43b3-9685-c936530fd326/module/290e715d-73e3-4b2d-a3c7-4fe113474070/section/73f2a1d5-7d77-440b-a9f2-3ea9750db228/day/346e18ae-25d8-47a5-bd59-0e4d9cd2a2d2/lesson/9b22b10c-1e8a-4f00-bab8-edac69573b6b

# function quick_sort retirada do course

def quick_sort(strings, start, end):
    if start < end:
        p = partition(strings, start, end)
        quick_sort(strings, start, p - 1)
        quick_sort(strings, p + 1, end)


def partition(strings, start, end):
    pivot = strings[end]
    delimiter = start - 1

    for i in range(start, end):
        if strings[i] <= pivot:
            delimiter = delimiter + 1
            strings[i], strings[delimiter] = strings[delimiter], strings[i]

    strings[delimiter + 1], strings[end] = strings[end], strings[delimiter + 1]

    return delimiter + 1


def is_anagram(first_string, second_string):
    string_one = list(first_string.lower())
    string_two = list(second_string.lower())

    quick_sort(string_one, 0, len(string_one) - 1)
    quick_sort(string_two, 0, len(string_two) - 1)

    if first_string == '' or second_string == '':
        return (''.join(string_one), ''.join(string_two), False)
    return (
        ''.join(string_one),
        ''.join(string_two),
        ''.join(string_one) == ''.join(string_two))
