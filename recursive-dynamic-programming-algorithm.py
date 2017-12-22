def total_value(items, max_weight):
    return  sum([x[2] for x in items]) if sum([x[1] for x in items]) < max_weight else 0
 
cache = {}
def solve(items, max_weight):
    if not items:
        return ()
    if (items,max_weight) not in cache:
        head = items[0]
        tail = items[1:]
        include = (head,) + solve(tail, max_weight - head[1])
        dont_include = solve(tail, max_weight)
        if total_value(include, max_weight) > total_value(dont_include, max_weight):
            answer = include
        else:
            answer = dont_include
        cache[(items,max_weight)] = answer
    return cache[(items,max_weight)]
 
items = (
    ("map", 9, 150), ("compass", 13, 35), ("water", 153, 200), ("sandwich", 50, 160),
    ("glucose", 15, 60), ("tin", 68, 45), ("banana", 27, 60), ("apple", 39, 40),
    ("cheese", 23, 30), ("camera", 32, 30),
    )
max_weight = 400
 
solution = solve(items, max_weight)
print "items:"
for x in solution:
    print x[0]
print "value:", total_value(solution, max_weight)
print "weight:", sum([x[1] for x in solution])
