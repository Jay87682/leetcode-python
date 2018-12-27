#!/usr/bin/python3

######### dir() #########
"""
List all attributes and methods of objects
"""
# print(dir())
# print(dir(object()))
# print(dir(list()))
# print(dir(tuple()))
# print(dir(set()))

######### immutable objects ########
"""
id(memory address) of x will be modified which means
it reallocate object.
"""
# x = "test"
# print(hex(id(x)))
# x = "test2"
# print(hex(id(x)))

"""
y and z have the the same id
"""
# y = "the same"
# z = "the same"
# print(hex(id(y)))
# print(hex(id(z)))

######### mutable objects ########
"""
a and b will have different id
"""
# a = []
# b = []
# print(hex(id(a)))
# print(hex(id(b)))

"""
Note: a and b will have the same id in this case
"""
# a = b = ['123', '456']
# a.append('789')
# print(hex(id(a)))
# print(hex(id(b)))
# print(b)    #['123', '456', '789']

######### Numbers lib ########
# import numbers
"""
numbers.Integral includes integer and boolean
"""
# intg = 8.7
# boo = False
# print("is int" if isinstance(intg, numbers.Integral) else "not int")
# print("is bool" if isinstance(boo, numbers.Integral) else "not bool")

"""
numbers.Real: float (include integer)
"""
# float_t = 3
# print("Is real" if isinstance(float_t, numbers.Real) else "Not real")


######### Object destory ########
"""
del and None
"""
# foo = 3
# print(id(foo))
## after "del" statement, any reference to "foo" will occur "NameError".
## Namely: unbound!
# del foo
## Reference still be alive
# foo = None
# print(id(foo))

######### Sequence ########
### Finite ordered sets indexed by non-negative numbers
### Supporting slice: a[i:j]
"""
Immutable sequences
"""
## string
# test_s = "test"
# print(test_s[0])
# test_s[0] = "k"  # Will error

## tuples
# tuple_t = (1, "2", 3+1j)
# print(id(tuple_t))
# print(tuple_t.__hash__())
# print(tuple_t.__eq__((1, "2", 3+2j)))
# del tuple_t[0] # Will error
# tuple_t[0] = 3  # Will error

"""""
Note1: Hashing and Immutability are related
    Because objects which are used hash keys must typically be immutable so that
the hash value doesn't change.
For instance:

    tuple_t = (1, "2", 3+1j)
    print(id(tuple_t))
    print(tuple_t.__hash__())
    tuple_t = tuple_t + (1)
    print(id(tuple_t))
    print(tuple_t.__hash__())

Note2: Hashing is the process of converting some large amount of data into a much
smaller amount(ex: integer). The look up in a table in constant-time O(1).

"""""


"""
Mutable sequences
"""
## list
# list_t = [ 1, "2", 3+4j]
# list_t[0] = "1"  # Fine!!
## del is supporting.
## After "del list_t[k]", {i > k, list_t[i] will be list_t[i-1]}
# del list_t[0]


######### Set ########
## Unordered finite sets of unique, immutable objects. Set is mutable
## "Set" cannot be indexed by any subscript but support iterated over.
## Common use: Fast membership testing, removing duplicates from a sequence,
##             computing mathematical operations (intersection, union, difference
##             and symmetric difference)
"""
Mutable
"""
## ini
# admin = {'jayhuang', 'rory'} # In Python3, "set" could be init via {}
# user = 'jayhuang'
# print("Welcome " + user if user in admin else "Illeague user " + user)
# admin.add('kevin')
# admin.remove('rory')
# print("admin set : \n" + " length: " + str(len(admin)) + "\n" + " content: " + str(admin))
# users = {'jayhuang', 'jeff', 'johnny'}
## xor: delete the same items
# print( "and op: " + str(admin & users) + "\n" +
#        "or op:" + str(admin | users) + "\n" +
#        "xor op:" + str(admin ^ users) + "\n" +
#        "diff op :" + str(admin - users))
# print(admin.__xor__(users)) # the method of the operator


## ini a empty set
# family = {}  ## Error! It will define the empty dic.
# family = set()   ## Correct format to define empty set
# print(type(admin))

## ini a char set
## ini an char set (not string)
# charset = set('abcde')
# print(charset)
# stringset = { 'abcde' }
# print(stringset)
## Note: The item of set should be hashable
## Foe the object without implementing the __hash__() and __eq__(), it should be unhashable.
# errorset = {[1, 2, 3, 4]} # Error. Due to list is mutable(unhashable)
# numberset = set([1, 2, 3, 4]) # Correct!!
# print(numberset)

## add and update
# family = {'lili', 'kely'}
# family.add({'joe', 'hua'})  #Error due to set is unhashable
# family.add(['joe', 'hua'])  #Error due to list is unhashable
# # Correct, like: for name in {'joe', 'hua'} family.add(name)
# family.update({'joe', 'hua'})
# print(family)

## For set operation(|, &, ^), python will check the operands should
## all are set type or it will omit type error.
# list_t = ['jay', 'joe', 'jackson']
# tuple_t = ('jay', 'joe', 'jackson')
# set_t = {'justin', 'jay'}
# print(list_t & set_t)  # Error, due to unsupport
## For different types, it can work with method.
# print(set_t.union(list_t)) # Work!
# print(set_t.union(tuple_t)) # Work!


################ Mapping ###############
## Finite sets of objects indexed by arbitrary index sets.
## a[k] selects item indexed by k from the mapping a, and
## this could be the target of assignment or del statements.
"""
 dict() is mutable. There is no __hash__ implement
"""
## The key should be immutable (object with __hash__, eg: tuple,
## integer, string, ...etc)
# dict_t = { {1,2,3}: 123, 456: 456}  # work! tuple is immutable
# dict_t = { [1,2,3]: 123, 456: 456}  # error! list is mutable
# print(dict_t[(1,2,3)])
## Add new item  (dict has no add or __add__)
# password = { "jay": 123, "joe": 456 }
## For duplicated keys, the later will replace the previous one
# password = { 1: 12345, 2: 456, 1:1234 } # password is {1:1234, 2:456}

## Using the dict to init
# password = dict( jay=123, joe=456 )
# password.update({"jeff": 789})
# print(password)
## Check the key exist or not
# user = "jay"
# print( user + " is in" if user in password else  user + " not find")

## Get the item if not exist return the default value
# print(password.get("ken", "No password"))

## Take the item (key, value) which is presented as tuple.
# print(password.items()) #([('joe', 456), ('jay', 123)])
## Apply the set operator
# print({'x', 'y'}.union(password.items()))
## Note: Using |, &, ^ will error.
# password.items() | { 'x', 'y' } # Error. Need to use function.


## Get the keys only which is presented as list
# print(password.keys())
## Apply the set operator
# print({'x', 'y'}.union(password.keys()))
## Note: Using |, &, ^ will error. Because list can access set
## via operator directly.
# password.keys() | { 'x', 'y' } # Error. Need to use function.


## Get the values only which is presented as list
## Like items(), keys() function. Able to apply the set operation function.
# print(password.keys()) #['joe', 'jay']
# print(password.values()) #[456, 123]
