import json
import numpy as np
import matplotlib.pylab as plt

def salva_matrice_come_json(M,i,dir):
    with open(dir + str(i) + '.json', 'w') as f:
        json.dump(M, f)

def salva_matrice_come_immagine(M,i,dir):
    M_np = np.array(M)
    background = np.ones(M_np.shape)

    plt.figure()
    plt.matshow(background, fignum=0, cmap='binary')

    fontsize = max(20 - M_np.shape[0], 5)

    for x in range(M_np.shape[0]):
        for y in range(M_np.shape[1]):
            plt.text(y, x, str(M_np[x, y]), ha='center', va='center', color='black', fontsize=fontsize)

    plt.xlim(-0.5,i-0.5)
    plt.ylim(-0.5,i-0.5)
    plt.gca().xaxis.tick_top()
    plt.gca().invert_yaxis()
    plt.title('Scacchiera ' + str(i) + 'x' + str(i))
    plt.savefig(dir + str(i) + '.png')

    plt.close()