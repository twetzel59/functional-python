from functional import *

#xs = List.Cons(4, List.Cons(5, List.Cons(6, List.Nil)))
#xs = List.new(4,5,6)

xs = List.new(*range(1, 101))
List.printls(xs)
