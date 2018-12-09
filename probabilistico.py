from random import shuffle
import math

#número de classes do problema
carsList = []

path = '/home/joao/Documentos/Machine Learning/car.data'
file = open(path,'r')
cars = file.readline()

buyingList = ['vhigh', 'high', 'med', 'low'] 
maintList = ["vhigh", "high", "med", "low"]
doorsList = ["2", "3", "4", "5more"]
personsList = ["2", "4", "more"]
lug_bootList = ["small", "med", "big"]
safetyList = [ "low", "med", "high"]
clssList = ["unacc", "acc", "good", "vgood"]

trainPercentage = 0.8

while (cars != ""):

    foo = ( [pos for pos, char in enumerate(cars) if char == ","])
    at1 = cars[0:foo[0]]
    at2 = cars[foo[0]+1:foo[1]]
    at3 = cars[foo[1]+1:foo[2]]
    at4 = cars[foo[2]+1:foo[3]]
    at5 = cars[foo[3]+1:foo[4]]
    at6 = cars[foo[4]+1:foo[5]]
    clss = cars[foo[5]+1:-1]

    i = 0
    
    for i in range(4):
        if (at1 == buyingList[i]):
            at1 = i
        if (at2 == maintList[i]):
            at2 = i
        if (at3 == doorsList[i]):
            at3 = i
        if (clss == clssList[i]):
            clss = i

    for i in range(3):
        if (at4 == personsList[i]):
            at4 = i
        if (at5 == lug_bootList[i]):
            at5 = i
        if (at6 == safetyList[i]):
            at6 = i

    tmp = [at1,at2,at3,at4,at5,at6,clss]
    carsList.append(tmp)
    cars = file.readline()
shuffle(carsList)
# print(carsList)

b_vh_un = 0
b_vh_ac = 0
b_vh_go = 0
b_vh_vgo = 0
b_h_un = 0
b_h_ac = 0
b_h_go = 0
b_h_vgo = 0
b_m_un = 0
b_m_ac = 0
b_m_go = 0
b_m_vgo = 0
b_l_un = 0
b_l_ac = 0
b_l_go = 0
b_l_vgo = 0

m_vh_un = 0
m_vh_ac = 0
m_vh_go = 0
m_vh_vgo = 0
m_h_un = 0
m_h_ac = 0
m_h_go = 0
m_h_vgo = 0
m_m_un = 0
m_m_ac = 0
m_m_go = 0
m_m_vgo = 0
m_l_un = 0
m_l_ac = 0
m_l_go = 0
m_l_vgo = 0

d_2_un = 0
d_2_ac = 0
d_2_go = 0
d_2_vgo = 0
d_3_un = 0
d_3_ac = 0
d_3_go = 0
d_3_vgo = 0
d_4_un = 0
d_4_ac = 0
d_4_go = 0
d_4_vgo = 0
d_5p_un = 0
d_5p_ac = 0
d_5p_go = 0
d_5p_vgo = 0

p_2_un = 0
p_2_ac = 0
p_2_go = 0
p_2_vgo = 0
p_4_un = 0
p_4_ac = 0
p_4_go = 0
p_4_vgo = 0
p_m_un = 0
p_m_ac = 0
p_m_go = 0
p_m_vgo = 0

lb_s_un = 0
lb_s_ac = 0
lb_s_go = 0
lb_s_vgo = 0
lb_m_un = 0
lb_m_ac = 0
lb_m_go = 0
lb_m_vgo = 0
lb_b_un = 0
lb_b_ac = 0
lb_b_go = 0
lb_b_vgo = 0

s_l_un = 0
s_l_ac = 0
s_l_go = 0
s_l_vgo = 0
s_m_un = 0
s_m_ac = 0
s_m_go = 0
s_m_vgo = 0
s_h_un = 0
s_h_ac = 0
s_h_go = 0
s_h_vgo = 0

