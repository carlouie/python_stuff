https://www.youtube.com/watch?v=W8KRzm-HUcc 
courses = ['Math', 'History', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
nums = [1, 5, 2, 4, 3]

print(len(courses))
print(course[0])
print(courses[0:1])


courses.insert(0, 'Art') #List 
courses.extend #similar to append but append would input type of variable at end of list
courses.remove('Math')
courses.pop() #removes end value of list
courses.append() # add item into end of list
courses.reverse() # reverses the list


# sort: sorts list in type of order
courses.sort() or courses.sort(reverse=True)
nums.sort() or courses.sort(reverse=True)
 
sorted_courses = sorted(courses) # need to create new variable w/o altering original


print(courses)
print(nums)


# mathematics stuff

print(sum(nums)) # prints out sum of numbers
print(max(nums)) # prints out largest number in list
print(min(nums)) # prints out lowest number in list


# find the index(place) in list
print(courses.index('Math')) # prints out 0
print(courses.index('English')) # prints out an error

# find the boolean value
print('Math' in courses) # prints out true
print('Art' in courses) # prints out false since value not in courses list


for item in courses:
    print(item)

for index, course in enumerate(courses, start=1):
    print(index, course)
    
    
course_str = ' - '.join(courses)

print(course_str) # PRINTS: History - Math - Physics - CompSci


# TUPLES

tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)


#SETS unordered and no duplicates

cs_courses = {'History', 'Art', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses) # print out unordered sets; does not care about order 

print(cs_courses.intersection(art_courses)) # prints: {'History', 'Art'}
print(cs_coures.difference(art_courses)) # prints: {'Physics', 'CompSci'}
print(cs_courses.union(art_courses)) # prints: {ALL COURSES}

# HOW TO CREATE EMPTY LISTS, TUPLES, SETS

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {}
empty_set = set()



