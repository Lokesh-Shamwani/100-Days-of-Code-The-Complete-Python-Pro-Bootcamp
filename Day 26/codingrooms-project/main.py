with open("file1.txt") as f1:
    dataf1 = f1.readlines()

with open("file2.txt") as f2:
    dataf2 = f2.readlines()

result = [int(num) for num in dataf1 if num in dataf2]

# Write your code above 👆

print(result)
