import numpy as np
import pickle
print('compleated')

load_model=pickle.load(open('model.sav','rb'))

data=[6 ,	147 ,	80 ,	0 ,	0 	,29.5 ,	0.178 ,	50	]

array_data=np.asarray(data)
reshape_data=array_data.reshape(1,-1)
print(reshape_data)
predii=load_model.predict(reshape_data)
print(predii)
if predii[0]==1:
  print('has diabetes')
else:
  print('no diabetest')
