import pprint

from model import *

class Backlog:

    def updateStatus(self, issueNumber, asigneeName, statusName, comment):

        users = User()
        user = self.getValue(users.findByName(asigneeName))
        pprint.pprint(user)

        statuses = Status()
        status = self.getValue(statuses.findByName(statusName))
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
