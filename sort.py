#-------------------------------------------------------------------------------
# Name:        Sort - Class of FoodRecommendations
# Purpose:     To sort the results and create recommendations for the user.
#
# Author:      Justin Moulton & Marko Nerandzic
#
# Created:     April 9, 2013
# Copyright:   (c) Justin Moulton & Marko Nerandzic 2013
# Licence:     This work is licensed under the Creative Commons
#              Attribution-NonCommercial-ShareAlike 3.0 Unported License.
#              To view a copy of this license, visit
#              http://creativecommons.org/licenses/by-nc-sa/3.0/.
#-------------------------------------------------------------------------------

class Sort():

    recommendations = [] # Create the three arrays required
    weights = []
    divideFactor = []
    finalThree = []

    def __init__(self, gender, nationality, age, spicy, favourites, location, genders, nationalities, ages, spicys, locations, nationalityOne, nationalityTwo, nationalityThree):
        self.rankNationalities(gender, nationality, age, spicy, favourites, location, genders, nationalities, ages, spicys, locations, nationalityOne, nationalityTwo, nationalityThree)
        self.applyDivideFactors()
        self.getThree() # Initialization function that gets the inputs then runs two functions, rankNationalities and getThree

    def getThree(self): # Function that gets the three final recommendations
        self.finalThree.append(self.getOne()) # Use the function getOne to get the first, then second, then third recommendation
        self.finalThree.append(self.getOne())
        self.finalThree.append(self.getOne())

    def applyDivideFactors(self): # Function to apply the divide factors
        counter = 0
        while counter < len(self.weights): # Go through the array and apply the divide factors to the weights
            self.weights[counter] = self.weights[counter] / self.divideFactor[counter]
            counter += 1

    def getOne(self): # Function to get a recommendation
        counter = 0 # Create the required variables
        biggest = 0
        while counter < len(self.weights): # While the counter is less than the array length,
            if self.weights[counter] > self.weights[biggest]: # If the current weight is bigger than the biggest,
                biggest = counter # then replace it with the new biggest
            counter += 1
        recommendation = self.recommendations[biggest] # The recommendation is the one with the biggest weight factor
        self.weights.pop(biggest) # Pop the places where the biggest was to facilitate finding the next recommendations
        self.recommendations.pop(biggest)
        return recommendation # Return the recommendation

    def rankNationalities(self, gender, nationality, age, spicy, favourites, location, genders, nationalities, ages, spicys, locations, nationalityOne, nationalityTwo, nationalityThree):
        weightFactor = 0 # Function to rank the nationalities
        counterTwo = 0

        while counterTwo < 3: # Run this three times, once each for the user's favourites
            index = 0
            while index < len(nationalityOne): # While the index is less than the length of nationalityOne,
                if favourites[counterTwo] == nationalityOne[index]: # If the favourites match,
                    weightFactor += 1.0 # increment the weight factor
                    if gender == genders[index]: # If the genders match,
                        weightFactor += 1.0 # increment the weight factor
                    if nationality == nationalities[index]: # Do the same for each demographic
                        weightFactor += 1.0
                    if age == ages[index]:
                        weightFactor += 1.0
                    if spicy == spicys[index]:
                        weightFactor += 1.0
                    if location == locations[index]:
                        weightFactor += 1.0
                    indexTwo = -1 # Set the two new variables to -1
                    indexThree = -1

                    counter = 0
                    while counter < len(self.recommendations): # Check the recommendations array to ensure that the favourite is not already listed
                        if nationalityTwo[index] == self.recommendations[counter]: # If the recommendation is already included,
                            indexTwo = counter # save the index
                        counter += 1

                    counter = 0
                    while counter < len(self.recommendations): # Do the same for the third favourite
                        if nationalityThree[index] == self.recommendations[counter]:
                            indexThree = counter
                        counter += 1

                    if indexTwo == -1: # If no match was found, create a new entry
                        self.recommendations.append(nationalityTwo[index])
                        self.weights.append(weightFactor)
                        self.divideFactor.append(0.5)
                    else: # Else, just increment the nationality's ranking by the weight factor
                        self.weights[indexTwo] += weightFactor
                        self.divideFactor[indexTwo] += 0.5

                    if indexThree == -1: # Do the same thing for the third favourite, but reduce the weights by half
                        self.recommendations.append(nationalityThree[index])
                        self.weights.append((weightFactor / 2))
                        self.divideFactor.append(0.5)
                    else:
                        self.weights[indexThree] += (weightFactor / 2)
                        self.divideFactor[indexThree] += 0.5

                weightFactor = 0
                index += 1
            counterTwo += 1

        counter = 0
        while counter < len(self.recommendations): # Find if the program recommended a user's favourites
            if favourites[0] == self.recommendations[counter]:
                self.recommendations.pop(counter) # If so, remove those entries
                self.weights.pop(counter)
                self.divideFactor.pop(counter)
                counter = 0
            elif favourites[1] == self.recommendations[counter]: # Do that again for each favourite
                self.recommendations.pop(counter)
                self.weights.pop(counter)
                self.divideFactor.pop(counter)
                counter = 0
            elif favourites[2] == self.recommendations[counter]:
                self.recommendations.pop(counter)
                self.weights.pop(counter)
                self.divideFactor.pop(counter)
                counter = 0
            elif self.recommendations[counter] == '': # Do that again if the program recommended a blank nationality
                self.recommendations.pop(counter)
                self.weights.pop(counter)
                self.divideFactor.pop(counter)
                counter = 0
            counter += 1

    def getRankings(self): # Function that returns the finalThree recommendations when called
        return self.finalThree