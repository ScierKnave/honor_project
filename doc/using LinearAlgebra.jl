using LinearAlgebra

v1 = [9 4]
v2 = [6 8]
v3 = [7 3]

u = kron(v1, v2)
println(kron(v1, v2))

println(kron(u, v3))


m1 = 
[
9 4 9; 
9 0 9; 
2 0 2
]


m1t = transpose(m1)
println(m1t)