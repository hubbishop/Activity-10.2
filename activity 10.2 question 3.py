__author__ = 'Dark-Knight'

m = [8, 2, 4, 3, 6, 5, 7, 1]
print(m)
for i in range(1, len(m)):
    for i in range(len(m)-1):
        if m[i] > m[i+1]:
            temp = m[i]
            m[i] = m[i+1]
            m[i+1] = temp
print(m)

# It puts the numbers in order pretty cool Dr. Cook