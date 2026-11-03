# import numpy as np

# a = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# print("Array:", a)
# print("Size:", a.size)
# print("Data Type:", a.dtype)
# print("Dimensions:", a.ndim)import numpy as np





# a = np.array([10, 20, 30, 40, 50])
# b = np.array([2, 4, 5, 8, 10])

# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("Modulus:", a % b)




# import numpy as np

# a = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# print("Maximum:", np.max(a))
# print("Minimum:", np.min(a))
# print("Sum:", np.sum(a))
# print("Average:", np.mean(a))




# import numpy as np

# a = np.arange(1, 21)

# even = a[a % 2 == 0]
# odd = a[a % 2 != 0]

# print("Even Numbers:", even)
# print("Odd Numbers:", odd)






# import numpy as np

# a = np.arange(1, 13)

# print("Original Array:", a)

# print("2 x 6 Matrix:")
# print(a.reshape(2, 6))

# print("3 x 4 Matrix:")
# print(a.reshape(3, 4))

# print("4 x 3 Matrix:")
# print(a.reshape(4, 3))










# import numpy as np

# a = np.array([[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]])

# b = np.array([[9, 8, 7],
#               [6, 5, 4],
#               [3, 2, 1]])

# print("Addition:")
# print(a + b)









# import numpy as np

# a = np.array([[1, 2],
#               [3, 4]])

# b = np.array([[5, 6],
#               [7, 8]])

# c = np.dot(a, b)

# print("Matrix Multiplication:")
# print(c)








# import numpy as np

# a = np.array([[1, 2, 3, 4],
#               [5, 6, 7, 8],
#               [9, 10, 11, 12]])

# print("Original Matrix:")
# print(a)

# print("Transpose:")
# print(a.T)











# import numpy as np

# a = np.arange(1, 17).reshape(4, 4)

# print("Matrix:")
# print(a)

# print("First Row:", a[0])
# print("Last Column:", a[:, -1])
# print("Diagonal:", np.diag(a))
# print("Second and Third Rows:")
# print(a[1:3])











# import numpy as np

# a = np.arange(1, 17).reshape(4, 4)

# print("Matrix:")
# print(a)

# print("Row Sum:", np.sum(a, axis=1))
# print("Column Sum:", np.sum(a, axis=0))





# import numpy as np

# a = np.arange(1, 21)

# print("First 5:", a[:5])
# print("Last 5:", a[-5:])
# print("Alternate Elements:", a[::2])
# print("Reverse:", a[::-1])




# import numpy as np

# a = np.array([10, 20, 40, 50, 60, 70, 80, 30, 90, 100])

# a[a > 50] = 0

# print("Updated Array:", a)











# import numpy as np

# a = np.array([50, 10, 40, 20, 30])

# print("Ascending:", np.sort(a))
# print("Descending:", np.sort(a)[::-1])









# import numpy as np

# a = np.array([10, 20, 10, 30, 20, 40, 50, 30])

# print("Unique Elements:", np.unique(a))







# import numpy as np

# a = np.array([[1, 2],
#               [3, 4]])

# b = np.array([[5, 6],
#               [7, 8]])

# print("Horizontal:")
# print(np.hstack((a, b)))

# print("Vertical:")
# print(np.vstack((a, b)))