from decimal import Decimal, getcontext
from vector import Vector

getcontext().prec = 30


class Plane(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 3

        if not normal_vector:
            all_zeros = ['0']*self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()

    def set_basepoint(self):
        try:
            n = self.normal_vector.coordinates
            c = self.constant_term
            basepoint_coords = ['0']*self.dimension

            initial_index = Plane.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e

    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector.coordinates

        try:
            initial_index = Plane.first_nonzero_index(n)
            terms = [write_coefficient(n[i],
                                       is_initial_term=(i == initial_index)) +
                     'x_{}'.format(i+1)
                     for i in range(self.dimension)
                     if round(n[i], num_decimal_places) != 0]

            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output

    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Plane.NO_NONZERO_ELTS_FOUND_MSG)

    def is_parallel_to(self, p):
        n1 = self.normal_vector
        n2 = p.normal_vector
        print(n1.angle_with(n2))
        return n1.is_parallel_to(n2)

    def __eq__(self, p):
        if self.normal_vector.is_zero():
            if not p.normal_vector.is_zero():
                return False
            else:
                diff = self.constant_term - p.constant_term
                return MyDecimal(diff).is_near_zero()
        elif p.normal_vector.is_zero():
            return False

        if not self.is_parallel_to(p):
            return False

        x0 = self.basepoint
        y0 = p.basepoint

        dv = x0.minus(y0)
        n = self.normal_vector

        return dv.is_orthogonal_to(n)


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps


print("--------------------------")
print("start of PLANE operations")
print("--------------------------")

p1 = Plane(Vector(['-0.412', '3.806', '0.728']), '-3.46')
p2 = Plane(Vector(['1.03', '-9.515', '-1.82']), '8.65')
is_par = p1.is_parallel_to(p2)
print('first pair: is parallel = {}, is equal = {}, not parallel = {}'.format(
    is_par, p1 == p2, (not is_par)))

p1 = Plane(Vector(['2.611', '5.528', '0.283']), '4.6')
p2 = Plane(Vector(['7.715', '8.306', '5.342']), '3.76')
is_par = p1.is_parallel_to(p2)
print('second pair: is parallel = {}, is equal = {}, not parallel = {}'.format(
    is_par, p1 == p2, (not is_par)))

p1 = Plane(Vector(['-7.926', '8.625', '-7.212']), '-7.952')
p2 = Plane(Vector(['-2.642', '2.875', '-2.404']), '-2.443')
is_par = p1.is_parallel_to(p2)
print('third pair: is parallel = {}, is equal = {}, not parallel = {}'.format(
    is_par, p1 == p2, (not is_par)))


print("--------------------------")
print("end of PLANE operations")
print("--------------------------")
print("\n")
print("\n")
print("\n")
