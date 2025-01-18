# Sequence : tuple , list , dictionary , sets. also known as data types.
# Operations -> if you want to perform any task on these sequnces . you need operatoions.
# select , max , min , concatinate 

# Top 10 operations
# selection is driven by - indexing
Rajat_list = [10,20,30,40,50,60,70]
print(Rajat_list[2])

# length
print(len(Rajat_list))

# slicing 
print(Rajat_list[1:4])

# concatination
rajat_tuple = (1,2,3,4,5,6,7,8)
rajat_tuple1 = (9,10)
print(rajat_tuple + rajat_tuple1)

# max , min , sum
print(max(rajat_tuple))
print(min(rajat_tuple))
print(sum(rajat_tuple))

# count
raj_tuple = "Hello Rajat "
print(raj_tuple.count('a'))

# membership
my_list = [1,2,3,4,5]
print(3 in my_list)