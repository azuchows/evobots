import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import curve_fit

def b(x, a, c):
    return a * x + c


def footprintGraphs():

    plt.figure()
    plt.subplot(3, 2, 1)
    ax = sns.heatmap(feetA)
    plt.xlabel("Link")
    plt.ylabel("Contact with the Ground (A)")

    plt.subplot(3, 2, 2)
    bx = sns.heatmap(feetB)
    plt.xlabel("Link")
    plt.ylabel("Contact with the Ground (B)")

    plt.subplot(3, 2, 3)
    cx = sns.heatmap(feetC)
    plt.xlabel("Link")
    plt.ylabel("Contact with the Ground (C)")

    plt.subplot(3, 2, 4)
    dx = sns.heatmap(feetD)
    plt.xlabel("Link")
    plt.ylabel("Contact with the Ground (D)")

    plt.subplot(3, 2, 5)
    ex = sns.heatmap(feetE)
    plt.xlabel("Link")
    plt.ylabel("Contact with the Ground (E)")


def genotypeFitness():
    plt.figure()
    p = curve_fit(b, fitA[0], fitA[1])
    plt.plot(np.arange(np.amax(fitA[0])), b(np.arange(np.amax(fitA[0])), *p[0]), color = '#b41820', label = "Population A")

    s = curve_fit(b, fitB[0], fitB[1])
    plt.plot(np.arange(np.amax(fitB[0])), b(np.arange(np.amax(fitB[0])), *s[0]), color = '#46acc8', label = "Population B")

    q = curve_fit(b, fitC[0], fitC[1])
    plt.plot(np.arange(np.amax(fitC[0])), b(np.arange(np.amax(fitC[0])), *q[0]), color = '#e58601', label = "Population C")

    r = curve_fit(b, fitD[0], fitD[1])
    plt.plot(np.arange(np.amax(fitD[0])), b(np.arange(np.amax(fitD[0])), *r[0]), color = '#BED558', label = "Population D - AFPO")

    t = curve_fit(b, fitE[0], fitE[1])
    plt.plot(np.arange(np.amax(fitE[0])), b(np.arange(np.amax(fitE[0])), *t[0]), color = '#52489c', label = "Population E - PHC")

    plt.scatter(fitA[0], fitA[1], marker = 'x', color = '#b41820', s = 1, alpha = 0.05)
    plt.scatter(fitB[0], fitB[1], marker = 'o', color = '#46acc8', s = 1, alpha = 0.05)
    plt.scatter(fitC[0], fitC[1], marker = 's', color = '#e58601', s = 1, alpha = 0.05)
    plt.scatter(fitD[0], fitD[1], marker = 'd', color = '#BED558', s = 1, alpha = 0.05)
    plt.scatter(fitE[0], fitE[1], marker = 'p', color = '#52489c', s = 1, alpha = 0.05)

    plt.xlabel("Genotypic Age (Generations)")
    plt.ylabel("Fitness Score")
    plt.legend()


def simulationFitness():
    plt.figure()
    plt.scatter(gFitA[0], gFitA[1], marker = 'x', color = '#b41820', s = 1, alpha = 0.1)
    p = curve_fit(b, gFitA[0], gFitA[1])
    plt.plot(np.arange(np.amax(gFitA[0])), b(np.arange(np.amax(gFitA[0])), *p[0]), color = '#b41820', label = "Population A")

    plt.scatter(gFitB[0], gFitB[1], marker = 'o', color = '#46acc8', s = 1, alpha = 0.1)
    p = curve_fit(b, gFitB[0], gFitB[1])
    plt.plot(np.arange(np.amax(gFitB[0])), b(np.arange(np.amax(gFitB[0])), *p[0]), color = '#46acc8', label = "Population B")

    plt.scatter(gFitC[0], gFitC[1], marker = 's', color = '#e58601', s = 1, alpha = 0.1)
    p = curve_fit(b, gFitC[0], gFitC[1])
    plt.plot(np.arange(np.amax(gFitC[0])), b(np.arange(np.amax(gFitC[0])), *p[0]), color = '#e58601', label = "Population C")

    plt.scatter(gFitD[0], gFitD[1], marker = 'd', color = '#BED558', s = 1, alpha = 0.1)
    p = curve_fit(b, gFitD[0], gFitD[1])
    plt.plot(np.arange(np.amax(gFitD[0])), b(np.arange(np.amax(gFitD[0])), *p[0]), color = '#BED558', label = "Population D - AFPO")

    plt.scatter(fitE[0], fitE[1], marker = 'p', color = '#52489c', s = 1, alpha = 0.1)
    t = curve_fit(b, fitE[0], fitE[1])
    plt.plot(np.arange(np.amax(fitE[0])), b(np.arange(np.amax(fitE[0])), *t[0]), color = '#52489c', label = "Population D - PHC")

    plt.xlabel("SImulation Age (Generations)")
    plt.ylabel("Fitness Score")
    plt.legend()

