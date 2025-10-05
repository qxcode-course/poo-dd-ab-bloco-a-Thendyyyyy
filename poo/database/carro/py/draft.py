class Carro:
    def __init__(self):
        self.pass_ = 0;
        self.km = 0;
        self.passMax = 2;
        self.gas = 0;
        self.gasMax = 100;

    def __str__(self):
        return f"pass: {self.pass_}, gas: {self.gas}, km: {self.km}";

    def enter(self):
        if self.pass_ < self.passMax:
            self.pass_ += 1;
        else:
            print("fail: limite de pessoas atingido");

    def leave(self):
        if self.pass_ > 0:
            self.pass_ -= 1;
        else:
            print("fail: nao ha ninguem no carro");

    def fuelUp(self, amount: int):
        self.gas += amount;
        if self.gas > self.gasMax:
            self.gas = self.gasMax;

    def drive(self, distance: int):
        if self.pass_ == 0:
            print("fail: nao ha ninguem no carro");
        elif self.gas == 0:
            print("fail: tanque vazio");
        elif distance <= self.gas:
            self.gas -= distance;
            self.km += distance;
        else:
            travelled = self.gas;
            self.km += travelled;
            print(f"fail: tanque vazio apos andar {travelled} km")
            self.gas = 0;
        
def __main__():
    carro = Carro();
    while True:
        line: str = input();
        print(f"${line}", end ="\n");
        arg: list[str] = line.split(" ");

        if arg[0] == "end":
            break;
        elif arg[0] == "show":
            print(carro.__str__());
        elif arg[0] == "enter":
            carro.enter();
        elif arg[0] == "leave":
            carro.leave();
        elif arg[0] == "fuel":
            amount = int(arg[1]);
            carro.fuelUp(amount);
        elif arg[0] == "drive":
            distancia = int(arg[1]);
            carro.drive(distancia);
        else:
            print("fail: comando desconhecido");

__main__();