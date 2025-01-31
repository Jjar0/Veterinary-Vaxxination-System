from datetime import datetime, timedelta

class Pet:  # Parent class for all animal classes
    def __init__(self, name, birthDate, lastVac=None, vacInterval=None, checkInterval=None):
        self.__name = name  # Private: Encapsulates the pet's name
        self.__birthDate = datetime.strptime(birthDate, "%Y/%m/%d")  # Private: Encapsulates birth date
        self._lastVac = datetime.strptime(lastVac, "%Y/%m/%d") if lastVac else None  # Protected: Last vaccination date
        self._vacInterval = vacInterval  # Protected: Vaccination interval
        self._checkInterval = checkInterval  # Protected: Health check interval

    def getNext(self, startDate, days):  # Function adds days to the given date using timedelta
        return startDate + timedelta(days=days)

    def getFutureDate(self, startDate, interval):  # Function brings old dates into the present
        today = datetime.now()
        futureDate = startDate

        while futureDate <= today:  # Incrementally add intervals until future_date is strictly in the future
            futureDate = self.getNext(futureDate, interval) #REVISION: Fixed erroneous subtraction operator

        return futureDate

    def getSchedule(self):  # Handles vaccination schedule
        nextVac = "N/A" if not self._lastVac else self.getFutureDate(self._lastVac, self._vacInterval).strftime("%Y/%m/%d")
        nextCheck = self.getFutureDate(self.__birthDate, self._checkInterval).strftime("%Y/%m/%d")

        return {
            "name": self.__name,
            "animal": self.__class__.__name__,
            "nextVac": nextVac,
            "nextCheck": nextCheck
        }
    