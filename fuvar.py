class Taxi:
    def __init__(self,ID,start,leng,km,dollar,plus,howbuy) -> None:
        self.ID = ID
        self.start = start
        self.leng = leng
        self.km = km
        self.dollar = dollar
        self.plus = plus
        self.howbuy = howbuy


taxi = []
file = open("fuvar.csv", "rt", encoding="utf-8")
file.readline
for row in file:
    row = row.strip().split(";")
    taxi.append(Taxi(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

print(f"3. feladat: {len(taxi)} fuvar")
