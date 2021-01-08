############################################################
######
######         Date Class
######
############################################################

# class to represent a calendar date 
class Date:

    # initialize the date
    def __init__(self, month, day, year):
        self._year = year

        if (month < 1):
            self._month = 1
        elif (month > 12):
            self._month = 12
        else:
            self._month = month

        numDays = self.daysPerMonth (self._month, year)
        if (day > 0 and day < numDays + 1):
            self._day = day
        elif (day > numDays):
            self._day = numDays
        else:
            self._day = 1
    
    # get the date values
    def getYear (self):
        return self._year
    def getMonth (self):
        return self._month
    def getDay (self):
        return self._day

    # set the date values
    def setYear (self, year):
        self._year = year
    def setMonth (self, month):
        self._month = month
    def setDay (self, day):
        self._day = day
    
    # find out if the year is a leap year
    def isLeapYear (self, year):
        isLeap = False
        if (year % 4 == 0):
            isLeap = True
        if (year % 100 == 0):
            isLeap = False
            if (year % 400 == 0):
                isLeap = True
        return isLeap

    # dictionary of the days per month
    daysInMonth = {1 : 31,
                   2 : 28,
                   3 : 31,
                   4 : 30,
                   5 : 31,
                   6 : 30,
                   7 : 31,
                   8 : 31,
                   9 : 30,
                   10 : 31,
                   11 : 30,
                   12 : 31}

    # find how many days are in the month
    def daysPerMonth (self, month, year):
        numDays = self.daysInMonth[month]
        isLeap = self.isLeapYear(year)

        if (month == 2 and isLeap == True):
            numDays = 29
        return numDays

    # see if two dates are the same
    def isSameDay (self, date):
        orgYear = self.getYear()
        orgMonth = self.getMonth()
        orgDay = self.getDay()
        compYear = date.getYear()
        compMonth = date.getMonth()
        compDay = date.getDay()
        isSame = False
        if (orgYear == compYear and orgMonth == compMonth and orgDay == compDay):
            isSame = True
        return isSame

    # increment the date
    def incrementDate (self):
        currYear = self.getYear()
        currMonth = self.getMonth()
        currDay = self.getDay()
        maxDays = self.daysPerMonth(self._month, self._year)

        currDay = currDay + 1
        if (currDay > maxDays):
            currDay = 1
            currMonth = currMonth + 1
            if (currMonth > 12):
                currMonth = 1
                currYear = currYear + 1

        self.setYear(currYear)
        self.setMonth(currMonth)
        self.setDay(currDay)

    # dictionary of the months
    whatMonth = {1 : "January",
                 2 : "February",
                 3 : "March",
                 4 : "April",
                 5 : "May",
                 6 : "June",
                 7 : "July",
                 8 : "August",
                 9 : "September",
                 10 : "October",
                 11 : "November",
                 12 : "December"}
                 
    # print the date
    def currDate (self):
        year = self.getYear()
        month = self.getMonth()
        day = self.getDay()
        currMonth = self.whatMonth[month]
        currDate = currMonth, day, year
        return currDate


############################################################
######
######         Utility Class
######
############################################################

