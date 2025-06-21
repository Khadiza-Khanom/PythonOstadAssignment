
A = set(map(int,input("Enter a set named A: ").split()))
B = set(map(int,input("Enter a set named B: ").split()))

# A={1,2,3,4,5}
# B={4,5,6,7,8}

print(f"Here is the union of A and B: {A.union(B)}")
print(f"Here is the union of A and B: {A.intersection(B)}")
print(f"Here is the union of A and B: {A.difference(B)}")