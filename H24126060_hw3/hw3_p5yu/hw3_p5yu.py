res = 0
height = input("Input sequence of seats:")
height = height.split(" ")
height = [int(x) for x in height]

for i in range(len(height)):
    curr = height[i]
    left_array = height[0:i]
    if not left_array:
        left_array = [0]
    right_array = height[i + 1 :]
    if not right_array:
        right_array = [0]
    leftMax = max(left_array)
    rightMax = max(right_array)
    boundary = min(leftMax, rightMax)
    diff = boundary - curr
    if diff > 0:
        res += diff
    else:
        pass

print("Water:",res)
