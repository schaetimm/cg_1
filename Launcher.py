import math
#from Vector.Vector4 import*
from Vector.Matrix import*
def main():
    """A = Matrix4(Vec4(1, 0, 1, 0), Vec4(0, 1, 0, 0), Vec4(0, 0, 1, 0), Vec4(1, 0, 1, 1))
    B = Matrix4(Vec4(0, 15, 25, 20), Vec4(5, 5, 3, 9), Vec4(15, 23, 10, -10), Vec4(32, 5, 5, 5))
    print(A.mulM(B))

    V1 = Vec4(1, 1, 1, 1)
    #print(A.mulV(V1))
    V2 = Vec4(8, 0, 8, 2)
    print(V1.mul(V2))
    V1 = Vec4(20, 25, 65, 20)

    print(V1.mulc(-1))
    A = Matrix4()
    A.setIdentity()
    A.m_values[2].values[1] = -19.3
    A.m_values[2].values[3] = -59.4
    A.m_values[1].values[3] = -59.5
    A.roundM()
    print(A)
    V1 = Vec4(3, 2, 3, 2)
    V2 = Vec4(6, 0, 4, 0)
    V1.add(V2)
    print(V1)
    print(V2)
    V1 = Vec4(8, 0, 0, 9)
    V2 = Vec4(0, 9, 8, 0)
    print("%.1f" % V1.dot(V2))
    V1 = Vec4(2, 4, 2, 0)
    V2 = Vec4(0, 1, 2, 1)
    result = V1.cross(V2)
    result.values[1] = abs(result.values[1])
    print(result)"""
    A = Matrix4(Vec4(1, 0, 0, 0),
                Vec4(0, 1, 0, 0),
                Vec4(0, 0, 1, 0),
                Vec4(0, 0, 0, 1))

    B = Matrix4(Vec4(5, 4, 3, 2),
                Vec4(5, 4, 3, 2),
                Vec4(5, 4, 3, 2),
                Vec4(5, 4, 3, 2))

    print(A * B)


    """ A = ViewportMatrix(3, 0, 15, 15)
    print(A)
    A = Matrix4(Vec4(1, 0, 0, 0),
                Vec4(0, 1, 0, 0),
                Vec4(0, 0, 1, 0),
                Vec4(0, 0, 0, 1))
    V = Vec4(3, 42, 3, 4)
    A * V
    print(V) 

   """
    A = RotationMatrix("y", 180)
    print(A)
    A = ScaleMatrix(Vec4(1, 1, 1))
    print(A)
    A = TranslationMatrix(Vec4(13, 0, 0))
    print(A)
    A = OrthogonalMatrix(-2, 2, -2, 2, -1, 120)
    print(A)
    A = PerspectiveMatrix(-2, 2, -2, 2, -1, 1000)
    print(A)
    A = ViewportMatrix(0, 0, 10, 10)
    print(A)





if __name__ == "__main__":
    main()