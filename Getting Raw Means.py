import numpy as np
import os


#file path to the folder containing text files of captures
filloc = '/Users/andrewharman/Documents/VirtualShare/Grid sensors/Grid Data/9 capture magnet/raw'

os.chdir(filloc)#navigates to the text files

files = sorted(os.listdir(filloc))#creates an array of the file names and sorts them

print files

print len(files)

def meancol(j): #function which takes an input of the number of 
    values = []
    for i in range (0,100):
        values.append(data[i][j])
        mean = np.mean(values)
    return mean


f = open("mean values.txt","w+") #opens/creates a file with the given name


captures = len(files)-2 #as the file we just created is in the same directory as the data
                        #we subtract 1 from the number of files to find the number of captures




for k in range(0,captures):
    
    data = np.loadtxt(files[k],delimiter = ',')
    means = []
    
    for j in range (0,27):
    
        means.append(round(meancol(j),3))#this loop iterates through each column and appends the mean value to the means array
        f.write(str(means[j]))#writes the line of means to the new file
        if j < 26:
            f.write(", ")


    f.write("\n") #signals the end of a line so the next line of means will fill below the first

f.close() #closes the file
