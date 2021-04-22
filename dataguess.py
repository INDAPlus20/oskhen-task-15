#!/usr/bin/env python3
# Types: stack/queue/prio/not sure/impossible

while True:
    try:
        n = input()
    except:
        exit()
    if n == "":
        exit()

    n = int(n)

    stack_bag = list()
    queue_bag = list()
    prio_bag = list()

    bagtype = [True]*3

    for _ in range(n):
        line = list(map(int, input().split(" ")))

        prio_bag.sort()

        if line[0] == 1:
            stack_bag.append(line[1])
            queue_bag.append(line[1])
            prio_bag.append(line[1])

        elif line[0] == 2:
                # Check Stack
                if bagtype[0] != False:

                    if len(stack_bag) == 0:
                        bagtype[0] = False
                    else:
                        if line[1] != stack_bag[-1]:
                            bagtype[0] = False
                        else:
                            stack_bag.pop()

                # Check Queue
                if bagtype[1] != False:

                    if len(queue_bag) == 0:
                        bagtype[1] = False
                    else:
                        if line[1] != queue_bag[0]:
                            bagtype[1] = False
                        else:
                            queue_bag.pop(0)

                # Check Prio
                if bagtype[2] != False:

                    if len(prio_bag) == 0:
                        bagtype[2] = False
                    else:
                        if line[1] != prio_bag[-1]:
                            bagtype[2] = False
                        else:
                            prio_bag.pop()



    if sum(bagtype) > 1:
        print("not sure")
    elif sum(bagtype) == 0:
        print("impossible")
    elif bagtype == [True, False, False]:
        print("stack")
    elif bagtype == [False, True, False]:
        print("queue")
    elif bagtype == [False, False, True]:
        print("priority queue")

