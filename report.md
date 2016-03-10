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

To generate these pictures, first we need to read the image.jpg into the img that contain 3 matrices which is r, g and b. 

What is a sparse matrix?
Sparse matrix is a matrix that contain the most of zero elements. But if the matrix has the most of nonzero element, then the matrix is considered dense. In this case, we keep the first 30 element of sigma and other set to be zero, this will be forming the sparse matrix. The dimension of the sigma is change to the (800,1000) which will create a large sparse matrix. After that, the sparse matrix will help to create a lower resolution picture when it is using the dot multiplication to combine the U and V.

-----------------------------------

<sup>last modified: change your date here</sup>
