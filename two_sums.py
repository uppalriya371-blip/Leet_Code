# question no.1 

list=[2,4,6,8,10]
target=6 
class solution:
    def twosum(self,nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums [i]+ nums[j]==target:
                    return (i,j) 
            