
def binary_search(key, L):
        if len(L)<0:
                return None

        temp_L=L
        
        while True:
                mid=int(len(temp_L)/2)
                if temp_L[mid]==key:
                        ans=temp_L[mid]
                        return ans
                elif temp_L[mid]<key:
                        temp_L=temp_L[mid:]
                elif temp_L[mid]>key:
                        temp_L=temp_L[:mid]

sumnumbers = [0, 2, 3, 5, 13, 16, 18]
print(binary_search(3,sumnumbers))