un = 0
ac = 0
go = 0
vgo = 0
i = 0
for i in range(int(len(carsList)*trainPercentage)):
    if (carsList[i][0] == 0 and (carsList[i][6] == 0)):
        b_vh_un+=1
    if (carsList[i][0] == 0 and (carsList[i][6] == 1)):
        b_vh_ac+=1
    if (carsList[i][0] == 0 and (carsList[i][6] == 2)):
        b_vh_go+=1
    if (carsList[i][0] == 0 and (carsList[i][6] == 3)):
        b_vh_vgo+=1
    if (carsList[i][0] == 1 and (carsList[i][6] == 0)):
        b_h_un+=1
    if (carsList[i][0] == 1 and (carsList[i][6] == 1)):
        b_h_ac+=1
    if (carsList[i][0] == 1 and (carsList[i][6] == 2)):
        b_h_go+=1
    if (carsList[i][0] == 1 and (carsList[i][6] == 3)):
        b_h_vgo+=1
    if (carsList[i][0] == 2 and (carsList[i][6] == 0)):
        b_m_un+=1
    if (carsList[i][0] == 2 and (carsList[i][6] == 1)):
        b_m_ac+=1
    if (carsList[i][0] == 2 and (carsList[i][6] == 2)):
        b_m_go+=1
    if (carsList[i][0] == 2 and (carsList[i][6] == 3)):
        b_m_vgo+=1
    if (carsList[i][0] == 3 and (carsList[i][6] == 0)):
        b_l_un+=1
    if (carsList[i][0] == 3 and (carsList[i][6] == 1)):
        b_l_ac+=1
    if (carsList[i][0] == 3 and (carsList[i][6] == 2)):
        b_l_go+=1
    if (carsList[i][0] == 3 and (carsList[i][6] == 3)):
        b_l_vgo+=1
    
    if (carsList[i][1] == 0 and (carsList[i][6] == 0)):
        m_vh_un+=1
    if (carsList[i][1] == 0 and (carsList[i][6] == 1)):
        m_vh_ac+=1
    if (carsList[i][1] == 0 and (carsList[i][6] == 2)):
        m_vh_go+=1
    if (carsList[i][1] == 0 and (carsList[i][6] == 3)):
        m_vh_vgo+=1
    if (carsList[i][1] == 1 and (carsList[i][6] == 0)):
        m_h_un+=1
    if (carsList[i][1] == 1 and (carsList[i][6] == 1)):
        m_h_ac+=1
    if (carsList[i][1] == 1 and (carsList[i][6] == 2)):
        m_h_go+=1
    if (carsList[i][1] == 1 and (carsList[i][6] == 3)):
        m_h_vgo+=1
    if (carsList[i][1] == 2 and (carsList[i][6] == 0)):
        m_m_un+=1
    if (carsList[i][1] == 2 and (carsList[i][6] == 1)):
        m_m_ac+=1
    if (carsList[i][1] == 2 and (carsList[i][6] == 2)):
        m_m_go+=1
    if (carsList[i][1] == 2 and (carsList[i][6] == 3)):
        m_m_vgo+=1
    if (carsList[i][1] == 3 and (carsList[i][6] == 0)):
        m_l_un+=1
    if (carsList[i][1] == 3 and (carsList[i][6] == 1)):
        m_l_ac+=1
    if (carsList[i][1] == 3 and (carsList[i][6] == 2)):
        m_l_go+=1
    if (carsList[i][1] == 3 and (carsList[i][6] == 3)):
        m_l_vgo+=1

    if (carsList[i][2] == 0 and (carsList[i][6] == 0)):
        d_2_un+=1
    if (carsList[i][2] == 0 and (carsList[i][6] == 1)):
        d_2_ac+=1
    if (carsList[i][2] == 0 and (carsList[i][6] == 2)):
        d_2_go+=1
    if (carsList[i][2] == 0 and (carsList[i][6] == 3)):
        d_2_vgo+=1
    if (carsList[i][2] == 1 and (carsList[i][6] == 0)):
        d_3_un+=1
    if (carsList[i][2] == 1 and (carsList[i][6] == 1)):
        d_3_ac+=1
    if (carsList[i][2] == 1 and (carsList[i][6] == 2)):
        d_3_go+=1
    if (carsList[i][2] == 1 and (carsList[i][6] == 3)):
        d_3_vgo+=1
    if (carsList[i][2] == 2 and (carsList[i][6] == 0)):
        d_4_un+=1
    if (carsList[i][2] == 2 and (carsList[i][6] == 1)):
        d_4_ac+=1
    if (carsList[i][2] == 2 and (carsList[i][6] == 2)):
        d_4_go+=1
    if (carsList[i][2] == 2 and (carsList[i][6] == 3)):
        d_4_vgo+=1
    if (carsList[i][2] == 3 and (carsList[i][6] == 0)):
        d_5p_un+=1
    if (carsList[i][2] == 3 and (carsList[i][6] == 1)):
        d_5p_ac+=1
    if (carsList[i][2] == 3 and (carsList[i][6] == 2)):
        d_5p_go+=1
    if (carsList[i][2] == 3 and (carsList[i][6] == 3)):
        d_5p_vgo+=1

    if (carsList[i][3] == 0 and (carsList[i][6] == 0)):
        p_2_un+=1
    if (carsList[i][3] == 0 and (carsList[i][6] == 1)):
        p_2_ac+=1
    if (carsList[i][3] == 0 and (carsList[i][6] == 2)):
        p_2_go+=1
    if (carsList[i][3] == 0 and (carsList[i][6] == 3)):
        p_2_vgo+=1
    if (carsList[i][3] == 1 and (carsList[i][6] == 0)):
        p_4_un+=1
    if (carsList[i][3] == 1 and (carsList[i][6] == 1)):
        p_4_ac+=1
    if (carsList[i][3] == 1 and (carsList[i][6] == 2)):
        p_4_go+=1
    if (carsList[i][3] == 1 and (carsList[i][6] == 3)):
        p_4_vgo+=1
    if (carsList[i][3] == 2 and (carsList[i][6] == 0)):
        p_m_un+=1
    if (carsList[i][3] == 2 and (carsList[i][6] == 1)):
        p_m_ac+=1
    if (carsList[i][3] == 2 and (carsList[i][6] == 2)):
        p_m_go+=1
    if (carsList[i][3] == 2 and (carsList[i][6] == 3)):
        p_m_vgo+=1

    if (carsList[i][4] == 0 and (carsList[i][6] == 0)):
        lb_s_un+=1
    if (carsList[i][4] == 0 and (carsList[i][6] == 1)):
        lb_s_ac+=1
    if (carsList[i][4] == 0 and (carsList[i][6] == 2)):
        lb_s_go+=1
    if (carsList[i][4] == 0 and (carsList[i][6] == 3)):
        lb_s_vgo+=1
    if (carsList[i][4] == 1 and (carsList[i][6] == 0)):
        lb_m_un+=1
    if (carsList[i][4] == 1 and (carsList[i][6] == 1)):
        lb_m_ac+=1
    if (carsList[i][4] == 1 and (carsList[i][6] == 2)):
        lb_m_go+=1
    if (carsList[i][4] == 1 and (carsList[i][6] == 3)):
        lb_m_vgo+=1
    if (carsList[i][4] == 2 and (carsList[i][6] == 0)):
        lb_b_un+=1
    if (carsList[i][4] == 2 and (carsList[i][6] == 1)):
        lb_b_ac+=1
    if (carsList[i][4] == 2 and (carsList[i][6] == 2)):
        lb_b_go+=1
    if (carsList[i][4] == 2 and (carsList[i][6] == 3)):
        lb_b_vgo+=1

    if (carsList[i][5] == 0 and (carsList[i][6] == 0)):
        s_l_un+=1
    if (carsList[i][5] == 0 and (carsList[i][6] == 1)):
        s_l_ac+=1
    if (carsList[i][5] == 0 and (carsList[i][6] == 2)):
        s_l_go+=1
    if (carsList[i][5] == 0 and (carsList[i][6] == 3)):
        s_l_vgo+=1
    if (carsList[i][5] == 1 and (carsList[i][6] == 0)):
        s_m_un+=1
    if (carsList[i][5] == 1 and (carsList[i][6] == 1)):
        s_m_ac+=1
    if (carsList[i][5] == 1 and (carsList[i][6] == 2)):
        s_m_go+=1
    if (carsList[i][5] == 1 and (carsList[i][6] == 3)):
        s_m_vgo+=1
    if (carsList[i][5] == 2 and (carsList[i][6] == 0)):
        s_h_un+=1
    if (carsList[i][5] == 2 and (carsList[i][6] == 1)):
        s_h_ac+=1
    if (carsList[i][5] == 2 and (carsList[i][6] == 2)):
        s_h_go+=1
    if (carsList[i][5] == 2 and (carsList[i][6] == 3)):
        s_h_vgo+=1

    if (carsList[i][6] == 0):
        un+=1
    if (carsList[i][6] == 1):
        ac+=1
    if (carsList[i][6] == 2):
        go+=1
    if (carsList[i][6] == 3):
        vgo+=1


