import matplotlib.pyplot as plt
import numpy as np



T = 1
pause = 0.25
armonics = 15
f0 = 1/T
amp = 2
tau = T-pause


def squareWave(x):
    x+= 0.75/2.
    if((x%1)>0.75):
        return -1
    else:
        return 1




def Xn(n):
    Xn = ((amp*tau)/T)*np.sin(n*f0*np.pi*tau)/(n*f0*np.pi*tau)
    return Xn



def fourier(n_max,t):
    a0 = 0.5
    sum = a0
    for n in range(1,n_max):
        try:
            sum = sum + 2*Xn(n)*np.cos(2*np.pi*n*f0*t)
        except:
            print("e")
            pass
    return sum



def main():
    y = []
    f = []
    plt.style.use("ggplot")
    x_ = np.linspace(-5,5,1000)
    plt.show()
    for i in x_:
        y.append(squareWave(i))
        f.append(fourier(armonics,i))

    plt.plot(x_,y,color="blue",label="Signal")
    plt.plot(x_,f,color="red",label="Fourier series approximation")
    plt.title("Fourier Series approximation number of armonics: "+str(armonics))
    #plt.legend()
    plt.show()


if __name__ == '__main__':
        main()