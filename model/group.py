
class Group:

    def __init__(self, groupname=None, header=None, footer=None, id=None):
        self.groupname = groupname
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.groupname)

    def __eq__(self, other):
        return self.id == other.id and self.groupname == other.groupname

