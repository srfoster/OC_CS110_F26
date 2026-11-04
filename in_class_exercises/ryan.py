list = ["bob", "alice", "john", "mary"]
numbered_list = list.copy()
for i in range(len(numbered_list)):
    numbered_list[i] = f"{i + 1}. {numbered_list[i]}"
numbered_list.sort()
print(numbered_list[::-1])
