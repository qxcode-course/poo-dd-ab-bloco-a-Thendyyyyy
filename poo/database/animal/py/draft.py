class Animal:
    def __init__(self, species: str, age: int, sound: str):
        self.species: str = species;
        self.age: 0 = age;
        self.sound: str = sound;
    
    def ageBy(self, amount: int) -> None:
        self.age += amount;
        if self.age >= 4:
            self.age = 4;
            return f"warning: {self.species} morreu";

    def makeSound(self) -> str:
        if self.age == 0:
            return "---";
        elif self.age == 4:
            return "RIP";
        else:
            return self.sound;

    def read(self) -> str:
        return f"{self.species}:{self.age}:{self.sound}";

def __main__():
    animal = Animal("", "", "");
    while True:
        line: str = input();
        print(f"${line}", end="\n");
        args: list[str] = line.split(" ");
            
        if args[0] == "end":
            break;
        elif args[0] == "init":
            species = args[1];
            age = 0;
            sound = args[2];
            animal = Animal(species, age, sound);
        elif args[0] == "show":
            print(animal.read());
        elif args[0] == "grow":
            msg = animal.ageBy(int(args[1]));
            if msg:
                print(msg);
        elif args[0] == "noise":
            print(animal.makeSound());
        else:
            print("fail: comando desconhecido");

__main__();
