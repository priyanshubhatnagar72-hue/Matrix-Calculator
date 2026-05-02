import numpy as np

def input_matrix(name):
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    print(f"Enter elements of {name} row-wise:")
    
    elements = list(map(float, input().split()))
    matrix = np.array(elements).reshape(rows, cols)
    return matrix
  
A = input_matrix("Matrix A")
B = input_matrix("Matrix B")

print("\nMatrix A:\n", A)
print("\nMatrix B:\n", B)

# Operations
print("\nChoose operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Transpose (A)")
print("5. Determinant (A)")
print("6. Inverse (A)")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Result:\n", A + B)

elif choice == 2:
    print("Result:\n", A - B)

elif choice == 3:
    print("Result:\n", np.dot(A, B))

elif choice == 4:
    print("Transpose of A:\n", A.T)

elif choice == 5:
    print("Determinant of A:\n", np.linalg.det(A))

elif choice == 6:
    print("Inverse of A:\n", np.linalg.inv(A))

else:
    print("Invalid choice")