class Musician:

    def __init__(self, name, fee, age):
        self.__name = name
        self.__fee = fee
        self.__age = age

    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, name):
        self.__name = name


    @property
    def fee(self):
        return self.__fee


    @fee.setter
    def fee(self, fee):
        self.__fee = fee


    @property
    def age(self):
        return self.__age


    @age.setter
    def age(self, age):
        self.__age = age

    def __str__(self):
        return f"Musician: {self.name}, Fee: {self.fee}, Age: {self.__age}"


class MusicFestival:
    def __init__(self, budget):
        self.budget = budget
        self.musicians = []

    def add_musicians(self, musicians):
        if not isinstance(musicians, list):
            musicians = [musicians]

        total_fee = self.get_total_fee()
        for musician in musicians:

            if total_fee + musician.fee <= self.budget:
                self.musicians.append(musician)
                total_fee += musician.fee
            else:
                print(f"The artist {musician.name} does not fit into the budget.")
                
    def remove_musician(self, musician_name):
        for musician in self.musicians:
            if musician.name == musician_name:
                self.musicians.remove(musician)
                print(f"{musician_name} has been removed.")
                return
        print(f"{musician_name} not found in the list.")


    def get_total_fee(self):
        return sum(musician.fee for musician in self.musicians)

    def show_musicians(self):
        print("Musicians in the festival:")
        for musician in self.musicians:
            print(musician)

    def __str__(self):
        return f"Music Festival with Budget: {self.budget}, Current Total Fee: {self.get_total_fee()}"


def main():

    musician1 = Musician("Adelе", 2800, 36)
    musician2 = Musician("Travis Scott", 7000, 33)
    musician3 = Musician("The Weeknd", 5000, 34)
    musician4 = Musician("Billie Eilish", 6000, 22)

    festival = MusicFestival(14000)

    festival.add_musicians([musician1, musician2, musician3, musician4])

    festival.show_musicians()

    musician5 = Musician("Nikow", 1000, 23)
    festival.add_musicians(musician5)

    festival.remove_musician("The Weeknd")

    festival.show_musicians()


if __name__ == "__main__":
    main()