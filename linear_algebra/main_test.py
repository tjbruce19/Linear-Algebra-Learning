from linear_algebra.Vector import Vector

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
    zero = Vector.zero(2)
    print(zero)
    print(vec.norm())
    print(vec2.norm())
    print(vec.normalize())
    print(vec2.normalize())
    print(vec.normalize().norm())
    print(vec2.normalize().norm())
    try:
        print(zero.normalize())
    except ZeroDivisionError:
        print("zero vector {} can't be normal".format(zero) )

    print(vec.dot(vec2))