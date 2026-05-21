
class Websites:
    def __init__(self, filename):
        self.fileName = filename
        self.filelist = [] 
        self.reportList = []
        self.index = 0
        self.loadFile(filename)
    
    def loadFile(self, fileName):
        fh = open(fileName, "r")
        dataList = fh.readlines()

        for v in dataList:
            v = "https://" + v.strip()
            data = {"website" : v, "status code" : -1}
            self.filelist.append(data)
            data["index"] = len(self.filelist) - 1

            #print(data)



        

    def getNextWebsiteToCheck(self):
        if self.index >= len(self.filelist):
            return None
        data = self.filelist[self.index]
        self.index += 1
        return data

    def putWebsiteData(self,data):
        if "index" in data and "website" in data and "statusCode" in data:
            self.reportList.append(data)
        else:
            print("Bad keys in report: " + str(data))

    def saveReport(self):
        fh = open("report.txt", "w")

        for el in self.reportList:
            fh.write(str(el["website"]) + " - " + str(el) )