
'''
**Movie Store** - Manage video rentals and controls when videos are
checked out, due to return, overdue fees and for added complexity
create a summary of those accounts which are overdue for contact.
'''

from datetime import date

class Video:
    def __init__(self, out, back, fee):
        self.outDate = out
        self.backDate = back
        self.feePerDay = fee

    def getFeeDue(self, day):
        #number of days overdue times feePerDay
        if day > self.backDate:
            n = day - self.backDate
            return n.days * self.feePerDay
        return 0.00

class VideoStore:

    def __init__(self):
        self.videosOut = []

    def addVideoOut(self, video):
        self.videosOut.append(video)

    def getOverdueSummary(self, day):
        result = []
        for v in self.videosOut:
            fee = v.getFeeDue(day)
            if fee > 0.00:
                result.append(fee)
        return result

def main():
    print "Running"
    today = date(2010, 10, 10)
    v1 = Video( date(2010, 1, 12), date(2010, 10, 10), 1.00 )
    v2 = Video( date(2010, 1, 12), date(2010, 10, 20), 1.00 )
    v3 = Video( date(2010, 1, 12), date(2010, 8, 20), 1.00 )
    vs = VideoStore()
    vs.addVideoOut(v1)
    vs.addVideoOut(v2)
    vs.addVideoOut(v3)
    print "Fee per video is -- " + str(vs.getOverdueSummary(today))
    print "Closing"


if __name__ == "__main__":
    main()
