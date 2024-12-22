class HistoryDict:
    def __init__(self, some_dict):
        self.some_dict = some_dict
        self.changed_dict = {}
        self.l = []
    
    def set_value(self, key, value):
        self.changed_dict.update(self.some_dict)
        self.changed_dict[key] = value
        
        if key not in self.l:
            self.l.append(key)

        # каждый раз удаляет самый старй
        if len(self.l) > 5:
            self.l.pop(0)

        
        

    def get_history(self):
        
        return self.l


        
# Example usage:
d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
print(d.get_history())  # ["bar"]

d.set_value("foo", 44)
print(d.get_history())  # ["bar", "foo"]

d.set_value("baz", 45)
d.set_value("qux", 46)
d.set_value("qux", 46)
d.set_value("dde", 46)
d.set_value("wd", 46)
d.set_value("quux", 47)
d.set_value("corge", 48)  # This exceeds the limit of 5
print(d.get_history())  # ["foo", "baz", "qux", "quux", "corge"]

d.set_value("bar", 49)
print(d.get_history())  # ["baz", "qux", "quux", "corge", "bar"]