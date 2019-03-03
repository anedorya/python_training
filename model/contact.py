from sys import maxsize

class Info:

    def __init__(self, firstname=None, middlename=None, lastname=None, nick=None, title=None, cname=None, address=None, homedid=None, cellular=None, workdid=None, fax=None, email=None, email2=None, email3=None, website=None, address2=None, home=None, notes=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nick = nick
        self.title = title
        self.cname = cname
        self.address = address
        self.homedid = homedid
        self.cellular = cellular
        self.workdid = workdid
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.website = website
        self.address2 = address2
        self.home = home
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

