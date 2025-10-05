class Towel:
    def __init__(self, color: str, size: str):
        self.color: str = color;
        self.size: str = size;
        self.wetness: int = 0;

    def __str__(self) -> str:
        return f"Cor:{self.color}, Tam:{self.size}, Umidade:{self.wetness}"

    def __dry__(self, amount: int) -> None:
        self.wetness += amount;
        if self.wetness > self.getMaxWetness():
            print("toalha encharcada")
            self.wetness = self.getMaxWetness;

    def __getMaxWetness__(self) -> int:
        if self.size == "P":
            return 10;
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0
    
    def __isDry__(self) -> bool:
        return self.wetness;

    def __wringOut__(self) -> None:
        self.wetness = 0;

def __main__():
    toalha = Towel("", " ");
    while True:
        print("$", end="")
        line:str = input()
        args: list[str] = line.split(" ")
        
        if args[0] == "end":
            break;
        elif args[0] == "criar":
            color = args[1];
            size = args[2];
            toalha = Towel(color, size);
        elif args[0] == "mostrar":
            print(toalha);
        elif args[0] == "enxugar":
            if toalha.dry >= toalha.getMaxWetness:
                print("toalha encharcada");
            else:
                amount = int(args[1])
                toalha.dry(amount);
        elif args[0] == "torcer":
            toalha.dry = 0;
        elif args[0] == "seca":
            if toalha.dry == 0:
                print("sim")
            else:
                print("nao")
        else:
            print("fail: comando desconhecido");

__main__();