#-------------------------------------------------------------------------------
# Name:        FoodRecommendations
# Purpose:     To interact with each of the three classes in order to collect
#              user input, analyze it, and provide recommendations for the user.
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

from FileIO import *
from UserIO import *
from Sort import *
import jLibrary

def main():
    fileInteraction = FileIO() # Create instances of FileIO and UserIO
    userInteraction = UserIO()
    userInteraction.printWelcomeMessage() # Print the welcome message

    fileInteraction.getInfoFromFile() # Get the infro from the file
    ageArray = fileInteraction.getAgeArray() # Retreive the variablies required from the file
    countryArray = fileInteraction.getCountryArray()
    firstNationalityArray = fileInteraction.getFavNationalityArray()
    secondNationalityArray = fileInteraction.getSecondFavNationalityArray()
    thirdNationalityArray = fileInteraction.getThirdFavNationalityArray()
    genderArray = fileInteraction.getGenderArray()
    nationalityArray = fileInteraction.getNationalityArray()
    spicyArray = fileInteraction.getSpicyArray()

    userInteraction.getInitialInformation() # Get the user's information
    age = userInteraction.getAgeRange() # Retreive the variables required from the user
    country = userInteraction.getLocation()
    favourites = userInteraction.getFoodFavorites()
    firstFavourite = favourites[0]
    secondFavourite = favourites[1]
    thirdFavourite = favourites[2]
    gender = userInteraction.getGender()
    nationality = userInteraction.getNationality()
    spicy = userInteraction.getSpicy()

    sortClass = Sort(gender, nationality, age, spicy, favourites, country, genderArray, nationalityArray, ageArray, spicyArray, countryArray, firstNationalityArray, secondNationalityArray, thirdNationalityArray)
    recommendations = sortClass.getRankings() # Sort the recommendations and then get the rankings from the class
    userInteraction.displayRecommendations(recommendations) # Display the recommendations

if __name__ == '__main__':
    main()
