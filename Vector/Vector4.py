class Vec4():
    def __init__(self, x=0, y=0, z=0, w=0):
        """Constructor for Vec4
        DO NOT MODIFY THIS METHOD"""
        self.values = [x, y, z, w]

    def __str__(self):
        """Returns the vector as a string representation
        DO NOT MODIFY THIS METHOD"""
        toReturn = ''
        if self is None: return '0.00 0.00 0.00 0.00'
        for c in range(0, 4):
            toReturn += "%.2f" % self.values[c]
            if c != 3:
                toReturn += ' '
        return toReturn

    def mul(self, v):
        """Element wise multiplication of self by vector v
        Returns the result as a new vector"""
        return Vec4(self.values[0]*v.values[0], self.values[1]*v.values[1], self.values[2]*v.values[2], \
                  self.values[3]*v.values[3])


    def mulc(self, c):
        """Element wise multiplication of vec4 by constant c
        Returns the result as a new vector"""
        return Vec4(self.values[0] * c, self.values[1] * c, self.values[2] *c, \
                self.values[3] *c)


    def add(self, v):
        """Element wise addition of vec4 by vector v
        Returns the result as a new vector"""
        return Vec4(self.values[0] + v.values[0], self.values[1] + v.values[1], self.values[2] + v.values[2], \
                     self.values[3] + v.values[3])


    def addc(self, c):
        """Element wise addition of vec4 by constant c
        Returns the result as a new vector"""
        return Vec4(self.values[0] + c, self.values[1] + c, self.values[2] + c, \
                     self.values[3] + c)


    def sub(self, v):
        """Element wise subtraction of vec4 by vector v
        Returns the result as a new vector"""
        return Vec4(self.values[0] - v.values[0], self.values[1] - v.values[1], self.values[2] - v.values[2], \
                  self.values[3] - v.values[3])


    def subc(self, c):
        """Element wise subtraction of vec4 by constant
        Returns the result as a new vector"""
        return Vec4(self.values[0] - c, self.values[1] - c, self.values[2] - c, \
                      self.values[3] - c)


    def cross(self, v):
        """Returns the cross product of self and vector v, ignore w in calculations
        and set w of the resulting vector to 1"""
        return  Vec4(self.values[1] * v.values[2] - self.values[2] * v.values[1], self.values[2] * v.values[0] - self.values[0] * v.values[2], self.values[0] * v.values[1] - self.values[1] * v.values[0], 1)




    def dot(self, v):
        """Returns the dot product of self and vector v"""
        return self.values[0] * v.values[0] + self.values[1] * v.values[1] + self.values[2] * v.values[2] \
                    + self.values[3] * v.values[3]



class Matrix4():
    def __init__(self, row1=None, row2=None, row3=None, row4=None):
        """Constructor for Matrix4
        DO NOT MODIFY THIS METHOD"""
        if row1 is None: row1 = Vec4()
        if row2 is None: row2 = Vec4()
        if row3 is None: row3 = Vec4()
        if row4 is None: row4 = Vec4()
        self.m_values = [row1, row2, row3, row4]

    def __str__(self):
        """Returns a string representation of the matrix
        DO NOT MODIFY THIS METHOD"""
        toReturn = ''
        if self is None: return '0.00 0.00 0.00 0.00\n0.00 0.00 0.00 0.00\n0.00 0.00 0.00 0.00\n0.00 0.00 0.00 0.00'
        for r in range(0, 4):
            for c in range(0, 4):
                toReturn += "%.2f" % self.m_values[r].values[c]
                if c != 3:
                    toReturn += ' '
            toReturn += '\n'
        return toReturn

    def setIdentity(self):
        """Sets the current Matrix to an identity matrix
        self is an identity matrix after calling this method"""
        vector_1000 = Vec4(1,0,0,0)
        vector_0100 = Vec4(0,1,0,0)
        vector_0010 = Vec4(0,0,1,0)
        vector_0001 = Vec4(0,0,0,1)
        self.m_values =[vector_1000, vector_0100, vector_0010, vector_0001]







    def mulV(self, vector):
        """Multiplication: Matrix times vector.
            'vector' is the vector with which to multiply.
            Return the result as a new Vec4.
            Make sure that you do not change self or the vector.
            return self * v"""
        return Vec4(self.m_values[0].values[0]*vector.values[0] + self.m_values[0].values[1]*vector.values[1] + self.m_values[0].values[2]*vector.values[2] + self.m_values[0].values[3]*vector.values[3], \
                    self.m_values[1].values[0]*vector.values[0] + self.m_values[1].values[1]*vector.values[1] + self.m_values[1].values[2]*vector.values[2] + self.m_values[1].values[3]*vector.values[3], \
                    self.m_values[2].values[0]*vector.values[0] + self.m_values[2].values[1]*vector.values[1] + self.m_values[2].values[2]*vector.values[2] + self.m_values[2].values[3]*vector.values[3], \
                    self.m_values[3].values[0]*vector.values[0] + self.m_values[3].values[1]*vector.values[1] + self.m_values[3].values[2]*vector.values[2] + self.m_values[3].values[3]*vector.values[3])









    def roundM(self):
        """Rounds every entry in the matrix"""

        for r in range(0,4):
            for c in range(0,4):
                self.m_values[r].values[c] = round(self.m_values[r].values[c])
        return





    def mulM(self, m):
        """Multiplication: Matrix times Matrix.
            m is the matrix with which to multiply.
            Return the result as a new Matrix4.
            Make sure that you do not change self or the other matrix.
            return this * m"""
        return Matrix4(
            Vec4(
                self.m_values[0].dot(m.column(0)),
                self.m_values[0].dot(m.column(1)),
                self.m_values[0].dot(m.column(2)),
                self.m_values[0].dot(m.column(3))),
            Vec4(
                self.m_values[1].dot(m.column(0)),
                self.m_values[1].dot(m.column(1)),
                self.m_values[1].dot(m.column(2)),
                self.m_values[1].dot(m.column(3))),
            Vec4(
                self.m_values[2].dot(m.column(0)),
                self.m_values[2].dot(m.column(1)),
                self.m_values[2].dot(m.column(2)),
                self.m_values[2].dot(m.column(3))),
            Vec4(
                self.m_values[3].dot(m.column(0)),
                self.m_values[3].dot(m.column(1)),
                self.m_values[3].dot(m.column(2)),
                self.m_values[3].dot(m.column(3))),
        )











