import matplotlib.pyplot as plt
import numpy as np
import ggplot as gp



T = 1
pause = 0.25
harmonics = 1
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


def res():
    g = gp.ggplot(gp.aes(x='carat', y='price'), data=gp.diamonds)
    g = g + gp.geom_point()
    g = g + gp.ylab(' ')+ gp.xlab(' ')
    g.make()
    # obtain figure from ggplot
    fig = plt.gcf()
    ax = plt.gca()
    # adjust some of the ggplot axes' parameters
    ax.set_title("ggplot plot")
    ax.set_xlabel("Some x label")
    ax.set_position([0.1, 0.55, 0.4, 0.4])
    
    #plot the rest of the maplotlib plots
    for i in [2,3,4]:
        ax2 = fig.add_subplot(2,2,i)
        ax2.imshow(np.random.rand(23,23))
        ax2.set_title("matplotlib plot")
    plt.show()



def main():
    res()
    #y = []
    #f = []
    #a1 = []
    #a2 = []
    #a3 = []
    #plt.style.use("ggplot")
    #x_ = np.linspace(-5,5,1000)
    #for i in x_:
    #    y.append(squareWave(i))
    #    f.append(fourier(harmonics,i))
    #    a1.append(fourier(1,i))
    #    a2.append(fourier(2,i))
    #    a3.append(fourier(3,i))
    #
    #p1 = plt.plot(x_,y,color="blue",label="Signal")
    #p2 = plt.plot(x_,f,color="red",label="Signal approximation")
    ##plt.plot(x_,a1,color="yellow",label="a1")
    ##plt.plot(x_,a2,color="green",label="a2")
    ##plt.plot(x_,a3,color="purple",label="a3")
    #plt.title("Approximation with n="+str(harmonics))
    #grid.arrange(p1, p2, nrow = 1)
    #plt.legend()
    #plt.show()


if __name__ == '__main__':
        main()