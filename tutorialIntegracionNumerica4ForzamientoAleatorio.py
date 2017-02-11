import scipy as sc
from scipy.integrate import odeint
import matplotlib.pylab as gr

p={"a":1.0, "tau":1.0,"x0":0.5}
p["timeMax"]=10.0; p["timeStep"]=1e-3
p["sampTimes"]= sc.arange(0,p["timeMax"],p["timeStep"]); 

# Modeling Ornstein-Uhlenbeck and related processes using Langevin-like equations
def linearForcedEq(x,t,p):
	dx = (p["a"] - x)/p["tau"] + p["f"](t)
	return dx 

p["f"] = lambda t: 0.0
o0= odeint(func=linearForcedEq, y0=p["x0"],t=p["sampTimes"], args=(p,)).transpose()
# Random process to force the system
uUnif= -0.5 + sc.rand(len(sampTimes))
p["f"] = lambda t: sc.interp(t, xp=sampTimes, fp=uUnif)
oUnif= odeint(func=linearForcedEq, y0=p["x0"],t=p["sampTimes"], args=(p,)).transpose()
uNorm= 0.3*sc.randn(len(sampTimes))
p["f"] = lambda t: sc.interp(t, xp=sampTimes, fp=uNorm)
oNorm= odeint(func=linearForcedEq, y0=p["x0"],t=p["sampTimes"], args=(p,)).transpose()
#
gr.figure(figsize=(11,5))
gr.plot(p["sampTimes"],o0[0],'k', alpha=0.35, lw=2.0, label=r"$(t,x(t))$")
gr.plot(p["sampTimes"],oUnif[0],'k', alpha=1.0, lw=1.0, label=r"$(t,x_{unif}(t))$")
gr.plot(p["sampTimes"],oNorm[0],'b', lw=1.0, label=r"$(t,x_{norm}(t))$")
gr.legend(loc="lower right")
gr.ion(); gr.draw()
