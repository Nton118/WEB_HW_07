import sqlite3
import init_db
import pprint


def execute_query(sql: str, *args) -> list:
    with sqlite3.connect("MyDB.sqlite") as con:
        cur = con.cursor()
        cur.execute(sql, args)
        return cur.fetchall()


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
            init_db.init_db()
        elif 13 > answer > 0:
            filename = f"query_{answer}.sql"
            with open(filename, "r") as f:
                sql = f.read()
                if answer == 2 or answer == 3:
                    print("Введить № предмета 1-9")
                    n_subj = input_number(1, 9)
                    pprint.pprint(execute_query(sql, n_subj))
                elif answer == 5:
                    print("ВВедіть № викладача 1-6")
                    n_teach = input_number(1, 6)
                    pprint.pprint(execute_query(sql, n_teach))
                elif answer == 6:
                    print("ВВедіть № группи 1-4")
                    n_gr = input_number(1, 4)
                    pprint.pprint(execute_query(sql, n_gr))
                elif answer == 7:
                    print("Введить № предмета 1-9")
                    n_subj = input_number(1, 9)
                    print("ВВедіть № группи 1-4")
                    n_gr = input_number(1, 4)
                    pprint.pprint(execute_query(sql, n_subj, n_gr))
                elif answer == 9:
                    print("ВВедіть № студента 1-50")
                    n_st = input_number(1, 50)
                    pprint.pprint(execute_query(sql, n_st))
                elif answer == 10 or answer == 11:
                    print("ВВедіть № студента 1-50")
                    n_st = input_number(1, 50)
                    print("ВВедіть № викладача 1-6")
                    n_teach = input_number(1, 6)
                    pprint.pprint(execute_query(sql, n_st, n_teach))
                elif answer == 12:
                    print("ВВедіть № группи 1-4")
                    n_gr = input_number(1, 4)
                    print("Введить № предмета 1-9")
                    n_subj = input_number(1, 9)
                    pprint.pprint(execute_query(sql, n_gr, n_subj))
                else:
                    pprint.pprint(execute_query(sql))


if __name__ == "__main__":
    main()
