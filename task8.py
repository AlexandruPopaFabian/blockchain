# Parametrii curbei
p = 9739
a = 497
b = 1768

class Point:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def is_identity(self):
        return self.x is None and self.y is None

    def __add__(self, other):
        # (a) Dacă P = O
        if self.is_identity():
            return other
        # (b) Dacă Q = O
        if other.is_identity():
            return self

        # (c) P = (x1, y1), Q = (x2, y2)
        x1, y1 = self.x, self.y
        x2, y2 = other.x, other.y

        # (d) Dacă x1 = x2 și y1 = -y2 mod p
        if x1 == x2 and (y1 + y2) % p == 0:
            return Point(None, None) # P + Q = O

        # (e) Calcularea pantei lambda
        if x1 != x2 or y1 != y2:
            # (e1) P != Q
            num = (y2 - y1) % p
            den = pow((x2 - x1) % p, -1, p)
            lmbda = (num * den) % p
        else:
            # (e2) P == Q
            num = (3 * x1**2 + a) % p
            den = pow((2 * y1) % p, -1, p)
            lmbda = (num * den) % p

        # (f) x3 = lambda^2 - x1 - x2 mod p
        x3 = (lmbda**2 - x1 - x2) % p

        # (h) y3 = lambda*(x1 - x3) - y1 mod p
        y3 = (lmbda * (x1 - x3) - y1) % p

        # (i) P + Q = (x3, y3)
        return Point(x3, y3)

    def is_on_curve(self):
        """Verifica dacă punctul apartine curbei E(Fp): y^2 = x^3 + ax + b mod p"""
        if self.is_identity():
            return True
        left = (self.y**2) % p
        right = (self.x**3 + a * self.x + b) % p
        return left == right

    def __repr__(self):
        return f"O" if self.is_identity() else f"({self.x}, {self.y})"


X = Point(5274, 2841)
Y = Point(8669, 740)

# --- Calculul cerut: S = P + P + Q + R ---
P = Point(493, 5564)
Q = Point(1539, 4742)
R = Point(4403, 5202)

S = P + P + Q + R

print(f"Punctul S(x, y) este: {S}")

assert S.is_on_curve(), "Punctul S NU se afla pe curba!"
print("[+] Assert confirmat: Punctul S(x, y) apartine grupului E(F_p).")

