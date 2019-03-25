from Vector import Vector

if __name__ == "__main__":
    vec = Vector([5,4])
    print(vec)
    print(len(vec))
    print(vec[0])
    vec2 = Vector([6,1])
    print(vec+vec2)
    print(vec * 3)
    print(3 * vec)
    print(+vec)
    print(-vec)
    print(Vector.zero(0))