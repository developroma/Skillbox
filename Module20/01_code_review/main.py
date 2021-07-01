students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def func(dictionary):
    lst = []
    string = ''
    for _, interests_and_surname in dictionary.items():
        lst += interests_and_surname['interests']
        string += interests_and_surname['surname']
    return lst, len(string)


for id, ages in students.items():
    pairs = []
    pairs += (id, ages['age'])
    print(pairs)

my_lst = func(students)[0]
my_lst_2 = func(students)[1]
print(f'{my_lst}\n{my_lst_2}')