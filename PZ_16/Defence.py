
class Squad:
    def __init__(self,surname,dolznost, zp):
        self.surname = surname
        self.dolznost = dolznost
        self.zp = zp
    def showZP(self):
        return self.zp


worker1 = Squad("Иванов", "Бухгалтер", 75000)
worker2 = Squad("Петров", "Бухгалтер", 95000)
worker3 = Squad("Сидоров", "Начальник", 160000)

print("Зп 1-го:", worker1.showZP(),"Зп 2-го:",worker2.showZP(),"Зп 3-го:",worker3.showZP())
