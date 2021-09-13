
height=[1,8,6,2,5,4,8,3,7]
res=0
width=8
l=0

r=len(height)-1
while l<r:
    length=min(height[l],height[r])
    area = length*width
    
    res=max(res,area)

    if height[l]<height[r]:
        l=l+1
        width-=1
    else:
        r=r-1
        width=width-1
print(res)
        
        







