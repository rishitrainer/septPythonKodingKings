import numpy as np

'''
test_list = [1,2,3,4,5]
float_list = []
for eachInt in test_list:
    float_list.append(float(eachInt))
print(float_list)
'''


a = np.array([1,2,3,4,5] ,dtype='i4', ndmin = 2)
print(a)

a = np.array([[1, 2], [3, 4]])
print(a)

a = np.array([[[1, 2], [3, 4]], [[5,6], [7,8]]])
print(a)

dt_age = np.dtype([('age',np.int16)])
a = np.array([(15,),(20,),(17,)], dtype = dt_age)
print(a)

dt_student = np.dtype([('name','S20'), ('age', 'i2'), ('marks', 'f4')])
a = np.array([('Mr David Pattrick Harris', 21, 50),('Niel', 18, 75), ('Ram', 19, 85)], dtype = dt_student)
print(a)
