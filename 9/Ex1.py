# Ex1:

Dv = 5*np.exp(-3)
Du = 5*np.exp(-3)

def laplacian(Z):
    Ztop = Z[0:-2, 1:-1]
    Zleft = Z[1:-1, 0:-2]
    Zbottom = Z[2:, 1:-1]
    Zright = Z[1:-1, 2:]
    Zcenter = Z[1:-1, 1:-1]
    return (Ztop + Zleft + Zbottom + Zright -4 * Zcenter) / dx**2

U = np.random.rand(100, 100)
V = np.random.rand(100, 100)
DeltaU= laplacian(U)
deltaV= laplacian(V)
Uc= U[1:-1, 1:-1]
Vc= V[1:-1, 1:-1]
U[1:-1, 1:-1] = Uc+ dt* (Du * DeltaU+ Uc-Uc**3 -Vc+ T),
V[1:-1, 1:-1] = Vc+ dt* (Dv* deltaV+ Uc-Vc) * a