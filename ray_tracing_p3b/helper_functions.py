import math

class PVector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "PVector(%f, %f, %f)" % (self.x, self.y, self.z)

    def __add__(self, other):
        return PVector.add(self, other)

    def __mul__(self, n):
        return PVector.mult(self, n)

    def __rmul__(self, n):
        return PVector.mult(self, n)

    def mag(self):
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def magSq(self):
        return self.x * self.x + self.y * self.y + self.z * self.z

    def copy(self):
        return PVector(self.x, self.y, self.z)

    def div(self, n):
        return PVector(
            a.x / n,
            a.y / n,
            a.z / n,
        )

    @staticmethod
    def dist(a, b):
        return PVector.sub(a, b).mag()

    @staticmethod
    def add(a, b):
        return PVector(
            a.x + b.x,
            a.y + b.y,
            a.z + b.z,
        )

    @staticmethod
    def sub(a, b):
        return PVector(
            a.x - b.x,
            a.y - b.y,
            a.z - b.z,
        )
    
    def __sub__(self, other):
        return PVector.sub(self, other)


    @staticmethod
    def mult(a, n):
        return PVector(
            n * a.x,
            n * a.y,
            n * a.z,
        )

    @staticmethod
    def pairwise_mult(a, b):
        return PVector(
            a.x * b.x,
            a.y * b.y,
            a.z * b.z,
        )

    @staticmethod
    def dot(a, b):
        return a.x * b.x + a.y * b.y + a.z * b.z

    @staticmethod
    def cross(a, b):
        return PVector(
            a.y * b.z - a.z * b.y,
            a.z * b.x - a.x * b.z,
            a.x * b.y - a.y * b.x,
        )

    def normalize(self):
        mag = sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        self.x /= mag
        self.y /= mag
        self.z /= mag
        return self

class Light:
    def __init__(self, v, r, g, b):
        self.v = v
        self.r = r
        self.g = g
        self.b = b

class Ray():
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def getXYZ(self, t):
        x = self.origin.x + (t * self.direction.x)
        y = self.origin.y + (t * self.direction.y)
        z = self.origin.z + (t * self.direction.z)
        return PVector(x, y, z)

class Triangle():
    def __init__(self, v1, v2, v3, dr, dg, db, ar, ag, ab, sr, sg, sb, spec_power, k_refl):
        self.a = v1
        self.b = v2
        self.c = v3
        
        self.dr = dr
        self.dg = dg
        self.db = db
        
        self.ar = ar
        self.ag = ag
        self.ab = ab
        
        self.sr = sr
        self.sg = sg
        self.sb = sb
        
        self.spec_power = spec_power
        self.k_refl = k_refl
        
        self.triNorm = PVector.cross((self.b - self.a), (self.c - self.a)).normalize()
        
        self.t = 0
        
    def getIntersect(self, ray): 
        denom = PVector.dot(self.triNorm, ray.direction)
        if denom == 0:
            return None
        else:
            t = PVector.dot(self.triNorm, (self.a - ray.origin)) / denom
            self.t = t
        if (t < 0):
            return None
        else: 
            p = ray.getXYZ(t)
        triple1 = PVector.dot((PVector.cross((self.b - self.a),(p - self.a))), self.triNorm)
        triple2 = PVector.dot((PVector.cross((self.c - self.b),(p - self.b))), self.triNorm)
        triple3 = PVector.dot((PVector.cross((self.a - self.c),(p - self.c))), self.triNorm)
        
        if (triple1 >= 0 and triple2 >= 0 and triple3 >= 0):
            return p
        else:
            return None 
        
        
class Sphere:
    def __init__(self, radius, x, y, z, dr, dg, db, ar, ag, ab, sr, sg, sb, spec_power, k_refl):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z
        self.center = PVector(x, y, z)
        
        self.dr = dr
        self.dg = dg
        self.db = db
        
        self.ar = ar
        self.ag = ag
        self.ab = ab
        
        self.sr = sr
        self.sg = sg
        self.sb = sb
        
        self.spec_power = spec_power
        self.k_refl = k_refl
        self.t = 0
    def getIntersect(self, ray):
        toSphere = ray.origin - self.center
        point1 = PVector.dot(ray.direction, ray.direction)
        point2 = 2 * (PVector.dot(toSphere, ray.direction))
        point3 = PVector.dot(toSphere, toSphere) - (self.radius **2)

        discriminant = (point2*point2) - (4*point1*point3)
        #print(discriminant)
        if discriminant < 0:
            return None
        else: 
            hits = (-point2 - sqrt(discriminant)) / (2*point1)
            self.t = hits
            return ray.getXYZ(hits)
