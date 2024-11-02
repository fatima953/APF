#Advanced Python Functions
#add two lists using map and lambda
nums1 = [3,5,8]
nums2 = [5,6,2]
resault = map(lambda x,y: x + y, nums1, nums2)
print("Addition of two lists")
print(list(resault))

#Zip
s1 = {2,3,4}
s2 = {5,6,7}
s3 = list(zip(s1,s2))
print(s3)