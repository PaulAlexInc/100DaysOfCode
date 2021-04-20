row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

#user input is of the form 23, where 2 is the column, 3 is the row according to the user(swapped from conventional matrx)
i=int(position[0]);
j=int(position[1]);
map[j-1][i-1]="X"

print(f"{row1}\n{row2}\n{row3}")

# # Example Input 1

# column 2, row 3 would be entered as:

# ```
# 23
# ```

# # Example Output 1

# ```
# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', 'X', '⬜️']
# ```

# # Example Input 2

# column 3, row 1 would be entered as:

# ```
# 31
# ```

# # Example Output 2

# ```
# ['⬜️', '⬜️', 'X']

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']
# ```