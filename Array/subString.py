text = "hello world"
pattern = "world"

n = len(text)
m = len(pattern)

found = False

for i in range(n - m + 1):
    j = 0
    
    while j < m and text[i + j] == pattern[j]:
        j += 1
        
    if j == m:
        print("Substring found at index", i)
        found = True
        break

if not found:
    print("Substring not found")