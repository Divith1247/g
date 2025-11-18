import pandas as pd
from functools import reduce
data={
    'num':[1,2,3,4,5],
    'let':['a','b','c','d','e']
}
df=pd.DataFrame(data)
sq=df('num'),map(lambda x : x**2)
print(sq)
ev=list(filter(lambda x: x%2==0,df('num')))
print(ev)
po=reduce(lambda x,y: x*y,df('num'))
print(po)