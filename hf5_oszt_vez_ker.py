import math


class Number:
    def __init__(self, num, row):
        self.num = num
        self.row = row


# beolvasás

num_file = open("input.txt", "r")
num_list = list()
row_count = 0

for line in num_file:
    array = line.split(":")
    row_count += 1
    for numb in array:
        num_list.append(Number(int(numb), row_count))

# 2. feladat

min_list = list()

for numb in num_list:
    if numb.row == 1:
        min_list.append(numb.num)

print(f"2. feladat:\nAz 1. sorban szereplő számok minimuma: {min(min_list)}")

# 3. feladat

three_divs = list()

for numb in num_list:
    if numb.num % 3 == 0 and numb.row == 2:
        three_divs.append(numb.num)

print(f"3. feladat:\nA 2. sorban szereplő hárommal osztható számok összege: {sum(three_divs)}")

# 4. feladat

odd_nums = list()

for numb in num_list:
    if numb.num % 2 == 1 and numb.row == 3:
        odd_nums.append(numb.num)


avg = sum(odd_nums) / len(odd_nums)

print(f"4. feladat:\nA 3. sorban szereplő páratlan  számok számtani közepe: {avg:.2f}")

# 5. feladat

line_four_nums = list()
i = 0

for numb in num_list:
    if numb.row == 4:
        line_four_nums.append(numb.num)

line_four_nums = sorted(line_four_nums)
summ = 1


while i < 15:
    summ *= line_four_nums[i]
    i += 1

summ = math.pow(summ, 1/10)

print(f"5. feladat\nA 4. sorban szereplő 15 legkisebb szám szorzatának nagyságrendje: 10^{summ:.2f}")


# 6. feladat

powsum = 0

for numb in num_list:
    if numb.row == 5 and numb.num % 2 == 0:
        powsum += math.pow(numb.num, 2)

print(f"6. feladat\nAz 5. sorban szereplő páros számok négyzeteinek összege: {int(powsum)}")


# 7. feladat

num_list = sorted(num_list, key=lambda num: num.num)
asd = list()

i = 0

while i < 12:
    asd.append(num_list[i].num)
    i += 1

print(f"7. feladat\nAz inputban szereplő összes szám közül a  12 legkisebb szám maximuma: {max(asd)}")
