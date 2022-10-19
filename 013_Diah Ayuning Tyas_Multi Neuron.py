#Diah Ayuning Tyas_A_21091397013
#Membuat Program Multi Neuron

#inisialisasi numpy
import numpy as np

#inisialisasi variabel dengan input sesuai panjang input layer = 10
inputs = [2.0,1.5,2.2,3.4,1.0,3.0,4.5,5.0,2.4,7.0]

#inisialisasi bobot variabel dengan weight sesuai jumlah neuron = 5 
weights = [[5.5,0.8,-1.2,3.5,4,8,-1.5,-2.2,0.4,5.5],
           [3,6,0.7,-2.4,1.0,5,2.5,0.4,-0.6,9.0],
           [2,1.5,2.0,-0.5,0.2,-2.2,1.0,7,5.5,0.5],
           [1.2,4,8,1,3,0.2,8.0,7.5,-0.3,4.5],
           [3.3,1.5,-4.2,3.0,5,7,0.1,2.4,1.5,6.5]]

#jumlah bias seperti jumlah neuron 
bias = [1.2,0.4,5,2.5,0.2] 

#menghitung output = (input*weight)+bias
output = np.dot(weights, inputs) + bias

#mencetak output 
print(output)