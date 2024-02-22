## ----------- append and extend -----------
# l = [1, 3, 5]  
# s = [7, 9]
# # l.append(s)
# l.extend(s)
# print(l)

## ------------ sort --------------
# s = [0, -1, 4, 3, 7]
# s.sort(reverse=True)
# print(s)
## ----------- + ------------
# s = [1, 2]
# s2 = [3, 4]

# rst = s + s2
# print(f"s = {s}")
# print(f"rst = {rst}")

# s.extend(s2)
# print(s)


# ------------- * -----------
# s = [1,2]
# a = s * 3
# print(a)

# ------------- in -------------
# s = [1, 2]
# print(1 in s)
# print(3 in s)

# ----------- lists are mutable ---
s = [1, 2]
s[0] = -1
print(s)
