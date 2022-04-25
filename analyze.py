import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import curve_fit

def b(x, a, m, c, d):
    return a * np.log(m * x + c) + d


def footprintGraphs():
    plt.subplot(1, 2, 1)
    ax = sns.heatmap(feetA)
    plt.xlabel("Link")
    plt.ylabel("Contact with the Ground (A)")

    plt.subplot(1, 2, 2)
    bx = sns.heatmap(feetB)
    plt.xlabel("Link")
    plt.ylabel("Contact with the Ground (B)")

    plt.show()


def genotypeFitness():
    plt.scatter(fitA[0], fitA[1], marker = 'x', label = "Population A", color = 'b', s = 1, alpha = 0.25)
    p = curve_fit(b, fitA[0], fitA[1])
    plt.plot(np.arange(np.amax(fitA[0])), b(np.arange(np.amax(fitA[0])), *p[0]), color = 'b')

    plt.scatter(fitB[0], fitB[1], marker = 'o', label = "Population B", color = 'r', s = 1, alpha = 0.25)
    p = curve_fit(b, fitB[0], fitB[1])
    plt.plot(np.arange(np.amax(fitB[0])), b(np.arange(np.amax(fitB[0])), *p[0]), color = 'r')

    plt.xlabel("Genotypic Age (Generations)")
    plt.ylabel("Fitness Score")
    plt.legend()

    plt.show()


def simulationFitness():
    plt.scatter(gFitA[0], gFitA[1], marker = 'x', label = "Population A", color = 'b', s = 1, alpha = 0.25)
    p = curve_fit(b, gFitA[0], gFitA[1])
    plt.plot(np.arange(np.amax(gFitA[0])), b(np.arange(np.amax(gFitA[0])), *p[0]), color = 'b')

    plt.scatter(gFitB[0], gFitB[1], marker = 'o', label = "Population B", color = 'r', s = 1, alpha = 0.25)
    p = curve_fit(b, gFitB[0], gFitB[1])
    plt.plot(np.arange(np.amax(gFitB[0])), b(np.arange(np.amax(gFitB[0])), *p[0]), color = 'r')

    plt.xlabel("SImulation Age (Generations)")
    plt.ylabel("Fitness Score")
    plt.legend()

    plt.show()


fitA = np.load('fitA.npy')
feetA = np.load('feetA.npy')
gFitA = np.load('gFitA.npy')

fitB = np.load('fitB.npy')
feetB = np.load('feetB.npy')
gFitB = np.load('gFitB.npy')

fitA = fitA[:, fitA[0].argsort()]
fitB = fitB[:, fitB[0].argsort()]

footprintGraphs()
genotypeFitness()
simulationFitness()
