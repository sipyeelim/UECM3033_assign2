import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy as sp


def image_svd(n):
    
    # Keep first and the none zero elements
    r_a=Sr.copy()
    g_a=Sg.copy()
    b_a=Sb.copy()

    r_a[n:800]=np.zeros_like(Sr[n:800])
    g_a[n:800]=np.zeros_like(Sg[n:800])
    b_a[n:800]=np.zeros_like(Sb[n:800])

    # to create a matrix of sigma to perform dot multiplication
    # change the dimension of r_a, g_a and b_a to (800,1000)  
    r1 = sp.linalg.diagsvd(r_a,800,1000)
    g1 = sp.linalg.diagsvd(g_a,800,1000)
    b1 = sp.linalg.diagsvd(b_a,800,1000)

    # to perform dot multiplication for new matrix
    r_new = np.dot(np.dot(Ur,r1), Vr)
    g_new = np.dot(np.dot(Ug,g1), Vg)
    b_new = np.dot(np.dot(Ub,b1), Vb) 

    img[:,:,0]= r_new
    img[:,:,1]= g_new
    img[:,:,2]= b_new

    #Use to plot the new images
    fig2 = plt.figure(n)
    ax1 = fig2.add_subplot(2,2,1)
    ax2 = fig2.add_subplot(2,2,2)
    ax3 = fig2.add_subplot(2,2,3)
    ax4 = fig2.add_subplot(2,2,4)
    ax1.imshow(img)
    ax2.imshow(r, cmap = 'Reds')
    ax3.imshow(g, cmap = 'Greens')
    ax4.imshow(b, cmap = 'Blues')
    plt.show()


#original resolution set
img=mpimg.imread('image.jpg')
[r,g,b] = [img[:,:,i] for i in range(3)]
fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img)
ax2.imshow(r, cmap = 'Reds')
ax3.imshow(g, cmap = 'Greens')
ax4.imshow(b, cmap = 'Blues')
plt.show()

#to find U, sigma and V of red, green and blue matrix.
Ur, Sr, Vr = sp.linalg.svd(r) 
Ug, Sg, Vg = sp.linalg.svd(g) 
Ub, Sb, Vb = sp.linalg.svd(b) 

#check the none zero elements in sigma of red, green and blue matrices
nonezero_r=np.count_nonzero(Sr)
nonezero_g=np.count_nonzero(Sg)
nonezero_b=np.count_nonzero(Sb)
print("The number of none zero elements in original Sigma of red is", nonezero_r,", green is" ,nonezero_g,"and blue is" ,nonezero_b)


#low resolution, sigma 30
image_svd(30)

#good resolution, sigma 200
image_svd(200)