trainNumber = (float(len(carsList)))*trainPercentage
valid = 0
invalid = 0


b_un_list=[b_vh_un/trainNumber, b_h_un/trainNumber, b_m_un/trainNumber, b_l_un/trainNumber]
b_ac_list=[b_vh_ac/trainNumber, b_h_ac/trainNumber, b_m_ac/trainNumber, b_l_ac/trainNumber]
b_go_list=[b_vh_go/trainNumber, b_h_go/trainNumber, b_m_go/trainNumber, b_l_go/trainNumber]
b_vgo_list=[b_vh_vgo/trainNumber, b_h_vgo/trainNumber, b_m_vgo/trainNumber, b_l_vgo/trainNumber]
# print ("Buying-------")
# print (b_un_list,b_ac_list,b_go_list,b_vgo_list)

m_un_list=[m_vh_un/trainNumber, m_h_un/trainNumber, m_m_un/trainNumber, m_l_un/trainNumber]
m_ac_list=[m_vh_ac/trainNumber, m_h_ac/trainNumber, m_m_ac/trainNumber, m_l_ac/trainNumber]
m_go_list=[m_vh_go/trainNumber, m_h_go/trainNumber, m_m_go/trainNumber, m_l_go/trainNumber]
m_vgo_list=[m_vh_vgo/trainNumber, m_h_vgo/trainNumber, m_m_vgo/trainNumber, m_l_vgo/trainNumber]
# print ("Maint-------")
# print (m_un_list,m_ac_list,m_go_list,m_vgo_list)

