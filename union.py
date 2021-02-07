#!/usr/bin/env python3

while True:
    
    try:
        n, m = map(int, input().split(" "))
    except:
        exit()

    commands = list()

    for i in range(m):
        commands.append(input().split(" "))

    #print("\n\n")

    groups = dict()
    atoms = dict()

    for i in range(n):
        groups[str(i+1)] = [i+1]
        atoms[str(i+1)] = str(i+1)



    for operation in commands:
        
        #print(operation)
        command = int(operation[0])

        if command != 3:

            atomP = operation[1]
            atomQ = operation[2]

            setPKEY = str(atoms[atomP])
            setQKEY = str(atoms[atomQ])

            if setPKEY == setQKEY:
                break

            if command == 1:

                for atom in groups[setQKEY]:
                    ## Update atom -> group
                    atoms[str(atom)] = setPKEY
                    ## Update group -> atom
                    groups[setPKEY].append(atom)

                groups.pop(setQKEY)
        
            else: # command == 2

                # update atom -> group
                atoms[str(atomP)] = atoms[str(atomQ)]
                # update group -> atom
                groups[setQKEY].append(int(atomP))
                groups[setPKEY].remove(int(atomP))

                if groups[setPKEY] == []:
                    groups.pop(setPKEY)
            
            # print(groups)
            # print(atoms)
        else:

            atomP = operation[1]
            setPKEY = str(atoms[atomP])

            print(f"{len(groups[setPKEY])} {sum(groups[setPKEY])}")
