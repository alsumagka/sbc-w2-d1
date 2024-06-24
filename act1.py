nums = []
while len(nums) < 5:
    user = input("Enter a number: ")
    nums.append(user)

while nums:
    command = input("Command: ").lower().split()
    nums.pop(0) if command[0] == "naa" else ""
    nums.pop() if command[0] == "wala" else ""
    print(nums if command[0] == "display" else "")
    nums.append(command[1]) if command[0] == "add" else ""