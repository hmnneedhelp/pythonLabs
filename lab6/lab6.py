def process_lists(lists):
    merged_list = sum(lists, [])
    unique_list = list(set(merged_list))
    sorted_list = sorted(unique_list)
    sort_choice = input("Желаете отсортировать список? (да/нет): ")
    if sort_choice.lower() == 'да':
        print("Результат после объединения, удаления повторяющихся значений и сортировки:")
        print(sorted_list)
    else :
        print("Результат после объединения, удаления повторяющихся значений:")
        print(unique_list)

        
def input_lists():
    lists = []
    for i in range(3):
        list_input = input(f"Введите список {i+1} целых чисел через пробел: ")
        int_list = list(map(int, list_input.split()))
        lists.append(int_list)
    return lists

lists = input_lists()
result = process_lists(lists)

