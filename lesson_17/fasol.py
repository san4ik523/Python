import random
fas = 20
print("у вас ", fas, " фасолей")
igr=int(input("укажите число угроков(2) "))
print ("в игре учавствуйют", igr)
qw = 1
while fas > 0:
    if qw == igr:
        qw = 1
    a=int(input(f"игрок номер 1 сколько уберем? "))
    qw += 1


    if a > 3:
        print("вы можете убирать от 1 до 3")
    fas=fas-a
    print(fas)
    if qw == igr:
        qw = 1
    a=int(input(f"игрок номер 2 сколько уберем? "))
    qw += 1


    if a > 3:
        print("вы можете убирать от 1 до 3")
    fas=fas-a
    print(fas)
    if fas < 0: break
print("вы проиграли игрок номер", qw)