d_un_list=[d_2_un/trainNumber, d_3_un/trainNumber, d_4_un/trainNumber, d_5p_un/trainNumber]
d_ac_list=[d_2_ac/trainNumber, d_3_ac/trainNumber, d_4_ac/trainNumber, d_5p_ac/trainNumber]
d_go_list=[d_2_go/trainNumber, d_3_go/trainNumber, d_4_go/trainNumber, d_5p_go/trainNumber]
d_vgo_list=[d_2_vgo/trainNumber, d_3_vgo/trainNumber, d_4_vgo/trainNumber, d_5p_vgo/trainNumber]
# print ("Door-------")
# print (d_un_list,d_ac_list,d_go_list,d_vgo_list)

p_un_list=[p_2_un/trainNumber, p_4_un/trainNumber, p_m_un/trainNumber]
p_ac_list=[p_2_ac/trainNumber, p_4_ac/trainNumber, p_m_ac/trainNumber]
p_go_list=[p_2_go/trainNumber, p_4_go/trainNumber, p_m_go/trainNumber]
p_vgo_list=[p_2_vgo/trainNumber, p_4_vgo/trainNumber, p_m_vgo/trainNumber]
# print ("Person-------")
# print (p_un_list,p_ac_list,p_go_list,p_vgo_list)

