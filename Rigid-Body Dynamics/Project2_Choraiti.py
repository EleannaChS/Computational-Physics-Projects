#Project 2: Rigid-body dynamics

from scipy.special import ellipj
import matplotlib.pyplot as plt
import math as m
import numpy as np

#Αρχικές συνθήκες και σταθερές
I1 = 0.8
I2 = 0.9
I3 = 1.0
w1_0 = 1.0
w2_0 = 0.0
w3_0 = 2.0

#Task 1

#Συναρτήσεις υπολογισμού των Ε και Μ^2
energy = lambda I1, I2, I3, w1_0, w2_0, w3_0: (I1*pow(w1_0,2) + I2*pow(w2_0,2) + I3*pow(w3_0,2))/2
angular_momentum_squared = lambda I1, I2, I3, w1_0, w2_0, w3_0: pow(I1,2)*pow(w1_0,2) + pow(I2,2)*pow(w2_0,2) + pow(I3,2)*pow(w3_0,2)

#Συναρτήσεις υπολογισμού των τ και κ^2 που είναι τα ορίσματα των ελλειπτικών συναρτήσεων Jacobi
tau_f = lambda I1, I2, I3, E, M2, t: t * m.sqrt((I3-I2)*(M2-2*E*I1)/(I1*I2*I3))
k2_f = lambda I1, I2, I3, E, M2: ((I2-I1)*(2*E*I3-M2))/((I3-I2)*(M2-2*E*I1)) 

#Ορισμός του χρόνου και των βηματων του
t = np.linspace(0,100,1000) 

#Υπολογισμός της αρχικής κινητικής ενέργειας και στροφορμής (διατηρούνται και θα χρησιμοποιηθούν στους υπολογισμούς αναλλίωτα)
E = energy(I1, I2, I3, w1_0, w2_0, w3_0)
M2 = angular_momentum_squared(I1, I2, I3, w1_0, w2_0, w3_0)

#Υπολογισμός των τ και κ^2
tau = tau_f(I1, I2, I3, E, M2, t)
k2 = k2_f(I1, I2, I3, E, M2)

#Υπολογισμός των συναρτήσεων Jacobi
[sn, cn, dn, ph] = ellipj(tau,k2)

#Υπολογισμός των ω1(t), ω2(t) και ω3(t) από την αναλυτική λύση
w1_t = m.sqrt((2*E*I3-M2)/(I1*(I3-I1)))*cn
w2_t = m.sqrt((2*E*I3-M2)/(I2*(I3-I2)))*sn
w3_t = m.sqrt((M2-2*E*I1)/(I3*(I3-I1)))*dn

#Γράφημα των αποτελεσμάτων
fig1 = plt.figure
plt.plot(t,w1_t, label = "w1(t)")
plt.plot(t,w2_t, label = "w2(t)")
plt.plot(t,w3_t, label = "w3(t)")
plt.title("Analytic solution of Euler\'s equation \nusing Jacobi\'s elliptic functions:")
plt.legend(loc='best')
plt.grid()
plt.xlabel('t')
plt.ylabel('w(t)')
plt.savefig('Analytic.png')
plt.show()

#Υπολογισμός της ενέργειας για κάθε βήμα χρόνου
E_t = energy(I1, I2, I3, w1_t, w2_t, w3_t)

#Υπολογισμός του σχετικού σφάλματος (προστίθεται ο όρος 10^(-10) για να μπορεί να υπολογιστεί ο λογάριθμος, τον λογίζουμε ώς το σφάλμα μηχανής)
r_err =np.log10(abs((E_t - E)/E) + pow(10,-16)) 

#Γράφημα του σχετικού σφάλματος
fig2 = plt.figure
plt.plot(t,r_err,"-", label = "relative error")
plt.title("Relative Energy error \nof the analytic solution")
plt.grid()
plt.xlabel('t')
plt.ylabel('log(E(t)-E(0))/E(0)')
plt.savefig('Error_Analytic.png')
plt.show()

print("Το σχετικό σφάλμα φάινεται να παρουσιάζει κάποιες κορυφές περιοδικά")

#Task 2

#3 συναρτήσεις που παριστάνουν τις διαφορικές εξισώσεις του Euler
def f1(w2, w3):
    return (I2-I3)/I1*w2*w3

def f2(w1, w3):
    return (I3-I1)/I2*w3*w1

def f3(w1, w2):
    return (I1-I2)/I3*w1*w2

#Αρχικοποίηση των πινάκων των αποτελεσμάτων
w1 = [w1_0]
w2 = [w2_0]
w3 = [w3_0]

