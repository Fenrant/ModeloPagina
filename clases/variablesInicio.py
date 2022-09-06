import pickle
from joblib import  load
import pandas as pd

modelos = ['svm','rf']
datasets = ['sintomas', 'recomendaciones']

clasificador = None
vectorizador = None
y_test = None

clf_svm_sintomas = load('sintomas\svm\SVM.joblib')
svm_sintomas_y_test = pd.read_excel('sintomas\svm\SVM-y_test.xlsx')
svm_sintomas_vectorizador = pickle.load(open("sintomas\svm\SVM-vectorizador.pickel", "rb"))

clf_rf_sintomas = load('sintomas\\rf\RandomForest.joblib')
rf_sintomas_y_test = pd.read_excel('sintomas\\rf\RandomForest-y_test.xlsx')
rf_sintomas_vectorizador = pickle.load(open("sintomas\\rf\RandomForest-vectorizador.pickel", "rb"))

#clf_svm_recomendaciones = load('recomendaciones\svm\SVM-Recomendaciones.joblib')
#svm_recomendaciones_y_test = pd.read_excel('recomendaciones\svm\SVM-Recomendaciones-y_test.xlsx')
#svm_recomendaciones_vectorizador = pickle.load(open("recomendaciones\svm\SVM-Recomendaciones.pickle", "rb"))

#clf_rf_recomendaciones = load('recomendaciones\\rf\RandomForest-Recomendaciones.joblib')
#rf_recomendaciones_y_test = pd.read_excel('recomendaciones\\rf\RandomForest-Recomendaciones-y_test.xlsx')
#rf_recomendaciones_vectorizador = pickle.load(open("recomendaciones\\rf\RandomForest-Recomendaciones.pickle", "rb"))

def definirVariablesModelo(modelo,dataset):

    if dataset == 'sintomas':
        global clasificador,vectorizador,y_test
        if modelo == 'rf':
            clasificador = clf_rf_sintomas
            vectorizador = rf_sintomas_vectorizador
            y_test = rf_sintomas_y_test
        elif modelo == 'svm':
            clasificador = clf_svm_sintomas
            vectorizador = svm_sintomas_vectorizador
            y_test = svm_sintomas_y_test
    #elif dataset == 'recomendaciones':
    #    if modelo == 'rf':
    #        clasificador = clf_rf_recomendaciones
    #        vectorizador = rf_recomendaciones_vectorizador
    #        y_test = rf_recomendaciones_y_test
    #    elif modelo == 'svm':
    #        clasificador = clf_svm_recomendaciones
    #        vectorizador = svm_recomendaciones_vectorizador
    #        y_test = svm_recomendaciones_y_test