import random

def sim_monty_hall(n):
    switchwin=0
    staywin=0
    for j in range(n):
        car_door=random.randint(0,2)
        initial_pick=random.randint(0,2)
        
        remaining_doors=[i for i in range(0,3) if i!=car_door and i!=initial_pick]

        host_pick=random.choice(remaining_doors)

        #find the door that contestant can switch to
        for door in range(3):
            if door!=initial_pick and door !=host_pick:
                switch_choice=door;
        
        #is car behind the switch choice?
        if car_door==switch_choice:
            switchwin+=1
        else:
            staywin+=1

    print(switchwin/n)
    print(staywin/n)

sim_monty_hall(1000)


