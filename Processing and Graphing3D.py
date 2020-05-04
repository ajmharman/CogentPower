import numpy as np
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from natsort import natsorted #you may need to dowload the natsort package


def lstdir(directory):  #this is some code used instead of os.listdir to list files
                           #without listing hidden files which crash the code if listed
    fileslist = os.listdir(directory)
    return [x for x in fileslist if not (x.startswith('.'))]


#filloc file path to the folder containing text files of captures

#!!! EDIT for use!!!
filloc = '/Users/andrewharman/Documents/VirtualShare/Grid sensors/Grid Data/36 capture magnet/raw'
#!!! EDIT for use !!!


os.chdir(filloc)#navigates to the text files

f=open("dataforgraph.txt","w+") #opens a file to record the graph data this code produces 


files = natsorted(lstdir(filloc))#creates an array of the file names and sorts them

#print files    #use to check if necessary that you're in the right place

#print len(files) #should be number of means files

def meancol(j): #function which takes an input of the number of 
    values = []
    for i in range (0,100):
        values.append(data[i][j])
        mean = np.mean(values)
    return mean



captures = len(files)-1 #as the file we create in this code are in the same directory as the means
                        #we subtract 1 from the number of files to find the number of captures

print files #do this to double check the code is operating in the right place

means = []
for k in range(0,captures):
    
    data = np.loadtxt(files[k],delimiter = ',')
    capmean = []

    for j in range (0,27):
        capmean.append(round(meancol(j),3))#this loop iterates through each column and appends the mean value to the means array

    means.append(capmean)


#!!!EDIT!!!
#here you enter your start positions x and then y in the two arrays inside s1posxy in the order of the captures
s1posxy = [[0,14,84,98,168,182,182,168,98,84,14,0,0,14,84,98,168,182,182,168,98,84,14,0,0,14,84,98,168,182,182,168,98,84,14,0],
           [0,0,0,0,0,0,14,14,14,14,14,14,84,84,84,84,84,84,98,98,98,98,98,98,168,168,168,168,168,168,182,182,182,182,182,182]]

    
def writeline(i,j):
    capture = i
    sensor = j
    startpos = [s1posxy[0][i],s1posxy[1][i]] #takes the start position from the array based on which capture it is
    line = []

        #the means array is made up of individual arrays for each capture
        #each of these following statements select the correct capture from the means based on the i value and the correct
        #sensor based on the 'if j' 
        
    if j == 0:
        line.append(startpos[0])
        line.append(startpos[1])
        line.append(0)
        line.append(means[i][3*j])
        line.append(means[i][3*j+1])
        line.append(means[i][3*j+2])
        
    if j == 1:
        pos1 = np.add(startpos,[0,28]) #lines like this adjust the position written based on which sensor it is
        line.append(pos1[0])
        line.append(pos1[1])
        line.append(0)
        line.append(means[i][3*j])
        line.append(means[i][3*j+1])
        line.append(means[i][3*j+2])

    if j == 2:
        pos2 = np.add(startpos,[0,56])
        line.append(pos2[0])
        line.append(pos2[1])
        line.append(0)
        line.append(means[i][3*j])
        line.append(means[i][3*j+1])
        line.append(means[i][3*j+2])

    if j == 3:
        pos3 = np.add(startpos,[-28,0])
        line.append(pos3[0])
        line.append(pos3[1])
        line.append(0)
        line.append(means[i][3*j])
        line.append(means[i][3*j+1])
        line.append(means[i][3*j+2])

        
    if j == 4:
        pos4 = np.add(startpos,[-28,28])
        line.append(pos4[0])
        line.append(pos4[1])
        line.append(0)
        line.append(means[i][3*j])
        line.append(means[i][3*j+1])
        line.append(means[i][3*j+2])

    if j == 5:
        pos5= np.add(startpos,[-28,56])
        line.append(pos5[0])
        line.append(pos5[1])
        line.append(0)
        line.append(means[i][3*j])
        line.append(means[i][3*j+1])
        line.append(means[i][3*j+2])

    if j == 6:
        pos6 = np.add(startpos,[-56,0])
        line.append(pos6[0])
        line.append(pos6[1])
        line.append(0)
        line.append(means[i][3*j])
        line.append(means[i][3*j+1])
        line.append(means[i][3*j+2])

    if j == 7:
        pos7 = np.add(startpos,[-56,28])
        line.append(pos7[0])
        line.append(pos7[1])
        line.append(0)
        line.append(means[i][3*j])
        line.append(means[i][3*j+1])
        line.append(means[i][3*j+2])

    if j == 8:
        pos8 = np.add(startpos,[-56,56])
        line.append(pos8[0])
        line.append(pos8[1])
        line.append(0)
        line.append(means[i][3*j])
        line.append(means[i][3*j+1])
        line.append(means[i][3*j+2])

    return line

cooldata = []
xpos = []
ypos = []
zpos = []
xmag = []
ymag = []
zmag = []

for i in range (0,captures):    #iterates over the number of captures
    for j in range(0,9):#iterates over each sensor
        cooldata.append(writeline(i,j))
        xpos.append(writeline(i,j)[0])
        ypos.append(writeline(i,j)[1])
        zpos.append(writeline(i,j)[2])
        xmag.append(writeline(i,j)[3])
        ymag.append(writeline(i,j)[4])
        zmag.append(writeline(i,j)[5])
        for l in range(0,6):#iterates over each array element in a line to be written
            f.write(str(writeline(i,j)[l])) #writes each element from a line into the file (eliminates square brackets in read out)
            if l < 5:
                f.write(", ") #writes a comma after each value but not the last one
        f.write("\n")#ends the line

f.close() #closes the file


X = xpos
Y = ypos
Z = zpos
U = xmag
V = ymag
W = zmag

plt.figure()
plt.title("Barmagnet field lines in xy plane")
Q = plt.quiver(X, Y, U, V,
               pivot='mid')
qk = plt.quiverkey(Q, 0.9, 0.9, 1, r'$1 \frac{m}{s}$', labelpos='E',
                   coordinates='figure')
plt.scatter(X, Y, color='r', s=5)



fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')
ax.set_xlim3d(-75,200)
ax.set_ylim3d(-30,280)
ax.set_zlim3d(-3,3)
ax.quiver(X,Y,Z,U,V,W, pivot = 'tail')
plt.title("Barmagnet field lines 3D")

plt.show()

