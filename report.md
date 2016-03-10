UECM3033 Assignment #2 Report
========================================================

- Prepared by: Lim Sip Yee
- Tutorial Group: T3

--------------------------------------------------------

## Task 1 --  $LU$ Factorization or SOR method

The reports, codes and supporting documents are to be uploaded to Github at: 

[https://github.com/sipyeelim/UECM3033_assign2.git](https://github.com/your_github_id/UECM3033_assign1)

Explain your selection criteria here.

Explain how you implement your `task1.py` here.

---------------------------------------------------------

## Task 2 -- SVD method and image compression

Put here your picture file (image.jpg)

![image.jpg](image.jpg)

How many non zero element in $\Sigma$?
All element like red, blue and green in $\Sigma$ are non zero element.

A lower resolution of sigma 30

![resolution_30_image.png](resolution_30_image.png)

A good resolution of sigma 200

![resolution_200_image.png](resolution_200_image.png)

To generate these pictures, first we need to read the image.jpg into the img that contain 3 matrices which is r, g and b. Each of the matrices r, g and b is a 3 dimension matrix. We named the Ur, Sr and Vr for the red matrix to get the U, sigma and V of the matrix by using scipy.linalg.svd. Also repeat it with green matrix as Ug, Sg, Vg and blue matrix as Ub, Sb and Vb to find the matrices.

After that, we use the numpy.count_nonzero to find out the none zero element and use the "plt.figure" to plot the image. Since we need to construct a lower resolution matrix, our image need to compress by keeping only the first 30 of none zero elements in the sigma and other become the zero elements in the sigma.

After create the low resolution image, we still need to create another better resolution image. So we created the self define function to plot the image. For the first, we use the Sr.copy. Sr.copy is to prevent loss of information from the copy of the original sigma and we apply this to red, blue and green matrices. After that, we use the r_a[n:800]=np.zeros_like(Sr[n:800]) to keep or set the element whether become zero or none zero. By using sp.linalg.diagsvd, we can avoid the dimension error happened when it combine U, sigma and v by dot multiplication to let r_a changes to dimension (800x1000) from the originally (800,1), its same goes to r_b and r_g. The new matrix will be create by the dot multiplication of np.dot. Finally, a new lower resolution image plotted.    



What is a sparse matrix?

Sparse matrix is a matrix that contain the most of zero elements. But if the matrix has the most of nonzero element, then the matrix is considered dense. In this case, we keep the first 30 element of sigma and other set to be zero, this will be forming the sparse matrix. The dimension of the sigma is change to the (800,1000) which will create a large sparse matrix. After that, the sparse matrix will help to create a lower resolution picture when it is using the dot multiplication to combine the U and V.

-----------------------------------

<sup>last modified: change your date here</sup>
