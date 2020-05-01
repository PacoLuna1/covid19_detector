import requests as request, json

class APICOVID():
    def __init__(self):
        self.name ='APICOVID'

    def getStats(self):
        stats = request.get('https://api.covid19api.com/stats')
        if (stats.status_code == 200):
            statsDc = stats.json()
            return stats
        else:
            return None

    def getGlobalStats(self):
        summary = request.get('https://api.covid19api.com/summary')
        if (summary.status_code == 200):
            summaryGlobal = summary.json()
            totalDeaths = summaryGlobal['Global']['TotalDeaths']
            totalRecovered = summaryGlobal['Global']['TotalRecovered']
            totalCases = totalDeaths + totalRecovered
            return {
                    'TotalCases': totalCases,
                    'GlobalDeaths': totalDeaths,
                    'GlobalRecovered': totalRecovered,
                    'Summary': summaryGlobal
                   }
        else:
            return None

    def getIndexOfCountry(self,summaryGlobal, countryTarget):
        i = 0
        for x in summaryGlobal:
            i = 0
            for country in summaryGlobal['Countries']:
                if(summaryGlobal['Countries'][i].get('Country', '') == countryTarget):
                    return i
                else:
                    i = i +1

        return None

    def getStatsOfCountry(self,stats, index):
        return stats['Summary']['Countries'][index]

    def printStats(self, statsCountry):
        print('----------------------------')
        for property in statsCountry:
            print(property +": " + str(statsCountry[property]))
        print('----------------------------')

    def getInfo(self, country):
        stats = self.getStats()
        globalStats = self.getGlobalStats()
        indexCountry = self.getIndexOfCountry(globalStats['Summary'], country)
        statsCountry = self.getStatsOfCountry(globalStats, indexCountry)
        self.printStats(statsCountry)
