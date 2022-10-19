#Diah Ayuning Tyas_A_21091397013
#Membuat Program Multi Neuron Batch Input

# inisialisasi numpy
import numpy as np

#inisialisasi variabel matriks 6x10 (jumlah batch = 6 dan input layer = 10 )
inputs = [[1.2,2.5,3.0,1.0,2.3,1.5,5.0,8.0,3.5,6.0],
          [1.2,4.2,5.5,3.5,8.0,6.5,2.5,1.0,4.5,5.0],
          [2.0,5.0,2.5,1.5,4.0,3.5,5.5,9.0,6.0,7.0],
          [3.3,5.0,2.4,1.2,5.0,3.2,7.5,6.0,3.0,2.5],
          [1.2,2.5,3.5,7.0,2.0,1.5,5.0,5.5,8.0,6.5],
          [3.5,2.5,1.0,2.2,4.0,2.0,8.0,5.0,3.5,7.5]]

#inisialisasi bobot variabel (panjang weight = panjang input dan jumlah weight = jumlah neuron)
weights = [[1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0],
           [1.2,2.2,4.2,3.4,5.0,1.0,2.5,5.2,4.7,8.0],
           [4.0,2.5,2.2,3.5,1.5,6.0,2.3,1.5,8.0,9.0],
           [3.0,5.5,2.5,4.2,1.0,2.6,7.5,9.0,2.0,6.7],
           [1.2,3.0,3.2,4.5,7.0,6.5,3.0,2.5,8.5,6.5]]

#inisialisasi bias (jumlah bias = jumlah neuron)
bias = [1.2,2.0,2.5,3.2,3.0]

#Menghitung output menggunakan rumus : 
output = np.dot(inputs, np.array(weights).T) + bias

#Mencetak Output 
print(output)