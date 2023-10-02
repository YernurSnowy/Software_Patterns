class Singleton:
    instance = None

    def __new__(cls):
        if Singleton.instance is None:
            Singleton.instance = super().__new__(cls)
        return Singleton.instance
    
    def weapon(self):
        print("Take a stick")
        self.data = "stick"

if __name__ == "__main__":
    police = Singleton()
    police.weapon()
    print(police)
    soldier = Singleton()
    print(soldier)
    print(police is soldier)
    print(police.data)
    police.data = "gun"
    print(soldier.data)
    