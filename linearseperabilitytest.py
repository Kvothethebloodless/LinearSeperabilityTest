import numpy as np
#from cvxopt import matrix, solvers
try:
			from cvxopt import matrix
			from cvxopt import solvers
	
except ImportError:
			print "CVXOPT Module not found. Please install."


class LStest():
	
	def __init__(self,cl1_data,cl2_data):
		
		
		if cl1_data.shape[1]!=cl2_data.shape[1]:
			raise Exception
		self.cl1_data =cl1_data;
		self.cl2_data = cl2_data;
		self.ndim = cl1_data.shape[1]
		self.create_A()
		self.create_B()
		self.create_C()
		
	
	#Solve AX<=B subject to minimizing CX
	def create_A(self):
		c1 = np.hstack((-self.cl1_data,np.ones((self.cl1_data.shape[0],1))))
		c2 = np.hstack((self.cl2_data,-np.ones((self.cl2_data.shape[0],1))))
		A = np.vstack((c1,c2))
		A = matrix(A)
		self.A = A
	def create_B(self):
		b = -np.ones(self.cl1_data.shape[0]+self.cl2_data.shape[0]);
		self.B = matrix(b)
	def create_C(self):
		c = np.zeros(self.ndim+1);
		self.C = matrix(c)
	def test_seperability(self):
		try:
			sol=solvers.lp(self.C,self.A,self.B)
			
			if sol['x']!= None:
				print("\n \n-------------------------------------------------------------------------------------------------------------")
				print('\t\t\t\t\t     LINEARLY SEPERABLE')
				print ("-------------------------------------------------------------------------------------------------------------\n \n")
				print("The seperating hyper plane is: \n")
				print (sol['x'])
			else:
				print("\n \n-------------------------------------------------------------------------------------------------------------")
				print('\t\t\t\t\t    NOT LINEARLY SEPERABLE')
				print ("-------------------------------------------------------------------------------------------------------------\n \n")

			
		except ValueError, TypeError:
			print("Error with Matrices and Ranks")
			pass
				
	
