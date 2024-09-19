import numpy as np # soorte de vectores
import matplotlib.pyplot as plt #graficador

plt.quiver(1,2,3,4, scale_units= 'xy', angles='xy', scale=1)
plt.xlim(0,4)
plt.ylim(0,8)

#guias
plt.axvline(x=1)
plt.axhline(y=2)

plt.axvline(x=1)
plt.axhline(y=2+4)

plt.quiver([1,0],[2,0],[1,2],[3,2], scale_units='xy', angles='xy', scale=1)
plt.xlim(0,4)
plt.ylim(0,6)

plt.axvline(x=1, color='gray', linestyle='--', alpha=0.3)
plt.axhline(y=2, color='gray', linestyle='--', alpha=0.3)

plt.axvline(x=2, color='gray', linestyle='--', alpha=0.3)
plt.axhline(y=2, color='gray', linestyle='--', alpha=0.3)

plt.axvline(x=2, color='gray', linestyle='--', alpha=0.3)
plt.axhline(y=5, color='gray', linestyle='--', alpha=0.3)

v1 = np.array([1,2])
v2 = np.array([3,4])

plt.quiver([0,0],[0,0],[v1[0],v2[0]],[v1[1],v2[1]], angles='xy', scale_units='xy', scale=1)
plt.xlim(0, max(v1[0], v2[0]))
plt.ylim(0, max(v1[1], v2[1]))

plt.axvline(x=1, alpha=0.2, linestyle='--')
plt.axhline(y=2, alpha=0.2, linestyle='--')
plt.axvline(x=3, alpha=0.2, linestyle='--')
plt.axhline(y=4, alpha=0.2, linestyle='--')

def grafvecs(vecs, cols):
    plt.figure(figsize=(5,5))

    for i in range(len(vecs)):
        vec = vecs[i]
        plt.quiver(0,0, vec[0], vec[1],color=cols[i],
                   angles='xy', scale_units='xy',scale=1)
        
v1 = np.array([1,2])
v2 = np.array([3,4])
v3 = np.array([8,4])

grafvecs([v1,v2,v3], ['blue', 'red','black'])
plt.xlim(0, max(v1[0], v2[0], v3[0]))
plt.ylim(0, max(v1[1], v2[1], v3[1]))