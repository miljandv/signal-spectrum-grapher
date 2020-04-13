import matplotlib.pyplot as plt
import numpy as np
import argparse


T = 1
pause = 0.25
f0 = 1/T
order = 6
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



def cosine_n(t,n):
    hn_k=2*abs(Xn(n))*np.cos(2*np.pi*n*f0*t+amplitude_spectrum(t))
    return hn_k


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
    a0 = tau-pause
    sum = a0
    for n in range(1,n_max):
        try:
            sum = sum + 2*Xn(n)*np.cos(2*np.pi*n*f0*t)
        except:
            print("e")
            pass
    return sum



def main_draw():
    parser = argparse.ArgumentParser(description='Signal spectrum drawer')
    parser.add_argument('--T', type=int, default=1, help='Signal period')
    parser.add_argument('--pause', type=float, default=0.25, help='Signal pause')
    parser.add_argument('--order', type=int, default=6, help='Order of fourier approximation')
    parser.add_argument('--amp', type=int, default=2, help='Signal amplitude')
    opt = parser.parse_args()
    T = opt.T
    amp = opt.amp
    order = opt.order
    amp = opt.amp
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
        f.append(fourier(order,i))
        X_0.append(X0(i))
        X_1.append(cosine_n(i,2))
        X_2.append(cosine_n(i,3))
        X_3.append(cosine_n(i,4))
        a0.append(fourier(1,i))
        a1.append(fourier(2,i))
        a3.append(fourier(4,i))
        a10.append(fourier(11,i))
        a100.append(fourier(101,i))
    for i in x_n:    
        amp_spec.append(amplitude_spectrum(i))
        phase_spec.append(phase_spectrum(i))

    
    fig, ((ax1,ax2), (ax3, ax4), (ax5, ax6),(ax7, ax8),(ax9, ax10),(ax11, ax12)) = plt.subplots(6, 2,sharex=True)
    fig.suptitle('OTR')
    ax1.plot(x_, y)
    ax2.stem(x_n, amp_spec, 'tab:orange',use_line_collection = True)
    ax3.stem(x_n, phase_spec, 'tab:green',use_line_collection = True)
    ax4.plot(x_, X_0, 'tab:red')
    ax5.plot(x_,X_1)
    ax6.plot(x_,X_2)
    ax7.plot(x_,X_3)
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


    plt.show()


def draw_amp_sp():
    amp_spec = []
    x_n = np.linspace(-5,5,100)
    for i in x_n:    
        amp_spec.append(amplitude_spectrum(i))
    plt.stem(x_n, amp_spec, 'tab:orange',use_line_collection = True)
    plt.show()



def draw_ph_sp():
    phase_spec = []
    x_n = np.linspace(-5,5,100)
    for i in x_n:    
        phase_spec.append(phase_spectrum(i))
    plt.stem(x_n, phase_spec, 'tab:orange',use_line_collection = True)
    plt.show()




def draw_compared():
    y = []
    a10 = []
    x_ = np.linspace(-5,5,1000)
    for i in x_:
        y.append(squareWave(i))
        a10.append(fourier(11,i))
    plt.plot(x_, y)
    plt.plot(x_,a10)
    plt.show()



def main():
    main_draw()



    

if __name__ == '__main__':
        main()