def generationalFitness():
    plt.figure()
    plt.scatter(agfit[0], agfit[1], marker = 'x', color = '#b41820', s = 1, alpha = 0.1)
    p = curve_fit(b, agfit[0], agfit[1])
    plt.plot(np.arange(np.amax(agfit[0])), b(np.arange(np.amax(agfit[0])), *p[0]), color = '#b41820', label = "Population A")

    plt.scatter(bgfit[0], bgfit[1], marker = 'o', color = '#46acc8', s = 1, alpha = 0.1)
    p = curve_fit(b, bgfit[0], bgfit[1])
    plt.plot(np.arange(np.amax(bgfit[0])), b(np.arange(np.amax(bgfit[0])), *p[0]), label = "Population B", color = '#46acc8')

    plt.scatter(cgfit[0], cgfit[1], marker = 's', color = '#e58601', s = 1, alpha = 0.1)
    p = curve_fit(b, cgfit[0], cgfit[1])
    plt.plot(np.arange(np.amax(cgfit[0])), b(np.arange(np.amax(cgfit[0])), *p[0]), color = '#e58601', label = "Population C")

    plt.scatter(dgfit[0], dgfit[1], marker = 'd', color = '#BED558', s = 1, alpha = 0.1)
    p = curve_fit(b, dgfit[0], dgfit[1])
    plt.plot(np.arange(np.amax(dgfit[0])), b(np.arange(np.amax(dgfit[0])), *p[0]), color = '#BED558', label = "Population D - AFPO")

    plt.scatter(fitE[0], fitE[1], marker = 'p', color = '#52489c', s = 1, alpha = 0.1)
    t = curve_fit(b, fitE[0], fitE[1])
    plt.plot(np.arange(np.amax(fitE[0])), b(np.arange(np.amax(fitE[0])), *t[0]), color = '#52489c', label = "Population D - PHC")

    plt.xlabel("SImulation Age (Generations)")
    plt.ylabel("Fitness Score")
    plt.legend()


fitA = np.load('fitA.npy')
feetA = np.load('feetA.npy')
gFitA = np.load('gFitA.npy')
afit = np.load('Afit.npy')
agfit = np.load('Agfit.npy')

fitB = np.load('fitB.npy')
feetB = np.load('feetB.npy')
gFitB = np.load('gFitB.npy')
bfit = np.load('Bfit.npy')
bgfit = np.load('Bgfit.npy')

fitC = np.load('fitC.npy')
feetC = np.load('feetC.npy')
gFitC = np.load('gFitC.npy')
cfit = np.load('Cfit.npy')
cgfit = np.load('Cgfit.npy')

fitD = np.load('fitD.npy')
feetD = np.load('feetD.npy')
gFitD = np.load('gFitD.npy')
dfit = np.load('Dfit.npy')
dgfit = np.load('Dgfit.npy')

fitE = np.load('fitE.npy')
feetE = np.load('feetE.npy')

fitA = fitA[:, fitA[0].argsort()]
fitB = fitB[:, fitB[0].argsort()]
fitC = fitC[:, fitC[0].argsort()]
fitD = fitD[:, fitD[0].argsort()]
fitE = fitE[:, fitE[0].argsort()]

#footprintGraphs()
#genotypeFitness()
#simulationFitness()
#generationalFitness()


plt.scatter(fitA[0], fitA[1], marker = 'x', color = '#b41820', s = 1)

plt.show()
