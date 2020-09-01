import sklearn.metrics
import numpy as np
import matplotlib.pyplot as plt

def plotROC(fpr,tpr,auc,route):
    plt.title('Curva ROC')
    plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % auc)
    plt.legend(loc = 'lower right')
    plt.plot([0, 1], [0, 1],'r--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.savefig(route)
    plt.close()

modelos = ["Autoencoder-Fully-Connected", "Autoencoder-Fully-Connected-Lotes",
            "Autoencoder-LSTM", "Predictor-LSTM", "Predictor-CNN-LSTM",
            "Feature-Bagging-LOF", "HBOS", "Isolation-Forest", "KNN",
            "LODA", "LOF", "PCA"]

# TP + FN * [1] + FP + TN * [0]
trueLabels = [41*[1]+516*[0],
            41*[1]+516*[0],
            41*[1]+516*[0],
            41*[1]+516*[0],
            41*[1]+514*[0],
            35*[1]+396*[0],
            49*[1]+505*[0],
            37*[1]+521*[0],
            48*[1]+506*[0],
            42*[1]+513*[0],
            46*[1]+509*[0],
            38*[1]+523*[0]]

# TP * [1] + FN *[0] + FP * [1] + TN * [0]
predictions = [33*[1]+8*[0]+441*[1]+75*[0],
            33*[1]+8*[0]+393*[1]+123*[0],
            33*[1]+8*[0]+447*[1]+69*[0],
            33*[1]+8*[0]+393*[1]+123*[0],
            35*[1]+6*[0]+213*[1]+301*[0],
            15*[1]+20*[0]+56*[1]+340*[0],
            44*[1]+5*[0]+505*[1],
            28*[1]+9*[0]+344*[1]+177*[0],
            43*[1]+5*[0]+505*[1]+1*[0],
            36*[1]+6*[0]+341*[1]+172*[0],
            40*[1]+6*[0]+471*[1]+38*[0],
            26*[1]+12*[0]+256*[1]+267*[0]]

for m,tl,pred in zip(modelos, trueLabels, predictions):
    fpr, tpr, thr = sklearn.metrics.roc_curve(tl, pred)
    auc = sklearn.metrics.auc(fpr,tpr)
    plotROC(fpr,tpr,auc,m+"_roc.png")
