import random

__author__ = 'guillermodelgado'


def get_cost_per_hour():
    x = random.randint(1, 10)
    return x


COST_PER_HOUR = get_cost_per_hour()


def get_salary_per_hour():
    x = 0
    while True:
        x = random.randint(1, 10)
        if x > COST_PER_HOUR:
            break
    return x


SALARY_PER_HOUR = get_salary_per_hour()


class Villain:
    def __init__(self):
        self.life = random.randint(0, 10)
        self.distance = random.randint(0, 10)
        self.isSneak = bool(random.getrandbits(1))


def get_villains_sort_key(villain):
    return villain.distance


def get_villains_list():
    generated_villains = random.randint(1,1000)
    # generated_villains = 3
    return sorted([Villain() for i in range(generated_villains)], key=get_villains_sort_key)


def get_working_hours():
    return random.randint(8, 24)


def print_villain_list(my_list):
    print("Number of villains : " + str(len(my_list)))
    count = 1
    for i in my_list:
        print("- Villain " + str(count) + " :: " + "life:"+str(i.life) + " / " + "distance:"+str(i.distance) + " / " + "isSneak:"+str(i.isSneak))
        count += 1


def main():
    villain_list = get_villains_list()
    captured_villains = []
    sneaks = []
    total_cost = 0
    total_salary = 0

    print_villain_list(villain_list)

    for day in range(0, 7):
        daily_cost = 0
        daily_salary = 0
        pending_hours = get_working_hours()

        print("\n************************************************************")
        print("Day " + str(day + 1))
        print("Hour/day: " + str(pending_hours))

        while True:
            if pending_hours <= 0:
                break
            if len(villain_list) > 0:
                v = villain_list[0]
                if v.isSneak:
                    print("Villain is sneak")
                    sneaks.append(v)
                    villain_list.remove(v)
                else:
                    daily_cost += COST_PER_HOUR
                    daily_salary += SALARY_PER_HOUR
                    v.life -= 1
                    if v.life <= 0:
                        print("Villain captured")
                        captured_villains.append(v)
                        villain_list.remove(v)
            pending_hours -= 1

        total_cost += daily_cost
        total_salary += daily_salary
        print("Daily spent money: " + str(daily_cost))
        print("Daily earned money: " + str(daily_salary))

    print("\n\n************************************************************")
    print("************************************************************")
    print("Cost/Hour : " + str(COST_PER_HOUR))
    print("Salary/Hour : " + str(SALARY_PER_HOUR))
    print("Sneaks: " + str(len(sneaks)))
    print("Captured villains: " + str(len(captured_villains)))
    print("Total spent money: " + str(total_cost))
    print("Total earned money: " + str(total_salary))


if __name__ == '__main__':
    main()
