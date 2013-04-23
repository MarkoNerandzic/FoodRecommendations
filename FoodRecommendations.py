#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Justin
#
# Created:     22/04/2013
# Copyright:   (c) Justin 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from FileIO import *
from UserIO import *
from sort import *
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
    (recommendations, weights) = sortClass.getRankings()
    counter = 0
    biggest = 0
    while counter < len(weights):
        if weights[counter] > weights[biggest]:
            biggest = counter
        counter += 1
    weights.pop(biggest)
    firstRecommendation = recommendations[biggest]
    recommendations.pop(biggest)
    counter = 0
    biggest = 0
    while counter < len(weights):
        if weights[counter] > weights[biggest]:
            biggest = counter
        counter += 1
    weights.pop(biggest)
    secondRecommendation = recommendations[biggest]
    recommendations.pop(biggest)
    counter = 0
    biggest = 0
    while counter < len(weights):
        if weights[counter] > weights[biggest]:
            biggest = counter
        counter += 1
    weights.pop(biggest)
    thirdRecommendation = recommendations[biggest]
    recommendations.pop(biggest)
    print firstRecommendation
    print secondRecommendation
    print thirdRecommendation

if __name__ == '__main__':
    main()
