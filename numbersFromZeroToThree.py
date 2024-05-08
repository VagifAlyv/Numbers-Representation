
import numpy as np
import matplotlib.pyplot as plt

#Number 1:
def NumberOne():
    x1_values = np.linspace(2, 4, 2000)  
    x2_values = np.linspace(4, 5, 2000)
    x3_values = np.linspace(5, 5.001, 20000)
    x4_values = np.linspace(3, 7)
    def S1(x):
        return 4 + 1/3 * (x-2) + 1/24 * (x-2)**3

    def S2(x):
        return 5 + 5/6 * (x-4) + 1/4 * (x-4)**2 -1/12 * (x-4)**3

    def S3(x):
        return 6 - 5000*(x-5)
    
    def S4(x):
        return 1 + 1/4000 * (x-3)

    # Plot S1
    
    plt.plot(x1_values, S1(x1_values))

    # Plot S2
    plt.plot(x2_values, S2(x2_values))

    # Plot S3
    plt.plot(x3_values, S3(x3_values))

    # Plot S4
    plt.plot(x4_values, S4(x4_values))

    plt.xlim(0,12)
    plt.ylim(0,12)
    plt.show()
    

#Number 2:
def NumberTwo():
    x1_values = np.linspace(4, 5, 1000)  
    x2_values = np.linspace(5, 7, 1000)
    x3_values = np.linspace(3, 7, 1000)
    x4_values = np.linspace(3, 7, 1000)

    def S1(x):
        return 5 + 4/3 * (x-4) -1/3 * (x-4)**3

    def S2(x):
        return 6 + 1/3 * (x-5) -(x-5)**2 + 1/6 * (x-5)**3

    def S3(x):
        return 1 + 3/4 * (x-3)

    def S4(x):
        return 1 + 1/4000 * (x-3)

    plt.plot(x1_values, S1(x1_values))

    # Plot S2
    plt.plot(x2_values, S2(x2_values))

    # Plot S3
    plt.plot(x3_values, S3(x3_values))

    # Plot S4
    plt.plot(x4_values, S4(x4_values))

    plt.xlim(0,12)
    plt.ylim(0,12)
    plt.show()

#Number 0:
def NumberZero():
    x1_values = np.linspace(3, 5, 2000) 
    x2_values = np.linspace(5, 7, 2000)
    x3_values = np.linspace(3, 5, 2000)
    x4_values = np.linspace(5, 7, 2000)

    def S1(x):
        return 4 + 1.5 * (x-3) - 1/8 * (x-3)**3

    def S2(x):
        return 6 -3/4 * (x-5)**2 + 1/8 * (x-5)**3

    def S3(x):
        return 4 - 3/2 * (x-3) + 1/8 * (x-3)**3
    
    def S4(x):
        return 2 + 3/4 * (x-5)**2 - 1/8 *(x-5)**3

    # Plot S1
    plt.plot(x1_values, S1(x1_values))

    # Plot S2
    plt.plot(x2_values, S2(x2_values))

    # Plot S3
    plt.plot(x3_values, S3(x3_values))

    # Plot S4
    plt.plot(x4_values, S4(x4_values))

    plt.xlim(0,12)
    plt.ylim(0,12)
    plt.show()

#Number Three: 
def NumberThree():

    x1_values = np.linspace(3, 5, 2000)  
    x2_values = np.linspace(5, 3, 2000)
    x3_values = np.linspace(3, 5, 2000)
    x4_values = np.linspace(3, 4, 2000)
    x5_values = np.linspace(4, 5, 2000)

    def S1(x):
        return 5 + 1/2000* (x-3)

    def S2(x):
        return 5 + (x - 5)

    def S3(x):
        return 3 + 1/2000 * (x-3)
    
    def S4(x):
        return 2 - 7/4 * (x-3) + 3/4 * (x-3)**3

    def S5(x):
        return 1 + 0.5 * (x-4) + 9/4 * (x-4)**2 - 3/4 * (x-4)**3

    # Plot S1
    plt.plot(x1_values, S1(x1_values))

    # Plot S2
    plt.plot(x2_values, S2(x2_values))

    # Plot S3
    plt.plot(x3_values, S3(x3_values))

    # Plot S4
    plt.plot(x4_values, S4(x4_values))

    # Plot S5
    plt.plot(x5_values, S5(x5_values))

    plt.xlim(0,12)
    plt.ylim(0,12)
    plt.show()



NumberZero()
NumberOne()
NumberTwo()
NumberThree()