lb_un_list=[lb_s_un/trainNumber, lb_m_un/trainNumber, lb_b_un/trainNumber]
lb_ac_list=[lb_s_ac/trainNumber, lb_m_ac/trainNumber, lb_b_ac/trainNumber]
lb_go_list=[lb_s_go/trainNumber, lb_m_go/trainNumber, lb_b_go/trainNumber]
lb_vgo_list=[lb_s_vgo/trainNumber, lb_m_vgo/trainNumber, lb_b_vgo/trainNumber]
# print ("Luggage Boot-------")
# print (lb_un_list,lb_ac_list,lb_go_list,lb_vgo_list)

s_un_list=[s_l_un/trainNumber, s_m_un/trainNumber, s_h_un/trainNumber]
s_ac_list=[s_l_ac/trainNumber, s_m_ac/trainNumber, s_h_ac/trainNumber]
s_go_list=[s_l_go/trainNumber, s_m_go/trainNumber, s_h_go/trainNumber]
s_vgo_list=[s_l_vgo/trainNumber, s_m_vgo/trainNumber, s_h_vgo/trainNumber]
# print ("Safety-------")
# print (s_un_list,s_ac_list,s_go_list,s_vgo_list)


for i in range(int(trainNumber),len(carsList)):
    obj_un = b_un_list[carsList[i][0]]*m_un_list[carsList[i][1]]*d_un_list[carsList[i][2]]*p_un_list[carsList[i][3]]*lb_un_list[carsList[i][4]]*s_un_list[carsList[i][5]]
    obj_ac = b_ac_list[carsList[i][0]]*m_ac_list[carsList[i][1]]*d_ac_list[carsList[i][2]]*p_ac_list[carsList[i][3]]*lb_ac_list[carsList[i][4]]*s_ac_list[carsList[i][5]]
    obj_go = b_go_list[carsList[i][0]]*m_go_list[carsList[i][1]]*d_go_list[carsList[i][2]]*p_go_list[carsList[i][3]]*lb_go_list[carsList[i][4]]*s_go_list[carsList[i][5]]
    obj_vgo = b_vgo_list[carsList[i][0]]*m_vgo_list[carsList[i][1]]*d_vgo_list[carsList[i][2]]*p_vgo_list[carsList[i][3]]*lb_vgo_list[carsList[i][4]]*s_vgo_list[carsList[i][5]]

    obj_max = float(max(obj_ac,obj_un,obj_go,obj_vgo))

    if(math.isclose(obj_max, obj_un, rel_tol=1e-5)):
        if (carsList[i][6] == 0):
            valid += 1
        else:
            invalid += 1
    elif (math.isclose(obj_max, obj_ac, rel_tol=1e-5)):
        if (carsList[i][6] == 1):
            valid += 1
        else:
            invalid += 1
    elif (math.isclose(obj_max, obj_go, rel_tol=1e-5)):
        if (carsList[i][6] == 2):
            valid += 1
        else:
            invalid += 1
    elif (math.isclose(obj_max, obj_vgo, rel_tol=1e-5)):
        if (carsList[i][6] == 3):
            valid += 1
        else:
            invalid += 1
    
# print(obj_un,obj_ac,obj_go,obj_vgo,obj_max)

accuracy = valid/(i-trainNumber)
print("Accuracy is: "+ str(accuracy)+ " of "+ str(int(trainNumber))+" subjects for training ("+ str(trainPercentage*100)+ "%) and "+ str(i - int(trainNumber))+ " subjects for testing")