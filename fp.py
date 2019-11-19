#!/bin/python

  # 1 => false / die
  # 2 => true  / life
  # 0 => ?
  #per duapuluh

#test
p_atribut = ["total kasus","age 20-40","age 41-60","age 61-80","steroid=NO","steroid=YES","malaise=NO","malaise=YES","liver big=NO","liver big=YES","spiders=NO","spiders=YES","varises=NO","varises=YES"]
p_jumlah  = [155,82,59,14,76,79,61,94,25,130,51,104,18,137]
p_life  =[123,73,39,11,56,67,38,85,22,101,29,94,7,116]
p_die  =[32,9,20,3,20,12,23,9,3,29,22,10,11,21]
p_x_life = [0.794,0.890,0.661,0.786,0.737,0.848,0.623,0.904,0.880,0.777,0.569,0.904,0.389,0.847]
p_x_die = [0.206,0.110,0.339,0.214,0.263,0.152,0.377,0.096,0.120,0.223,0.431,0.096,0.611,0.153]

#input user
arr_life = []
arr_die = []

a = int(input("Masukkan umur = ")) #input umur
if (a<=40) :
  arr_life.append(p_x_life[1])
  arr_die.append(p_x_die[1])
elif (a>=61):
  arr_life.append(p_x_life[3])
  arr_die.append(p_x_die[3])
else :
  arr_life.append(p_x_life[2])
  arr_die.append(p_x_die[2])

b = int(input("Apakah anda pengguna steroid = (1. No / 2. Yes)")) #input steroid
if (b==1):
  arr_life.append(p_x_life[4])
  arr_die.append(p_x_die[4])
elif (b==2):
  arr_life.append(p_x_life[5])
  arr_die.append(p_x_die[5])

c = int(input("apakah anda mengalami malaise = (1. No / 2. Yes)")) #input malaise
if(c==1):
  arr_life.append(p_x_life[6])
  arr_die.append(p_x_die[6])
elif(c==2):
  arr_life.append(p_x_life[7])
  arr_die.append(p_x_die[7])

d = int(input("Apakah anda mempunyai Liver yang besar = (1. No / 2. Yes)")) #input liver big
if (d==1):
  arr_life.append(p_x_life[8])
  arr_die.append(p_x_die[8])
elif (d==2):
  arr_life.append(p_x_life[9])
  arr_die.append(p_x_die[9])

e = int(input("apakah anda mengidap spiders = (1. No / 2. Yes)")) #input spiders
if (e==1):
  arr_life.append(p_x_life[10])
  arr_die.append(p_x_die[10])
elif (e==2):
  arr_life.append(p_x_life[11])
  arr_die.append(p_x_die[11])
f = int(input("apakah anda mengidap varises = (1. No / 2. Yes)")) #input varises
if (f==1):
  arr_life.append(p_x_life[12])
  arr_die.append(p_x_die[12])
elif (f==2):
  arr_life.append(p_x_life[13])
  arr_die.append(p_x_die[13])

prob_life = 1
prob_die = 1
for i in arr_life:
  prob_life = prob_life * i

for i in arr_die:
  prob_die = prob_die * i

if (prob_life > prob_die):
  print("Anda diprediksi hidup")
else :
  print("anda diprediksi meninggal")
print("Probabilitas total hidup : ",prob_life,"probabilitas total mati : ",prob_die)
