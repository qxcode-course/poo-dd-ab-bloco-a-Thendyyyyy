class Calculator:
    def __init__(self, batteryMax: int):
        self.display = 0.0;
        self.battery = 0;
        self.batteryMax = batteryMax;

    def __str__(self):
        print(f"display = {self.display:.2f}, battery = {self.battery}");

    def chargeUp(self, charging: int):
        self.battery += charging;
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax;

    def calculating(self) -> bool:
        if self.battery > 0:
            self.battery -= 1;
            return True;
        else:
            print("fail: bateria insuficiente");
            return False;

    def somar(self, a: float, b: float):
        if self.calculating():
            self.display = a + b;

    def dividir(self, den: float, num: float):
        if self.calculating():
            if num == 0:
                print("fail: divisao por zero")
            else:
                self.display = den / num;

def __main__():
    calculadora = Calculator("");
    while True:
        line:str = input();
        print(f"${line}", end = "\n");
        arg: list[str] = line.split(" ");

        if arg[0] == "end":
                break;
        elif arg[0] == "init":
            batteryMax = int(arg[1]);
            calculadora.__init__(batteryMax);
        elif arg[0] == "show":
            calculadora.__str__();
        elif arg[0] == "charge":
            charges = int(arg[1]);
            calculadora.chargeUp(charges);
        elif arg[0] == "sum":
            a = float(arg[1]);
            b = float(arg[2]);
            calculadora.somar(a, b);
        elif arg[0] == "div":
            a = float(arg[1]);
            b = float(arg[2]);
            calculadora.dividir(a, b);
        else:
            print("fail: comando desconhecido");

__main__();