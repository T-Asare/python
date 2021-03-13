import os 
#==========================================================
# TASK DESCRIPTION
#==========================================================
# In this tas you will apply some of the key concepts in python
# some data processing routines encountered in data science

## You have been provided cvs file containing several records
# of sales transactions from a firm. You are expected to 
# complete the following excercises applying knowledge from you
# python programming course

## NB: In all the assignments, you MUST implement your solutions using
# functions. Some of the functions are provided from your conveneice


#==========================================================
# HELPER FUNCTIONS
#==========================================================

BASE_DIRECTORY = os.getcwd()# is used if the working files are in the same working current directory as the code
#alternatively to make this code more reusable across multiple devices, We can ask user for input for file directory using
#BASE_DIRECTORY = input("Kindly key in your file directory : ")
DATA_FOLDER = "data"

#The two lines below constructs the paths to the files needed for this
#if alternate implementation is used, then there is no need for the next wo lines as the files are called directly.
product_file =  os.path.join(BASE_DIRECTORY,DATA_FOLDER,'products.csv')
transaction_file=  os.path.join(BASE_DIRECTORY, DATA_FOLDER,'transactions.csv')

##################################################################################

def read_data(self,data_file=None):
    data_file = "C:/Users/Tim Asare/Downloads/data/iris.csv"
    with open(data_file,'r') as file_object:
        return file_object.read()


data = read_data("iris.csv").split("\n")
newdata = []
for row in data:
    newdata.append(row.split(",")[0:2])
newdata.pop()

newdata = newdata[:-50]


def write_data(data_file, data):
    data_file = os.path.join(BASE_DIRECTORY,DATA_FOLDER,data_file)
    with open(data_file,'w') as f:
        for row in data:
            f.write(",".join(row)+"\n")

write_data("newdata.csv", newdata)
##################################################################################








class Analysis():
    def __init__(self, file = None):
        self.file = file
        
    #************** HELPERS BEGIN HERE ********
    # These functions have been provided for 
    # your convenience. Use them without modification
    
    def whatType(self,inp):
        """
        Returns the type of data in a given collection of data. 
        Assumes all data in the collection is of the same type
        """
        if inp.isnumeric():
            return type(int(inp))

        #does the input contain a decimal point?
        elif inp.count('.')==1:
            if inp.split('.')[0].isnumeric() and inp.split('.')[1].isnumeric():
                return type(float(inp))
            else:
                return type(inp)
    
        else:
            return type(inp)
    
    
           
    def read_data(self,data_file = None):
        if data_file:
            data_file = os.path.join(BASE_DIRECTORY,DATA_FOLDER,data_file)
            with open(data_file,'r') as file_object:
                return file_object.readlines()
        else:
            data_file = os.path.join(BASE_DIRECTORY,DATA_FOLDER,self.file)
            with open(data_file,'r') as file_object:
                return file_object.readlines()
            
    #************** HELPERS END HERE ********
    
    #=================== Q1 =================
    #========================================
    def dimension(self, data):
        """
        Returns information about the dimensions of the data
        Parameters:
            data: [str/list], being data read in from that has been read from a file
        Returns:
             a tuple of the form (n_rows,n_cols) where
            n_rows = the number or rows
            n_cols = the number of columns

        Expected output using products.csv file:
        n_rows = 200
        n_cols = 7
        """

        if(type(data) == list):
            n_rows = len(data)-1 #number of rows
            n_cols =  len(data[0].split(",")) #number of columns
        elif(type(data) == str):
            data = data.split("\n")
            data.pop()
            n_rows = len(data)-1
            n_cols =  len(data[0].split(","))
        # *** ADD YOUR OWN LINES OF CODE BELOW THIS LINE ***

        return (n_rows,n_cols)

    
    #=================== Q2 =================
    #========================================

    def unique(self, data,column):
        """
            Params:
                data: list, raw data
                column: str, name of column to check for uinque values

            Returns:
                a list of ONLY the unique values values in columns
        """
        # sample column names to test
        # 'product_id,product_line,product_class,product_size,list_price

        unique_values = None 

        # *** ADD YOUR OWN LINES OF CODE BELOW THIS LINE ***
        titles = data[0].strip().split(",")
        if(column in titles):
            index = titles.index(column)

        unique_values = []
        for row in data[1:]:
            value = row.strip().split(",")[index]
            if(value != ""):
                unique_values.append(value)
        
        
        return list(set(unique_values))
    
    #Q3
    def info(self,data):
        """
        Params: 
            data: str, raw data read from file using read_data()
        Output:
            Prints out to the screen the following info about the data:
            - number of rows
            - number of columns
            - for each column, the columns name and the type of the data stored in that column 
        """
        # HIINT: use the function whatType() to help you get the type of the data in the columns

        # YOUR CODE AFTER THIS LINE
        print("Number of rows: " + str(self.dimension(data)[0]))
        print("Number of columns: " + str(self.dimension(data)[1]))

        Headings = data[0].strip().split(",")
        dataRow = data[1].strip().split(",")
        for title,item in zip(Headings,dataRow):
            print("{0} : {1}".format(title,self.whatType(item)))
        
        
        



# ====================== LEAVE THESE LINES ALONE ====================
# The lines of code bellow should run smoothly without any problem

analyze = Analysis('products.csv')
data = analyze.read_data()
# analyze.dimension(analyze.read_data())
# print(analyze.unique(data, column='product_class'))
analyze.info(data)
