
# coding: utf-8

# # Tutorial de solución de ecuaciones diferenciales ordinarias sujetas a una variación sistemática de parámetros
# ### Lourdes Martín Aguilar, César Flores López & Marco Herrera Valdez  
# #### Facultad de Ciencias, Universidad Nacional Autónoma de México
# 
# Resolveremos la ecuación 
# 
# \begin{equation}
# \partial_t x = \frac{a - x}{\tau}, \quad 
# \end{equation}
# 
# para diferentes valores de $\tau$ (velocidad de cambio) y de las condiciones iniciales

# Primero importemos los módulos y funciones que necesitamos

# In[1]:

import scipy as sc
import matplotlib.pylab as gr 
from scipy.integrate import odeint 
get_ipython().magic(u'matplotlib inline')


# El módulo scipy (scipy.org) tiene librerías para cálculos numéricos. El módulo matplotlib (matplotlib.org) tiene liberías para hacer gráficas en 2D, 3D, y más, con calidad de publicación.

# Definamos una función que calcule el cambio en $x$

# In[14]:

def linearEq(u,t,pa): 
    du = (pa["a"]-u)/pa["tau"]
    return du 


# Note que la función _linearEq_ toma como argumentos la variable de estado, el tiempo, y un diccionario de parámetros _p_. Definimos entonces un diccionario que contenga parámetros  

# In[15]:

p=dict() 
p["a"]=90.0; p["tau"]=45.0; p["ic"]=200.0
p["timeMax"]=300; p["timeStep"]=0.1
p["sampTimes"]= sc.arange(0,p["timeMax"],p["timeStep"])

uSol= odeint(func=linearEq, y0=p["ic"], t=p["sampTimes"], args=(p,)).transpose()


# Definimos de qué modo cambiará el valor en los parámetros $\tau$ y condiciones iniciales fijas

# In[16]:

taus= sc.arange(20,120.01,20)
tauSims=list()
for t in taus:
	p["tau"]=t
	uSol= odeint(func=linearEq, y0=p["ic"], t=p["sampTimes"], args=(p,)).transpose()
	tauSims.append(uSol[0])


# Soluciones iteradas para distintas condiciones iniciales y $\tau$ fija

# In[17]:

p["tau"]=45.0; 
ics= sc.arange(70,120.01,10)
icsSims=list()
for t in ics:
	p["ic"]=t
	uSol= odeint(func=linearEq, y0=p["ic"], t=p["sampTimes"], args=(p,)).transpose()
	icsSims.append(uSol[0])


# Graficamos la solución numérica para los diferentes valores de $\tau$ (gráfica izquierda) y de condiciones iniciales (gráfica derecha)

# In[18]:

fig=gr.figure(figsize=(15,5))
rows=1; cols=2; gr.ioff()
ax1=fig.add_subplot(rows,cols,1) 
ax2=fig.add_subplot(rows,cols,2)
nTaus=len(taus)
for n in sc.arange(nTaus): 
	s0=r'$\tau$=%g mins'%(taus[n])
	ax1.plot(p["sampTimes"],tauSims[n],lw=3,alpha=0.9, label=s0) 
nIcs=len(ics)
for n in sc.arange(nIcs): 
	s0=r'$x_0$=%g mg/dl'%(ics[n])	
	ax2.plot(p["sampTimes"], icsSims[n],lw=3, alpha=0.9, label=s0) 

ax2.set_xlabel("mins")
ax1.set_xlabel("mins")
ax2.set_ylabel("mg/dl")
ax1.set_ylabel("mg/dl")
ax1.legend(ncol=2); ax2.legend(ncol=2)
gr.ion();gr.draw()

