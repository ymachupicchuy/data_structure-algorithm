class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user is None or group is None:
        return None
    queue = [group]
    while len(queue):
        node = queue.pop(0)
        if user in node.users:
            return True
        if node.groups:
            queue.append(node.groups[0])
    return False


'''
TEST
'''
def test1(user, parent):
    return is_user_in_group(user, parent) == True
print(test1('sub_child_user', parent))
# True

def test2(user, parent):
    return is_user_in_group(user, parent) == True
print(test2(None, None))
# False

def test2(user, parent):
    return is_user_in_group(user, parent) == True
print(test2('sub_child_user', None))
# False