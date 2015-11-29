# Scipt to test Linear Seperability of binary class data #

This script uses linear programming module ```CVXOPT``` to convert the linear seperability problem into a linear programming problem and solve it. 

Please Refer to [this link](http://www.joyofdata.de/blog/testing-linear-separability-linear-programming-r-glpk/) from the _Joy of Data_ blog for background on optimization formulation of the linear seperability problem .
Please install ```CVXOPT``` before using the script. [CVXOPT Installation](http://cvxopt.org/install/).

This script also uses ```NUMPY```. Please consider installing ```NUMPY```.

## Using the script ##

Initialize the class object `LStest()` with two variables, which hold the data in numpy matrices. The matrices should be of the dimensions `(no_samples,n_dim)` where `no_samples` are the number of points in that class and `n_dim` is the dimensionality of data points. `n_dim` should be the same for both matrices.

Then run the ```test_seperability()``` method to if the classes are linear seperable.

Code snippet illustrating usage.

```python
>>> run linearseperabilitytest.py
>>> A = LStest(c1_points,c2_points) ##c1_points.shape = (no_samples1,ndim),c2_points.shape = (no_samples2,ndim)
>>> A.test_seperability()

```

Standard Results if data is linearly seperable.

```python
>>> l1 =  [[1,0],[1,1]]
>>> l2 =  [[0,0],[0,1]]
>>> l1 = np.array(l1)
>>> l2 = np.array(l2)
>>> run linearseperabilitytest.py
>>> A = LStest(l1,l2)
>>> A.test_seperability()
    pcost       dcost       gap    pres   dres   k/t
    0:  0.0000e+00  4.0000e+00  4e+00  1e+00  2e+00  1e+00
    1:  0.0000e+00  4.0000e-02  4e-02  1e-02  2e-02  1e-02
    2:  0.0000e+00  4.0000e-04  4e-04  1e-04  2e-04  1e-04
    3:  0.0000e+00  4.0000e-06  4e-06  1e-06  2e-06  1e-06
    4:  0.0000e+00  4.0000e-08  4e-08  1e-08  2e-08  1e-08
    Optimal solution found.
	  
	   
    -------------------------------------------------------------------------------------------------------------
 	  					     LINEARLY SEPERABLE
    -------------------------------------------------------------------------------------------------------------
					      
						      
    The seperating hyper plane is: 
						      
    [ 4.00e+00]
    [ 4.75e-16]
    [ 2.00e+00]
```
						      



Results if the data is linearly inseperable. Example: XOR problem.



```python
>>> l1 =  [[0,0],[1,1]]
>>> l2 =  [[1,0],[0,1]]
>>> l1 = np.array(l1)
>>> l2 = np.array(l2)
>>> run linearseperabilitytest.py
>>> A = LStest(l1,l2)
>>> A.test_seperability()
    pcost       dcost       gap    pres   dres   k/t
    0:  0.0000e+00  4.0000e+00  4e+00  2e+00  0e+00  1e+00
    Certificate of primal infeasibility found.

       
    --------------------------------------------------------------------------------------------------------------
      						 NOT LINEARLY SEPERABLE
    --------------------------------------------------------------------------------------------------------------

```
		


