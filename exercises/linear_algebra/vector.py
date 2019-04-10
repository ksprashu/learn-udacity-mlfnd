import math
from decimal import Decimal, getcontext

getcontext().prec = 15

CANNOT_NORMALIZE_ZERO_MSG = 'Cannot normalize Zero vector'
CANNOT_COMPUTE_ANGLE_ZERO_MSG = 'Cannot compute an angle with a Zero vector'
NO_PARALLEL_COMPONENT_MSG = 'There is no parallel component of this projection'
NO_ORTHOGONAL_COMPONENT_MSG = 'There is no orthogonal component'\
    ' to this projection'


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
        return 'Vector: {}'.format(tuple(round(float(x), 3)
                                         for x in self.coordinates))

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
        return round(math.sqrt(sum(squared_coords)), 3)

    def normalized(self):
        try:
            magni = self.magnitude()
            return self.times_scalar(Decimal('1.0')/Decimal(magni))

        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_MSG)

    def dot(self, v):
        coords = [x*y for x, y in zip(self.coordinates, v.coordinates)]
        return round(sum(coords), 3)

    def angle_with(self, v, in_degrees=False):
        try:
            radians = math.acos(self.normalized().dot(v.normalized()))
            return round(radians, 3) if in_degrees is False \
                else round(math.degrees(radians), 3)

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_MSG:
                raise Exception(self.CANNOT_COMPUTE_ANGLE_ZERO_MSG)
            else:
                raise e

    def is_parallel_to(self, v):
        return (self.is_zero() or
                v.is_zero() or
                self.angle_with(v) == 0 or
                self.angle_with(v) == math.pi)

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    # orthogonal if dot product is zero
    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance

    def projection_on(self, b):
        try:
            unit_b = b.normalized()
            scalar = self.dot(unit_b)
            return unit_b.times_scalar(scalar)
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_MSG:
                raise Exception(self.NO_PARALLEL_COMPONENT_MSG)
            else:
                raise e

    def orthogonal_to(self, b):
        try:
            proj_v = self.projection_on(b)
            return self.minus(proj_v)
        except Exception as e:
            if str(e) == self.NO_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_ORTHOGONAL_COMPONENT_MSG)
            else:
                raise e

    def cross(self, v):
        x1, y1, z1 = self.coordinates
        x2, y2, z2 = v.coordinates

        cross_x = y1*z2 - y2*z1
        cross_y = Decimal("-1.0") * (x1*z2 - x2*z1)
        cross_z = x1*y2 - x2*y1

        return Vector([cross_x, cross_y, cross_z])

    def area_parallelogram(self, v):
        return self.cross(v).magnitude()

    def area_triangle(self, v):
        return self.area_parallelogram(v) * 0.5

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
print(v.normalized())

v = Vector([1.996, 3.108, -4.554])
print(v.normalized())

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
print('first pair; parallel = {}, orthogonal = {}'
      .format(v.is_parallel_to(w), v.is_orthogonal_to(w)))

v = Vector([-2.029, 9.97, 4.172])
w = Vector([-9.231, -6.639, -7.245])
print('second pair; parallel = {}, orthogonal = {}'
      .format(v.is_parallel_to(w), v.is_orthogonal_to(w)))

v = Vector([-2.328, -7.284, -1.214])
w = Vector([-1.821, 1.072, -2.94])
print('third pair; parallel = {}, orthogonal = {}'
      .format(v.is_parallel_to(w), v.is_orthogonal_to(w)))

v = Vector([2.118, 4.827])
w = Vector([0, 0])
print('fourth pair; parallel = {}, orthogonal = {}'
      .format(v.is_parallel_to(w), v.is_orthogonal_to(w)))

# projections
v = Vector([3.039, 1.879])
w = Vector([0.825, 2.036])
print(v.projection_on(w))

v = Vector([-9.88, -3.264, -8.159])
w = Vector([-2.155, -9.353, -9.473])
print(v.orthogonal_to(w))

v = Vector([3.009, -6.172, 3.692, -2.51])
w = Vector([6.404, -9.144, 2.759, 8.718])
print(v.projection_on(w))
print(v.orthogonal_to(w))


# cross product and areas
v = Vector([8.462, 7.893, -8.187])
w = Vector([6.984, -5.975, 4.778])
print(v.cross(w))

v = Vector([-8.987, -9.838, 5.031])
w = Vector([-4.268, -1.861, -8.866])
print(v.area_parallelogram(w))

v = Vector([1.5, 9.547, 3.691])
w = Vector([-6.007, 0.124, 5.772])
print(v.area_triangle(w))
