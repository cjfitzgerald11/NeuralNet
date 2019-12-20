# Perceptron

This program can be used to classify hand written digits. 

Digits must be binary representations, 1's where pencil is drawn, 0's where there is no writting

Reccomend using the msnit data set

A valid data set of 8x8 and 32x32 digit represenations is already provided

To run the program run the following command 

Python3 Classifier.py lr epochs imageSize biasNodes outputNodes

lr = learning rate (decimal value between 0-1)
epochs = # of training epochs 
imageSize = 8 (for 8x8) or 32 (for 32x32)
biasNodes = 0 for no bias nodes or 1 for 1 bias node (can add more)
outputNodes = 1 or 10 (only two valid options)

1. The program will output the test success after each training epoch. 
2. The run time after each epoch. 
3. the best testing accuracy during training. 
