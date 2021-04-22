#!/usr/bin/env python3

count = 0
while True:
    
    try:
        n, m = map(int, input().split(" "))
    except:
        exit()

    groups = dict()
    atoms = dict()

    for i in range(n):
        groups[str(i+1)] = [i+1]
        atoms[str(i+1)] = str(i+1)

    for i in range(m):
        operation = input().split(" ")
        
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

        else:

            atomP = operation[1]
            setPKEY = str(atoms[atomP])

            print(f"{len(groups[setPKEY])} {sum(groups[setPKEY])}")

    # if count > 1:
    #     x = 1/0
    # count += 1