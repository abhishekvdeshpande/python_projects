#Task: To compute Trimmed Mean

import math
import sys


def rnd(num):                                                       #function to round the value of alpha
    str1 = str(num)                                                 #converting the input to string
    str2 = str1.split(".")                                          #split the function to access the mantis part of the floating point number
    str3 = str2[1]                                                  #access the mantis part 
    str4 = str3[:1]                                                 #reads the first number of mentis 
    if(str4 >= "5"):                                                #checks whether the mentis part is greater than 5 just to decide whether to floor or ceil the value
        return math.ceil(num)                                       #ceils the value
    else:
        return math.floor(num)                                      #floors the value


def TrimmedMean(datapoints,alpha):                                  #function to calculate TrimmedMean
        
               
    if(len(datapoints) != 0):                                       #compute the mean if there are values in the dataset. ie: list should not be empty.
        trimmed_mean = sum(datapoints)/len(datapoints)              #formula to calculate Mean
        return trimmed_mean
                                    


def mean(dataset):
    if(len(dataset) != 0):                                          #compute the mean if there are values in the dataset. ie: list should not be empty.
        Mean = sum(dataset)/len(dataset)                            #formula   
        return Mean 

#calculate median
def median(datapoints,alpha):
    if (len(datapoints) > 0):
        
        copylist = datapoints[:]
        if (len(copylist) % 2 == 0):
            rightmid = (len(copylist) // 2)
            leftmid = rightmid - 1
            median = (copylist[leftmid] + copylist[rightmid]) / 2
        else:
            mid = (len(copylist)//2)
            median = copylist[mid]
        return median
    else:
        return IndexError




def centralTend():
    dataset = input('Enter input: ')                                #reads input from the user
    read_list = list(map(float,dataset.split()))                    #maps all the data entered to floating point.
    datapoints = sorted(read_list)                                  #sorts the list in ascending order
    print("Ordered datapoints:" , datapoints)                       #prints the sorted set of datapoints
    alpha = input('Enter percent value: ')                          #allows user to enter the alpha value
    
    if not datapoints:                                              #compute the mean if there are no values in the dataset. ie: list should not be empty.
        if not alpha:                                               #no alpha input provided
            print("No datapoint and no percentage given")
            sys.exit(0)
        else:
            print("No data points entered")
            sys.exit(0)
    elif datapoints:
        if not alpha:                                               #if alpha value is not given
            print("Percentage value not given. Hence considered it as zero")
            alpha = 0                                               #initializing alpha to 0 so that I will be assigning it when I don't give alpha value it takes 0
            print("Trimmed mean is equal to normal Mean as alpha value is zero")
            mn = mean(datapoints)
            print('Mean: ' , mn)
            med = median(datapoints,alpha) 
            print('Meadian: ' , med)
            sys.exit(0)
        else:

            alpha_percent = int(alpha)/100                          #calculates the alpha percent
            pop = rnd(len(datapoints)*alpha_percent)                #gives the value to trim/remove the calcualted datapoints from the original datapoints

            if(pop >= math.ceil(len(datapoints)/2)):                #if the number of values to trimmed are more than the half of the length of datapoints then will print error message(Error handling)
                print('No data points are left out in the list')
                mn = mean(datapoints)
                print('Mean: ' , mn)
                    
            elif(pop == 0):                                         #condition where no elements will be popped 
                print('No trimming of datapoints required ')
                mn = mean(datapoints)
                print('Mean: ' , mn)
                med = median(datapoints,alpha) 
                print('Median: ' , med)


                    
            else:
                mn = mean(datapoints)
                print('Mean: ' , mn)
                datapoints = datapoints[pop:-pop]
                new_mean = TrimmedMean(datapoints,alpha)
                print('TrimmedMean: ' , new_mean)
                med = median(datapoints,alpha) 
                print('Median: ' , med)

centralTend()
