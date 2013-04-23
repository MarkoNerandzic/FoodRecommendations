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
    fileInteraction = FileIO()
    fileInteraction.getInfoFromFile()
    ageArray = fileInteraction.getAgeArray()
    countryArray = fileInteraction.getCountryArray()
    firstNationalityArray = fileInteraction.getFavNationalityArray()
    secondNationalityArray = fileInteraction.getSecondFavNationalityArray()
    thirdNationalityArray = fileInteraction.getThirdFavNationalityArray()
    genderArray = fileInteraction.getGenderArray()
    nationalityArray = fileInteraction.getNationalityArray()
    spicyArray = fileInteraction.getSpicyArray()

    userInteraction = UserIO()
    userInteraction.getInitialInformation()
    age = userInteraction.getAgeRange()
    country = userInteraction.getLocation()
    favourites = userInteraction.getFoodFavorites()
    firstFavourite = favourites[0]
    secondFavourite = favourites[1]
    thirdFavourite = favourites[2]
    gender = userInteraction.getGender()
    nationality = userInteraction.getNationality()
    spicy = userInteraction.getSpicy()

    sortClass = Sort(gender, nationality, age, spicy, favourites, country, genderArray, nationalityArray, ageArray, spicyArray, countryArray, firstNationalityArray, secondNationalityArray, thirdNationalityArray)
    recommendations = sortClass.getRankings()
    userInteraction.displayRecommendations(recommendations)


if __name__ == '__main__':
    main()
