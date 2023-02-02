import random
import math

horse = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]


race = horse
random.shuffle(race)


r1 = race[0:5]
r1.sort()
print("race 1 ", end='')
print(r1)

r2 = race[5:10]
r2.sort()
print("race 2 ", end='')
print(r2)

r3 = race[10:15]
r3.sort()
print("race 3 ", end='')
print(r3)

r4 = race[15:20]
r4.sort()
print("race 4 ", end='')
print(r4)

r5 = race[20:25]
r5.sort()
print("race 5 ", end='')
print(r5)

r6 = [r1[0], r2[0], r3[0], r4[0], r5[0]]
r6.sort()
print("race 6 ", end='')
print(r6)


index_temp = []
for r in [r6[0], r6[1]] :
	index = math.floor(race.index(r)/5) 
	match index :
		case 0 :
			index_temp.append(r1)
		case 1 :
			index_temp.append(r2)
		case 2 :
			index_temp.append(r3)
		case 3 :
			index_temp.append(r4)
		case 4 :
			index_temp.append(r5)

r7 = [index_temp[0][1],index_temp[0][2],index_temp[1][0],index_temp[1][1],r6[2]]
r7.sort()
print("race 7 ", end='')
print(r7)

result= [r6[0],r7[0],r7[1]]
print(result)
