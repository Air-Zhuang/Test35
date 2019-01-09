import array

'''
array比list性能高很多
array和list的一个重要区别：array只能存放指定的数据类型

Type code 	C Type 	        Python Type 	Minimum size in bytes 	Notes
'b' 	  signed char 	        int 	            1 	 
'B' 	  unsigned char 	    int 	            1 	 
'u' 	  Py_UNICODE 	    Unicode character 	    2 	            (1)
'h' 	  signed short 	        int 	            2 	 
'H' 	  unsigned short 	    int 	            2 	 
'i' 	  signed int 	        int 	            2 	 
'I' 	  unsigned int 	        int 	            2 	 
'l' 	  signed long 	        int 	            4 	 
'L' 	  unsigned long 	    int 	            4 	 
'q' 	  signed long long 	    int 	            8 	            (2)
'Q' 	  unsigned long long 	int 	            8 	            (2)
'f' 	  float 	            float 	            4 	 
'd' 	  double 	            float 	            8
'''

my_array=array.array("i")
my_array.append(1)
# my_array.append("abc")      #会报错，因为类型指定了i
print(my_array)