# class to represent a customer's utilities
class Utility:

    # initialize the utility rate variables needed
    def __init__(self, utilityRate, anniversaryDate):
        self._utilityRate = utilityRate

        year = anniversaryDate.getYear()
        month = anniversaryDate.getMonth()
        day = anniversaryDate.getDay()
        toChange = False
        if (month == 2 and day == 29):
            toChange = True

        if (toChange) == True:
            self._anniversaryDate = anniversaryDate
        else:
            adjustDay = 28
            newDate = Date (month, adjustDay, year)
            self._anniversaryDate = newDate

        self._monthlyUsage = 0
        self._yearlyUsage = 0
        self._monthlyBill = 0
        self._balance = 0
        self._amountPaid = 0
        self._amountDelinquent = 0
        self._salesTaxRate = 0.0
        self._interestRate = 0.0

    # get the utility values
    def getUtilityRate (self):
        return self._utilityRate
    def getMonthlyUsage (self):
        return self._monthlyUsage
    def getYearlyUsage (self):
        return self._yearlyUsage
    def getMonthlyBill (self):
        return self._monthlyBill
    def getBalance (self):
        return self._balance
    def getAmountPaid (self):
        return self._amountPaid
    def getAmountDelinquent (self):
        return self._amountDelinquent
    def getAnniversaryDate(self):
        date = self._anniversaryDate.currDate()
        return date
    def getSalesTaxRate (self):
        return self._salesTaxRate
    def getInterestRate (self):
        return self._interestRate
    def getMonthlyCharge (self):
        monthlyCharge = self.getMonthlyUsage() * self.getUtilityRate()
        return monthlyCharge

    # set the utility values
    def setUtilityRate (self, utilityRate):
        self._utilityRate = utilityRate
    def setMonthlyUsage (self, monthlyUsage):
        self._monthlyUsage = monthlyUsage
    def updateYearlyUsage (self, yearUsage):
        self._yearlyUsage = self._yearlyUsage + yearUsage
    def setMonthlyBill (self, monthlyBill):
        self._monthlyBill = monthlyBill
    def updateBalance (self, balance):
        self._balance = self._balance + balance
    def updateAmountPaid (self, amountPaid):
        self._amountPaid = self._amountPaid + amountPaid
    def setAmountDelinquent (self, amountDelinquent):
        self._amountDelinquent = amountDelinquent

    def setAnniversaryDate (self, date):
        month = date.getMonth()
        day = date.getDay()
        doNotUpdate = False

        if (month == 2 and day == 29):
            doNotUpdate = True
        if (doNotUpdate) == False:
            self._anniversaryDate = date

    def setSalesTaxRate (self, taxRate):
        self._salesTaxRate = taxRate
    def setInterestRate (self, interestRate):
        self._interestRate = interestRate

    # make a utility payment
    def makePayment (self, paymentAmount):
        self.updateBalance (- paymentAmount)
        self.updateAmountPaid (paymentAmount)

    # processes payments and balances at the end of the month
    def endOfMonthProcessing (self):
        salesByMonthly = self.getSalesTaxRate() * self.getMonthlyCharge()
        amountAdded = self.getMonthlyCharge() + salesByMonthly
        self.updateBalance(amountAdded)

        delinquintDiff = self.getAmountPaid() - self.getMonthlyBill()
        self.setAmountDelinquent(self.getAmountDelinquent() - delinquintDiff)

        if self.getAmountDelinquent() > 0:
            extraCharge = self.getAmountDelinquent() * self.getInterestRate()
            self.updateBalance(extraCharge)
            self.setAmountDelinquent(self.getAmountDelinquent() + extraCharge)

        self.setMonthlyBill = self.getBalance()
        self._amountPaid = 0

    # processes payments and balances at the end of the year
    def endOfYearProcessing (self):
        self._yearlyUsage = 0


############################################################
######
######         Water Utility Class
######
############################################################
        
# class to represent a customer's water utilities
class WaterUtility (Utility):

    # initialize the water utility rate variables needed
    def __init__(self, utilityRate, anniversaryDate, numBaths, bathFee):
        super (WaterUtility, self).__init__(utilityRate, anniversaryDate)
        self._numBaths = numBaths
        self._bathFee = bathFee

    # get the water utility values
    def getNumBaths (self):
        return self._numBaths
    def getBathFee (self):
        return self._bathFee

    # set the water utility values
    def setNumBaths (self, numBaths):
        self._numBaths = numBaths
    def setBathFee (self, bathFee):
        self._bathFee = bathFee

    # furthers the getMonthlyCharge method in Utility class
    def getMonthlyChargeW (self, monthlyUsage):
        extraCharge = self.getNumBaths() * self.getBathFee()
        monthBill = monthlyUsage * self.getUtilityRate()
        
        monthlyCharge = monthBill + extraCharge
        return monthlyCharge


############################################################
######
######         Gas Utility Class
######
############################################################

# class to represent a customer's gas utilities
class GasUtility (Utility):

    # initialize the water utility rate variables needed
    def __init__(self, utilityRate, anniversaryDate):
        super (GasUtility, self).__init__(utilityRate, anniversaryDate)
        self._isInstallmentPlan = False
        self._installmentAmount = 0
    
    # get/set installmentPlan
    def getInstallmentPlan (self):
        return self._isInstallmentPlan
    def setInstallmentPlan (self, bool):
        self._isInstallmentPlan = bool

    # similar methods in utility class
    def endOfYearProcessing(self):
        self._installmentAmount = self.getYearlyUsage() / 12

    def getMonthlyChargeG (self, bool):
        monthCharge = 0
        if bool == True:
            monthCharge = self._installmentAmount
        else:
            monthCharge = self.getMonthlyCharge()
        return monthCharge
    
    def endOfMonthProcessingG (self):
        if self.getInstallmentPlan == True:
            self._monthlyBill = self._installmentAmount *  \
                        self.getSalesTaxRate() +   \
                        self.getAmountDelinquent
        else:
            self._monthlyBill = self.endOfMonthProcessing()


date = Date (1,2,2001)
print(date.currDate())