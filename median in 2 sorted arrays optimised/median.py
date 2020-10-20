class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a1,a2=sorted([nums1,nums2],key=lambda x:len(x))
        n1,n2=len(a1),len(a2)
        b,e=0,n1
        while(b<=e):
            i1=(b+e)//2
            i2=(n1+n2+1)//2-i1
            min1,min2=float('inf') if(i1==n1) else a1[i1],float('inf') if(i2==n2) else a2[i2]
            max1,max2=float('-inf') if(i1==0) else a1[i1-1],float('-inf') if(i2==0) else a2[i2-1]
            print(min1,max1,min2,max2,i1,i2,b,e,a1,a2)
            if(min1>=max2 and min2>=max1):
                if((n1+n2)%2==0):
                    return sum([max(max1,max2),min(min1,min2)])/2
                
                return max(max1,max2)
            elif(max1>min2):
                e=i1-1
            else:
                b=i1+1
        return 1