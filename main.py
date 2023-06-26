import seed
import my_select
from database.models import Teacher, Student, Discipline, Grade, Group
from database.db import session

import pprint


def count_records(table_name):
    max_id = session.query(table_name).order_by(table_name.id.desc()).first()
    count = max_id.id if max_id else 0
    return count


def execute_query(num: int, *args) -> list:
    function_mapping = {
        1: my_select.select_1,
        2: my_select.select_2,
        3: my_select.select_3,
        4: my_select.select_4,
        5: my_select.select_5,
        6: my_select.select_6,
        7: my_select.select_7,
        8: my_select.select_8,
        9: my_select.select_9,
        10: my_select.select_10,
        11: my_select.select_11,
        12: my_select.select_12
    }
    selected_function = function_mapping.get(num)
    return selected_function(*args)


def input_number(start: int, stop: int) -> int:
    while True:
        answer = input(">>>")
        try:
            int_ans = int(answer)
        except ValueError:
            print("Невірно введена команда")
            continue
        if int_ans not in range(start, stop + 1):
            print("Невірний номер")
            continue
        return int_ans


def main():
    q_sub = count_records(Discipline)
    q_gr = count_records(Group)
    q_teach = count_records(Teacher)
    q_stud = count_records(Student)

    with open("README.md", "r", encoding="UTF-8") as hf:
        help_str = hf.read()

    print(help_str)
    while True:
        print("Зробіть ваш вибір")
        answer = input_number(0, 14)
        if answer == 14:
            print(help_str)
        elif answer == 13:
            print("До побачення!")
            break
        elif answer == 0:
            seed.fill_db()
        elif 13 > answer > 0:
            if answer == 2 or answer == 3:
                print(f"Введіть № предмета 1-{q_sub}")
                n_subj = input_number(1, q_sub)
                pprint.pprint(execute_query(answer, n_subj))
            elif answer == 5:
                print(f"Введіть № викладача 1-{q_teach}")
                n_teach = input_number(1, q_teach)
                pprint.pprint(execute_query(answer, n_teach))
            elif answer == 6:
                print(f"Введіть № групи 1-{q_gr}")
                n_gr = input_number(1, q_gr)
                pprint.pprint(execute_query(answer, n_gr))
            elif answer == 7:
                print(f"Введіть № предмета 1-{q_sub}")
                n_subj = input_number(1, q_sub)
                print(f"Введіть № групи 1-{q_gr}")
                n_gr = input_number(1, q_gr)
                pprint.pprint(execute_query(answer, n_subj, n_gr))
            elif answer == 8:
                print(f"Введіть № викладача 1-{q_teach}")
                n_teach = input_number(1, q_teach)
                pprint.pprint(execute_query(answer, n_teach))    
            elif answer == 9:
                print(f"Введіть № студента 1-{q_stud}")
                n_st = input_number(1, q_stud)
                pprint.pprint(execute_query(answer, n_st))
            elif answer == 10 or answer == 11:
                print(f"Введіть № студента 1-{q_stud}")
                n_st = input_number(1, q_stud)
                print(f"Введіть № викладача 1-{q_teach}")
                n_teach = input_number(1, q_teach)
                pprint.pprint(execute_query(answer, n_st, n_teach))
            elif answer == 12:
                print(f"Введіть № групи 1-{q_gr}")
                n_gr = input_number(1, q_gr)
                print(f"Введіть № предмета 1-{q_sub}")
                n_subj = input_number(1, q_sub)
                pprint.pprint(execute_query(answer, n_gr, n_subj))
            else:
                pprint.pprint(execute_query(answer))


if __name__ == "__main__":
    main()
