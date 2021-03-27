any(l == 't' for l in 'python') # Returns True. Same as: 't' in 'python'
all(l == 't' for l in 'python') # Returns False. Not all of the letters are 't'.


#iterator - which has next associated with it it goes one by one.
#iterator - like for loop for all in..

#iterator - once used one val it cannot be used again. It goes away
#iterator - we can use it again.



#generators expression
#generator in python 3.x has next(generator) not g.next()
g = (l=='t' for l in 'python')
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
