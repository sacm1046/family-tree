import random
class Family:
    def __init__(self, last_name):
        self._last_name = last_name #Is a parameter of the Family function. _name is for private*
        self._name = ""
        self._age = 0
        self._members = [
            {"id":1,"name":"sebastian","lastname":"Contreras","age":38}
        ]
    def _generateId(self):
        return random.randint(0, 50) #Return a random number
    #Methods
    def add_member(self, member):
        member = {
            "id":self._generateId(),
            "name":member._name,
            "lastname":member._last_name,
            "age":member._age
        }
        self._members.append(member)
        return member
        
    def delete_member(self, id):
        obj = self.get_member(id)
        self._members.remove(obj)

    def update_member(self, id, member):
        obj = self.get_member(id)
        obj.update(member)
        return obj
        
    def get_member(self, id):
        member = list(filter(lambda item: item["id"] == id, self._members))
        return member[0]
    def get_all_members(self):
        return self._members

