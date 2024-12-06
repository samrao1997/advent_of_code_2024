

def solve():
    with open('input/day1.txt', 'r') as file:
        f = file.read()
        
        list1 = []
        list2 = []

        for line in f.splitlines():
            data = line.split()
            list1.append(int(data[0]))
            list2.append(int(data[1]))

        list1.sort()
        list2.sort()

        iter = 0
        distance = []
        for _ in range(0 , len(list1)):
            distance.append(abs(list1[iter] - list2[iter]))
            iter += 1

    return sum(distance)
    
    
def solve2():
    with open('input/day1.txt', 'r') as file:
        f = file.read()
        
        list1 = []
        list2 = []

        for line in f.splitlines():
            data = line.split()
            list1.append(int(data[0]))
            list2.append(int(data[1]))

        list1.sort()
        list2.sort()

        iter = 0
        distance = []
        for _ in range(0 , len(list1)):
            distance.append(abs(list1[iter] - list2[iter]))
            iter += 1
    similarty = []
    
    for number in list1:
        x = [1 for x in list2 if x == number]
        similarty.append(number*(sum(x)))

    return sum(similarty)
    
    




if __name__ == "__main__":
    print(solve())
    print(solve2())
