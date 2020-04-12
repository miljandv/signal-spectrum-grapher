import matplotlib.pyplot as plt
import numpy as np



T = 1
pause = 0.25
harmonics = 6
f0 = 1/T
amp = 2
tau = T-pause



def squareWave(x):
    x+= 0.75/2.
    if((x%1)>0.75):
        return -1
    else:
        return 1


def X0(n):
    return tau-pause


def amplitude_spectrum(n):
    Xn = ((amp*tau)/T)*abs(np.sin(n*f0*np.pi*tau)/(n*f0*np.pi*tau))
    return Xn



def phase_spectrum(n):
    phase = 0
    ph = np.sin(n*f0*np.pi*tau)/(n*f0*np.pi*tau)
    if ph<0:
        phase = np.sign(n)*np.pi
    return phase



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
    X_0 = []
    X_1 = []
    X_2 = []
    X_3 = []
    a0 = []
    a1 = []
    a3 = []
    a10 = []
    a100 = []
    amp_spec = []
    phase_spec = []
    x_ = np.linspace(-5,5,1000)
    x_n = np.linspace(-5,5,100)
    for i in x_:
        y.append(squareWave(i))
        f.append(fourier(harmonics,i))
        a0.append(fourier(1,i))
        a1.append(fourier(2,i))
        a3.append(fourier(4,i))
        a10.append(fourier(11,i))
        a100.append(fourier(101,i))
    for i in x_n:    
        amp_spec.append(amplitude_spectrum(i))
        phase_spec.append(phase_spectrum(i))
        X_0.append(X0(i))
        X_1.append(Xn(2))
        X_2.append(Xn(3))
        X_3.append(Xn(4))
    
    fig, ((ax1,ax2), (ax3, ax4), (ax5, ax6),(ax7, ax8),(ax9, ax10),(ax11, ax12)) = plt.subplots(6, 2)
    fig.suptitle('OTR')
    ax1.plot(x_, y)
    ax2.stem(x_n, amp_spec, 'tab:orange')
    ax3.stem(x_n, phase_spec, 'tab:green')
    ax4.stem(x_n, X_0, 'tab:red')
    ax5.stem(x_n,X_1)
    ax6.stem(x_n,X_2)
    ax7.stem(x_n,X_3)
    ax8.plot(x_,a0)
    ax9.plot(x_,a1)
    ax10.plot(x_,a3)
    ax11.plot(x_,a10)
    ax12.plot(x_,a100)
    ax1.title.set_text('Original signal')
    ax2.title.set_text('Amplitude spectrum')
    ax3.title.set_text('Phase spectrum')
    ax4.title.set_text('X_0')
    ax5.title.set_text('X_1')
    ax6.title.set_text('X_2')
    ax7.title.set_text('X_3')
    ax8.title.set_text('a0')
    ax9.title.set_text('a1')
    ax10.title.set_text('a3')
    ax11.title.set_text('a10')
    ax12.title.set_text('a100')
    

    for ax in fig.get_axes():
        ax.label_outer()

    plt.show()



    

if __name__ == '__main__':
        main()