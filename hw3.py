import numpy as np
import matplotlib.pyplot as plt

print("#1")
def f(n):
   return sum([(-1)**(k-1)/(2*k-1) for k in range(1,n+1)])

plt.plot([n for n in range(101)],[(-1)**(n-1)/(2*n-1) for n in range(1,n+1)],color='black')
plt.xlabel('n')
plt.ylabel('f')
plt.legend()

print("-----------------------------------------------------------------")

print("#2")

def f(n):
   if f==0:
      return 0.5
   else:
      return r*f(n-1)*(1-f(n-1))

   if r==0.5 and f[0]==0.5:
      L=[r*f(n-1)*(1-f(n-1)) for n in range(101)]
      plt.plot(L)
      plt.plot([n for n in range(101)],[r*f(n-1)*(1-f(n-1)) for n in range(101)],'s-',color='black')
      plt.xlabel('n')
      plt.ylabel('f')
      plt.legend()

   if r==0.95 and f[0]==0.5:
      L=[r*f(n-1)*(1-f(n-1)) for n in range(101)]
      plt.plot(L)
      plt.plot([n for n in range(101)],[r*f(n-1)*(1-f(n-1)) for n in range(101)],'s-',color='black')
      plt.xlabel('n')
      plt.ylabel('f')
      plt.legend()

   if r==2 and f[0]==0.5:
      L=[r*f(n-1)*(1-f(n-1)) for n in range(101)]
      plt.plot(L)
      plt.plot([n for n in range(101)],[r*f(n-1)*(1-f(n-1)) for n in range(101)],'s-',color='black')
      plt.xlabel('n')
      plt.ylabel('f')
      plt.legend()

   if r==3.2 and f[0]==0.5:
      L=[r*f(n-1)*(1-f(n-1)) for n in range(101)]
      plt.plot(L)
      plt.plot([n for n in range(101)],[r*f(n-1)*(1-f(n-1)) for n in range(101)],'s-',color='black')
      plt.xlabel('n')
      plt.ylabel('f')
      plt.legend()

   if r==3.8 and f[0]==0.5:
      L=[r*f(n-1)*(1-f(n-1)) for n in range(101)]
      plt.plot(L)
      plt.plot([n for n in range(101)],[r*f(n-1)*(1-f(n-1)) for n in range(101)],'s-',color='black')
      plt.xlabel('n')
      plt.ylabel('f')
      plt.legend()

   if r==3.8 and f[0]==0.501:
      L=[r*f(n-1)*(1-f(n-1)) for n in range(101)]
      plt.plot(L)
      plt.plot([n for n in range(101)],[r*f(n-1)*(1-f(n-1)) for n in range(101)],'s-',color='black')
      plt.xlabel('n')
      plt.ylabel('f')
      plt.legend()

print("-----------------------------------------------------------------")

print("#3")
def sinc(x):
   return math.sin(x)/x

   def Fac(n):
      if n==0:
         return 1
      else:
         return n*Fac(n-1)
   return sum([(-1)**(n)*x**(2*n)/Fac(2*n+1) for k in range(0,x+1)])












      
