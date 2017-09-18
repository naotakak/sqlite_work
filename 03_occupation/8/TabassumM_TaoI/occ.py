import csv
import random
occupations_dict = {}

#with open('occupations.csv') as csvfile:
#	reader = csv.DictReader(csvfile)
#	for row in reader:
#		print(row)

reader = csv.DictReader(open('occupations.csv'))
for row in reader:
	k, v = row['Job Class'], float(row['Percentage'])
	occupations_dict[k] = v
	
#print occupations_dict

def getRandOcc():
	x = random.uniform(0,99.8)
	for k in occupations_dict:
		if (x - (occupations_dict.get(k)) < 0):
			return k
		else:
			x = (x - (occupations_dict.get(k)))
			

print getRandOcc()
print getRandOcc()
print getRandOcc()
print getRandOcc()
print getRandOcc()
print getRandOcc()
print getRandOcc()
print getRandOcc()
print getRandOcc()
print getRandOcc()