#Συνάρτηση εφαρμογής της μεθόδου Runge Kutta 4ης τάξης για επίλυση συστήματος τριών διαφορικών εξισώσεων
def RK4_3(t0, w1_0, w2_0, w3_0, tmax, dt):
   
    n = (int)((tmax - t0)/dt)
   
    w1_rk = w1_0
    w2_rk = w2_0
    w3_rk = w3_0
    for i in range(1, n):
        
        k1 = dt * f1(w2_rk, w3_rk)
        l1 = dt * f2(w1_rk, w3_rk) 
        n1 = dt * f3(w1_rk, w2_rk) 
        
        k2 = dt * f1(w2_rk + 0.5*l1, w3_rk + 0.5*n1)
        l2 = dt * f2(w1_rk + 0.5*k1, w3_rk + 0.5*n1) 
        n2 = dt * f3(w1_rk + 0.5*k1, w2_rk + 0.5*l1) 
        
        k3 = dt * f1(w2_rk + 0.5*l2, w3_rk + 0.5*n2)
        l3 = dt * f2(w1_rk + 0.5*k2, w3_rk + 0.5*n2)
        n3 = dt * f3(w1_rk + 0.5*k2, w2_rk + 0.5*l2)
                     
        k4 = dt * f1(w2_rk + l3, w3_rk + n3)
        l4 = dt * f2(w1_rk + k3, w3_rk + n3)
        n4 = dt * f3(w1_rk + k3, w2_rk + l3)
    
        w1_rk = w1_rk + (1.0 / 6.0)*(k1 + 2*k2 + 2*k3 + k4)
        w2_rk = w2_rk + (1.0 / 6.0)*(l1 + 2*l2 + 2*l3 + l4)
        w3_rk = w3_rk + (1.0 / 6.0)*(n1 + 2*n2 + 2*n3 + n4)

        w1.append(w1_rk)
        w2.append(w2_rk)
        w3.append(w3_rk)
       
    return w1,w2,w3

#Εφαρμογή της μεθόδου Runge Kutta     
RK4_3(0, 1.0, 0.0, 2.0, 100, 0.1)

#Γράφημα των αποτελεσμάτων
fig3 = plt.figure
plt.plot(t,w1, label = "w1(t)")
plt.plot(t,w2, label = "w2(t)")
plt.plot(t,w3, label = "w3(t)")
plt.title("Numerical solution of Euler\'s equation \nusing RK4 method:")
plt.legend(loc='best')
plt.grid()
plt.xlabel('t')
plt.ylabel('w(t)')
plt.savefig('RK4.png')
plt.show()

#Υπολογισμός της ενέργειας για κάθε βήμα χρόνου
E_t_RK = energy(I1, I2, I3, np.array(w1), np.array(w2), np.array(w3))

#Υπολογισμός του σχετικού σφάλματος (προσθέτουμς το σφάλμα μηχανής ώστε να μπορούμε να συγκρίνουμε τα σφάλματα)
r_err_RK =np.log10(abs((E_t_RK - E)/E) + pow(10,-16))

#Γράφημα του σχετικού σφάλματος
fig4 = plt.figure
plt.plot(t,r_err_RK,"-", label = "relative error")
plt.title("Relative Energy error \nof the RK4 solution")
plt.grid()
plt.xlabel('t')
plt.ylabel('log(E(t)-E(0))/E(0)')
plt.savefig('Error_RK4.png')
plt.show()

print("Το σφάλμα παρουσιάζει κι εδώ κορυφές  ενώ όσο ο χρόνος μεγαλώνει οι κορυφές εξομαλύνονται")
#Task 3

#3 συναρτήσεις που παριστάνουν τις μήτρες περιστροφής R
def Rx(theta):
    return np.array([[1, 0, 0],
                   [0, np.cos(theta), np.sin(theta)],
                   [0, -np.sin(theta), np.cos(theta)]])
    
def Ry(theta):
    return np.array([[np.cos(theta), 0, -np.sin(theta)],
                   [0, 1, 0],
                   [np.sin(theta), 0, np.cos(theta)]])
    
def Rz(theta):
    return np.array([[np.cos(theta), np.sin(theta), 0],
                   [-np.sin(theta), np.cos(theta), 0],
                   [0, 0, 1]])

#3 Συναρτήσεις των ακριβών λύσεων της μεθόδου splitting
def H_M1(t_sp, M):
    M_next = np.dot(Rx(M[0]*t_sp/I1),M)
    return M_next

def H_M2(t_sp, M):
    M_next = np.dot(Ry(M[1]*t_sp/I2),M)
    return M_next

def H_M3(t_sp, M):
    M_next = np.dot(Rz(M[2]*t_sp/I3),M)
    return M_next

#Αρχικοποίηση των πινάκων των αποτελεσμάτων
w1_sp =[w1_0]
w2_sp = [w2_0]
w3_sp = [w3_0]
#Αρχικοποίηση του πίνακα του χρόνου
t_sp = [0]

#Αρχικοπίηση του διανύσματος της στροφορμής
M_n = np.array([I1*w1_0, I2*w2_0, I3*w3_0])

#ορισμός του βήματος
dt = 0.02

