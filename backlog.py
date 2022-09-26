import pprint

from model import *

class Backlog:
    users = {}
    statuses = {}

    def __init__(self):
        self.users = User()
        self.statuses = Status()

    def updateStatus(self, issueNumber, asigneeName, statusName, comment):

        user = self.getValue(self.users.findByName(asigneeName))
        pprint.pprint(user)

        status = self.getValue(self.statuses.findByName(statusName))
        pprint.pprint(status)

        issue = Issue(issueNumber)
        data = {'statusId': status['id'],
                'assigneeId': user['id'], 'comment': comment}
        pprint.pprint(issue.update(data))

    def getValue(self, array):
        if len(array) > 0:
            return array[0]
        else:
            return None
