# Buatlah sebuah program yang mendemonstrasikan konversi dari:
# • List menjadi Set
# • Set menjadi List
# • Tuple menjadi Set
# • Set menjadi Tuple
# Tampilkan isi data sebelum dan sesudah konversi.

# List menjadi Set
ini_list=[1,2,3,10,454,5,62,7]
print(ini_list)
print(type(ini_list))

list_jadi_set=set(ini_list)
print(list_jadi_set)
print(type(list_jadi_set))

# Set menjadi List
ini_set={1,5,7,1,3,8,0,3,24,12}
print(ini_set)
print(type(ini_set))

set_jadi_list=list(ini_list)
print(set_jadi_list)
print(type(set_jadi_list))

# Tuple menjadi Set
ini_tuple=(1,4,5,7,2,3,)
print(ini_tuple)
print(type(ini_tuple))

tuple_jadi_set=set(ini_tuple)
print(tuple_jadi_set)
print(type(tuple_jadi_set))

# set menjadi tuple
ini_set_2={1,4,5,7,2,4,5,1,4,89}
print(ini_set_2)
print(type(ini_set_2))

set_jadi_tuple=tuple(ini_set_2)
print(set_jadi_tuple)
print(type(set_jadi_tuple))