#Επανάληψη για όλα τα βήματα χρόνου
for t_s in np.arange(0,100.02,dt):
    
    #Εφαρμογή της μεθόδου splitting
    M_n = H_M1(dt/2, M_n)
    M_n = H_M2(dt/2, M_n)
    M_n = H_M3(dt, M_n)
    M_n = H_M2(dt/2, M_n)
    M_n = H_M1(dt/2, M_n)        
    
    #ΚΑταχώρηση των αποτελεσμάτων σε πίνακες
    w1_sp.append(M_n[0]/I1)
    w2_sp.append(M_n[1]/I2)
    w3_sp.append(M_n[2]/I3)
    t_sp.append(t_s)

#Γράφημα των αποτελεσμάτων
fig5 = plt.figure
plt.plot(t_sp,w1_sp, label = "w1(t)")
plt.plot(t_sp,w2_sp, label = "w2(t)")
plt.plot(t_sp,w3_sp, label = "w3(t)")
plt.title("Numerical solution of Euler\'s equation \nusing the splitting method:")
plt.legend(loc='best')
plt.grid()
plt.xlabel('t')
plt.ylabel('w(t)')
plt.savefig('Splitting.png')
plt.show()

#Υπολογισμός και γράφημα του σχετικού σφάλματος (προσθέτουμς το σφάλμα μηχανής για να μπορούμε να συγκρίνουμε τα σφάλματα)
E_t_sp = energy(I1, I2, I3, np.array(w1_sp), np.array(w2_sp), np.array(w3_sp))

r_err_sp =np.log10(abs((E_t_sp - E)/E) + pow(10,-16))

fig6 = plt.figure
plt.plot(t_sp,r_err_sp,"-", label = "relative error")
plt.title("Relative Energy error \nof the splitting solution")
plt.grid()
plt.xlabel('t')
plt.ylabel('log(E(t)-E(0))/E(0)')
plt.savefig('Error_splitting.png')
plt.show()

print("Κι εδώ το σφάλμα παρουσιάζει κορυφές, \n παρακάτω θα τοποθετήσουμε στο ίδιο διάγραμμα όλα τα σφάλματα ώστε να τα συγκρίνουμε")

#γράφημα όλων των σφαλμάτων στο ίδιο γράφημα 
fig7 = plt.figure
plt.plot(t,r_err,"-", label = "analytic solution")
plt.plot(t,r_err_RK,"-", label = "RK4 solution")
plt.plot(t_sp,r_err_sp,"-", label = "splitting solution")
plt.title("Relative Energy error")
plt.legend(loc='best')
plt.grid()
plt.xlabel('t')
plt.ylabel('log(E(t)-E(0))/E(0)')
plt.savefig('errors.png')
plt.show()   

print("Η αναλυτική λύση είναι και αυτή με το μικρότερο σφάλμα, πράγμα λογικό, εφόσον το σφάλμα της είνα της τάξης μεγέθους του σφάλματος μηχανής")
print("H μέθοδος RK4 έχει το αμέσως μεγαλυτερο σφάλμα ενώ η splitting μέθοδος έχει το μεγαλύτερο σφάλμα και αυτο με τις μεγαλύτερες διακυμάνσεις") 
print("Και τα 3 σφάλματα παρουσιάζουν κορυφές και πτώσεις στα ίδια χρονικά σημεια")
print("Aπό τα διαγράματα των ω φαίνεται πως η περίοδος του σφάλματος ισούται με το 1/2 της περιόδου των ω1 και ω2 ενώ είναι ΄ίση με την περίοδο του ω3")           

#Γράφημα των ω για όλες τις μεθλοδους στο ίδιο γράφημα     
fig8 = plt.figure
plt.plot(t,w1_t,"-", label = "analytic solution")
plt.plot(t,w1,"-", label = "RK4 solution")
plt.plot(t_sp,w1_sp,"-", label = "splitting solution")
plt.title("w1(t)")
plt.legend(loc='best')
plt.grid()
plt.xlabel('t')
plt.ylabel('w1(t)')
plt.savefig('w1.png')
plt.show()           

fig9 = plt.figure
plt.plot(t,w2_t,"-", label = "analytic solution")
plt.plot(t,w2,"-", label = "RK4 solution")
plt.plot(t_sp,w2_sp,"-", label = "splitting solution")
plt.title("w2(t)")
plt.legend(loc='best')
plt.grid()
plt.xlabel('t')
plt.ylabel('w2(t)')
plt.savefig('w2.png')
plt.show() 

fig810 = plt.figure
plt.plot(t,w3_t,"-", label = "analytic solution")
plt.plot(t,w3,"-", label = "RK4 solution")
plt.plot(t_sp,w3_sp,"-", label = "splitting solution")
plt.title("w3(t)")
plt.legend(loc='best')
plt.grid()
plt.xlabel('t')
plt.ylabel('w3(t)')
plt.savefig('w3.png')
plt.show()         
    
print("Από τα γραφήματα των τιμών που προκύπτουν για τα ω1, ω2, ω3 από τις διάφορες μεθόδους, όταν τοποθετηθούν στο ίδιο σχήμα,")
print("βλέπουμε πως και οι 3 λύσεις του συστήματος είναι ικανοποιητικές. Οπότε χρησιμοποιούμε το σφάλμα για να κάνουμε σωστή σύγκριση.")     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        