# Defines functions and classes related to application objects

from enum import Enum
import datetime

class Status(Enum):
    UNSUBMITTED = "unsubmitted"
    SUBMITTED = "submitted"
    INTERVIEWED = "interviewed"
    OFFERED = "offered"
    ACCEPTED = "accepted"

class Fields(Enum):
    TITLE = "title"
    STATUS = "status"
    DEADLINE = "deadline"
    COMPANY = "company"
    TAGS = "tags"
    PAY = "pay"
    DATE = "date"

class Application:
    """
    Represents a single internship application.
    status (Status)
    title (String)
    deadline (date)
    company (String)
    tags (String array)
    pay (int)
    daterange (date array [startdate, enddate])
    """

    def __init__(self):
        self.status = Status.UNSUBMITTED
        self.title = "Awesome internship"
        self.deadline = None
        self.company = "PlaceCo"
        self.tags = []
        self.pay = 0
        self.daterange = []
    
    def __str__(self):
        out = ""
        out += "Title: " + self.title + "\n"
        out += "Company: " + self.company + "\n"
        out += "Status: " + str(self.status) + "\n"
        out += "Deadline: " + str(self.deadline) + "\n"
        out += "Tags: " + str(self.tags) + "\n"
        out += "Pay: " + str(self.pay) + "\n"
        out += "Date range: " + str(self.daterange) + "\n"
        return out
        

""" Takes an application list, a search query, and a field to
    search for (from the Fields enum) and outputs all
    items that match the search query.
"""
def filterlist(applist, search, field):
    out = []
    for app in applist:
        if field == Fields.TITLE:
            if search.lower() in app.title.lower(): out.append(app)
        elif field == Fields.STATUS:
            if search is app.status: out.append(app)
        elif field == Fields.COMPANY:
            if search.lower() in app.company.lower(): out.append(app)
        elif field == Fields.TAGS:
            if search.lower() in [x.lower() for x in app.tags]: out.append(app)
    return out
