

def solve():
    result = 0
    
    with open('input/day2.txt', 'r') as file:
        f = file.read()
        
        for line in f.splitlines():
            data = list(map(int, line.split()))
            
            if is_safe(data):
                result += 1
    
    return result

def is_safe(row):
    inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
        return True
    return False

def solve2():
    with open('input/day2.txt', 'r') as file:
        f = file.read()
        def is_safe(nums, safe_range, allow_skip):
            prev = nums[0]
            for curr in nums[1:]:
                if curr - prev in safe_range:
                    prev = curr
                elif not allow_skip:
                    return False
                else:
                    allow_skip = False
            return True
        
        safe = 0
        increasing = range(1, 4)
        decreasing = range(-3, 0)
        for line in f.split('\n'):
            nums = [int(num) for num in line.split()]
            safe += any([
                is_safe(nums, increasing, True), 
                is_safe(nums, decreasing, True),
                is_safe(nums[1:], increasing, False),
                is_safe(nums[1:], decreasing, False)
            ])

        return safe



if __name__ == "__main__":
    print(solve())
    print(solve2())