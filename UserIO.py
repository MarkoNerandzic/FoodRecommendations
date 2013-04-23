#-------------------------------------------------------------------------------
# Name:        UserIO - Class of FoodRecommendations
# Purpose:     To interact with the user to get their inputs and then display
#              their recommendations.
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

import jLibrary

class UserIO():

    spicyPreference = 0
    gender = 0
    age = ''
    foodNationalitiesFavorites = []
    location = ''
    nationality = ''

    def getInitialInformation(self):
        self.spicyPreference = self.getSpicyFromUser()
        self.gender = self.getGenderFromUser()
        self.age = self.getAgeRangeFromUser()
        self.foodNationalitiesFavorites = self.getFoodFavoritesFromUser()
        self.location = self.getLocationFromUser()
        self.nationality = self.getNationalityFromUser()

    def getNationalityFromUser(self):
        return jLibrary.getStrInput('What is your nationality?')

    def getSpicyFromUser(self):
        spicyTemp = jLibrary.getOption("Do you like spicy food?\n[1]Yes\n[2]No\n[3]Sometimes", 1, 3)
        if spicyTemp == 1:
            return "Yes"
        elif spicyTemp == 2:
            return "No"
        else:
            return "Sometimes"

    def getGenderFromUser(self):
        genderTemp = jLibrary.getOption("What is your gender?\n[1]Male\n[2]Female", 1, 2)
        if genderTemp == 1:
            return "Male"
        else:
            return "Female"

    def getAgeRangeFromUser(self):
        userInputTemp = jLibrary.getOption("What age group are you in?\n[1]0-19\n[2]20-39\n[3]40-59\n[4]60-79\n[5]80-99\n[6]100+\n", 1, 6)
        if userInputTemp == 1:
            return "0-19"
        elif userInputTemp == 2:
            return "20-39"
        elif userInputTemp == 3:
            return "40-59"
        elif userInputTemp == 4:
            return "60-79"
        elif userInputTemp == 5:
            return "80-99"
        else:
            return "100+"

    def getFoodFavoritesFromUser(self):
        foodFavorites = []
        finishedGettingInput = False
        counter = 0
        while not finishedGettingInput:
            userInputTemp = jLibrary.getStrInput("Enter your next favorite food nationality or 'exit' to end your input!")
            counter += 1
            if userInputTemp.lower() == 'exit':
                finishedGettingInput = True
            elif counter == 3:
                foodFavorites.append(userInputTemp.lower())
                finishedGettingInput = True
            else:
                foodFavorites.append(userInputTemp.lower())
        return foodFavorites

    def getLocationFromUser(self):
        return jLibrary.getStrInput("What country do you currently reside in?")

    def displayRecommendations(self, recommendations):
        print ''
        counter = 0
        moreSuggestions = True
        while counter < len(recommendations) and moreSuggestions:
            print "Your",
            if counter%10 != 0 and counter%10 != 1 and counter%10 != 2:
                print "%s%s" % (counter, "th"),
            elif counter == 0:
                print "%s%s" % (counter + 1, "st"),
            elif counter == 1:
                print "%s%s" % (counter + 1, "nd"),
            else:
                print "%s%s" % (counter + 1, "rd"),
            print "recommendation is: %s%s" % (((recommendations[counter])[0]).upper(), (recommendations[counter])[1:])
            counter += 1

    def getSpicy(self):
        return self.spicyPreference.lower()

    def getGender(self):
        return self.gender.lower()

    def getAgeRange(self):
        return self.age.lower()

    def getFoodFavorites(self):
        return self.foodNationalitiesFavorites

    def getLocation(self):
        return self.location.lower()

    def getNationality(self):
        return self.nationality.lower()

    def printWelcomeMessage(self):
        print 'Welcome to the Food Nationality Recommendation program!'
        print 'This program will recommend different nationalities of food to users based on their own'
        print 'favourites and demographics by comparing their characteristics to the responses of other'
        print 'respondants.  Please ensure to type in your responses with correct spelling in order to'
        print 'ensure that the program understands your inputs.'
        print 'Program created by: Justin Moulton & Marko Nerandzic.'