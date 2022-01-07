# Remove key values pairs from a list of dictionaries

class RemoveKeyValue:

    def __init__(self):
        self.dict_list = [{'1': 'a'}, {'Apple': '200.40'}, {'Shital': '101'}]
        print(self.dict_list)

    def removePair(self):
        flag = 0
        key = input("Enter key: ")
        for element in self.dict_list:
            if key in element.keys():
                self.dict_list.remove(element)
        print(self.dict_list)

remove = RemoveKeyValue()
remove.removePair()

