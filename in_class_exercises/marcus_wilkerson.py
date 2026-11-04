shoe_size = [12, 11, 10, 9]
left, right = 0, len(shoe_size) - 1
while left < right:
    shoe_size[left], shoe_size[right] = shoe_size[right], shoe_size[left]
    left += 1
    right -= 1
print(shoe_size)  # [9, 10, 11, 12]
  
  
