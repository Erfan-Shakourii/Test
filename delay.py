"""
@author: Erfan Shakouri
Subject: compare diffrent decoders
""""""
NM = Normal

"""
import numpy as np
import matplotlib.pyplot as plt
##
n=40
# Simple Decoder
Cdecs   = np.zeros((n), dtype=np.float64)
CdecsNM = np.zeros((n), dtype=np.float64)
Ddecs   = np.zeros((n), dtype=np.float64)
#Fast decoder (Row - Colum)
Cdecf   = np.zeros((n), dtype=np.float64)
CdecfNM = np.zeros((n), dtype=np.float64)
Ddecf   = np.zeros((n), dtype=np.float64)
#
x       = np.arange(n, dtype=np.float64)  # for plt
##
Cinv=1
Dinv=1
Cand=2
Dand=2
##
for i in range (2,n) :
   upN=int(i/2)
   dnN=int(i/2)+(i%2)
   
   Cdecs[1]  = Cinv
   Cdecs[i]  = Cdecs[i-1]+(2**i)*Cand+Cinv
   CdecsNM[i]= (Cdecs[i]/(2**i))
   Ddecs[1]  = Dinv
   Ddecs[i]  = Ddecs[i-1]+Dand
   
   Cdecf[1]  = Cinv
   Cdecf[i]  = Cdecf[upN]+Cdecf[dnN]+(2**i)*Cand
   CdecfNM[i]= (Cdecf[i]/(2**i))
   Ddecf[1]  = Dinv
   Ddecf[i]  = Ddecf[upN]+Dand

   i=i+1
##    
plt.plot(x, Ddecs)
plt.plot(x, Ddecf, 'o')

plt.legend(('Ddecs', 'Ddecf'))
plt.xlabel('Number of Input')
plt.ylabel('Delay')
plt.show()
##
plt.plot(x, CdecsNM)
plt.plot(x, CdecfNM, 'o')

plt.legend(('CdecsNM', 'CdecfNM'))
plt.xlabel('Number of Input')
plt.ylabel('Cost/2^n')
plt.show()