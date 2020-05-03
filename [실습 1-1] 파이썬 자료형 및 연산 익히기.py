def main():
    a = 3
    a_square = a ** 2
    b = 11
    a_power_b = a ** b

    c = [1.23, 2.21, 3.66, 4.25, 5.21, 31.25, 18.87]

    five_c = 5 * c

    c_ac_b = [a * c for i in c]

    d = [1, 2, 3, 5, 3, 7, 8, 8, 4, 5, 6, 2, 5, 7, 9, 4, 4, 9, 5, 6, 3, 2, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 8]

    num_one = d.count(1)
    num_two = d.count(0)

    e = ["유진", "민철", "가영", "민희", "영진", "미희", "진수", "영철", "민지", "영호", "호준", "지혜", "철수"]
    for idx in enumerate(e):
        e_with_rank = [str(idx + 1) + "등 - " + e for e in e]
    f = ["YJ", "MC", "GY", "MH", "YJ", "MH", "JS", "YC", "MJ", "YH", "HJ", "JH", "CS"]

    correspond_e_f = [zip(f, e)]

    print(a, b, a_square, a_power_b, c, five_c, c_ac_b, num_one, num_two, e_with_rank, correspond_e_f)


main()