#Diah Ayuning Tyas_A_21091397013
#Membuat Program Single Neuron

#Inisialisasi Numpy
import numpy as np

#Inisialisasi variabel dengan panjang input layer = 10
inputs = [4,6,5.5,3,4.5,2,7,9,8,1]

#Inisialisasi bobot variabel sesuai dengan jumlah neuron = 1
weights = [0.5,1.6,-2.7,0.8,-4.3,-0.9,2.5,1.9,-2.4,1.7]

#Inisialisasi bias berdasarkan panjang neuron
bias = 8

# Menghitung output = (input*weight)+bias
output = np.dot(weights, inputs) + bias

# cetak output
print(output)