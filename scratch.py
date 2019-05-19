"""
Створити консольну програму мовою Python і написати клас <Газонокосарка> який міститиме:

Такі поля:
- ширина скосу трави (в сантиметрах)
- потужність двигуна (у ватах)
- модель
- обєм паливного баку

Три додаткових поля, які найкраще описують даний клас

Конструктор (із вказаними дефолтними значеннями)

Деструктор

Метод, що повертає стрічкове представлення класу

Статичне поле

Статичний метод, що повертає значення статичного поля

В main() методі визначіть 3 об’єкти типу із завдання (з-за допомогою передачі різної кількості параметрів) та виведіть інформацію про них з-за
допомогою методу з пункту 4 в консоль
"""


class Lawnmover:
    price = 20

    def __init__(self, cutting_width=0, engine_power=0, model="no_name", tank_volume=0, weight=0, length=0,
                 сolour ="no_name"):
        self.cutting_width = cutting_width
        self.engine_power = engine_power
        self.model = model
        self.tank_volume = tank_volume
        self.weight = weight
        self.length = length
        self.colour = сolour

    def __str__(self):
        return str(self.__dict__)

    def __del__(self):
        print("Destructor -> " + self.cutting_width + " deleted")

    @staticmethod
    def clearence_height():
        return 20


def main():
    A100 = Lawnmover("A100", 2.95, 1, 1.1, "Green")
    Jforce350 = Lawnmover("Jforce350", 5, 1, 1.5, "Red")
    SigmaUX = Lawnmover("SigmaUX", "Orange-Black")

    print(A100)
    print(Jforce350)
    print(SigmaUX)

    print(Lawnmover.clearence_height())


if __name__ == "__main__":
    main()
