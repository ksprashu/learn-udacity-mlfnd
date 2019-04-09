from math import sqrt, acos, degrees, pi
from decimal import Decimal, getcontext

getcontext().prec = 15


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(Decimal(x) for x in coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        v_new = [x+y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(v_new)

    def minus(self, v):
        v_new = [x-y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(v_new)

    def times_scalar(self, c):
        v_new = [x*Decimal(c) for x in self.coordinates]
        return Vector(v_new)

    def magnitude(self):
        squared_coords = [x**Decimal(2) for x in self.coordinates]
        return sqrt(sum(squared_coords))

    def normalize(self):
        try:
            magni = self.magnitude()
            return self.times_scalar(Decimal('1.0')/Decimal(magni))

        except ZeroDivisionError:
            raise Exception('Cannot normalize Zero vector')

    def dot(self, v):
        coords = [x*y for x, y in zip(self.coordinates, v.coordinates)]
        return sum(coords)

    def angle_with(self, v, in_degrees=False):
        try:
            radians = acos(self.normalize().dot(v.normalize()))
            return radians if in_degrees is False else degrees(radians)

        except Exception as e:
            if str(e) == 'Cannot normalize Zero vector':
                raise Exception('Cannot compute an angle with a Zero vector')
            else:
                raise e

    def is_parallel_to(self, v):
        return (self.is_zero() or
                v.is_zero() or
                self.angle_with(v) == 0 or
                self.angle_with(v) == pi)

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    # orthogonal if dot product is zero
    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance

    __repr__ = __str__


# Arithmetic Operations
v = Vector([8.218, -9.341])
w = Vector([-1.129, 2.111])
print(v.plus(w))

v = Vector([7.119, 8.215])
w = Vector([-8.223, 0.878])
print(v.minus(w))

# Scalar product
v = Vector([1.671, -1.012, -0.318])
print(v.times_scalar(7.41))

# Magnitude
v = Vector([-0.221, 7.437])
print(v.magnitude())

v = Vector([8.813, -1.331, -6.247])
print(v.magnitude())

# Normalization
v = Vector([5.581, -2.136])
print(v.normalize())

v = Vector([1.996, 3.108, -4.554])
print(v.normalize())

# Dot product
v = Vector([7.887, 4.138])
w = Vector([-8.802, 6.776])
print(v.dot(w))

v = Vector([-5.955, -4.904, -1.874])
w = Vector([-4.496, -8.755, 7.103])
print(v.dot(w))

# Angle between vectors
v = Vector([3.183, -7.627])
w = Vector([-2.668, 5.319])
print(v.angle_with(w))

v = Vector([7.35, 0.221, 5.188])
w = Vector([2.751, 8.259, 3.985])
print(v.angle_with(w, in_degrees=True))

# parallel and orthogonal
v = Vector([-7.579, -7.88])
w = Vector([22.737, 23.64])
print('first pair')
print("parallel : {}".format(v.is_parallel_to(w)))
print("orthogonal : {}".format(v.is_orthogonal_to(w)))

v = Vector([-2.029, 9.97, 4.172])
w = Vector([-9.231, -6.639, -7.245])
print('second pair')
print("parallel : {}".format(v.is_parallel_to(w)))
print("orthogonal : {}".format(v.is_orthogonal_to(w)))

v = Vector([-2.328, -7.284, -1.214])
w = Vector([-1.821, 1.072, -2.94])
print('third pair')
print("parallel : {}".format(v.is_parallel_to(w)))
print("orthogonal : {}".format(v.is_orthogonal_to(w)))

v = Vector([2.118, 4.827])
w = Vector([0, 0])
print('fourth pair')
print("parallel : {}".format(v.is_parallel_to(w)))
print("orthogonal : {}".format(v.is_orthogonal_to(w)))
