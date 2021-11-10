import hashlib
# open address, linear probing


class HashTable():
    def __init__(self):
        self.length = 8
        self.hash_table = [None for i in range(self.length)]

    def get_key(self, data):
        hash_object = hashlib.sha1()  # select sha 1
        hash_object.update(data.encode())
        key = hash_object.hexdigest()
        return int(key, 16)

    def hash_function(self, key):
        return key % self.length

    def Insert(self, data, value):
        key = self.get_key(data)
        address = self.hash_function(key)

        if self.hash_table[address] is None:
            self.hash_table[address] = (key, value)
        else:
            for i in range(self.length):
                ad = self.hash_function(address+i)
                temp = self.hash_table[ad]
                if temp is None or temp == "DeleteMe":
                    self.hash_table[ad] = (key, value)
                    return
                elif temp[0] == key:
                    self.hash_table[ad] = (key, value)
                    return

    def Search(self, data):
        key = self.get_key(data)
        address = self.hash_function(key)

        if self.hash_table[address] is None:
            print("can't find item", data)
            return None
        else:
            for i in range(self.length):
                ad = self.hash_function(address+i)
                temp = self.hash_table[ad]
                if temp is not None and temp[0] == key:
                    return temp[1]
        return None

    def Delete(self, data, value):
        key = self.get_key(data)
        address = self.hash_function(key)

        if self.hash_table[address] is None:
            print('not exist!')
            return
        else:
            for i in range(self.length):
                ad = self.hash_function(address+i)
                temp = self.hash_table[ad]
                if temp == (key, value):
                    self.hash_table[ad] = "DeleteMe"
                    return
        print('not exist!')


ht = HashTable()
print("(s,3) 삽입")
ht.Insert("strawberry", 3)
print("(b,10) 삽입")
ht.Insert("blackberry", 10)
print(ht.hash_table)
print("(a,1) 삽입")
ht.Insert("apple", 1)
print("(m,2) 삽입")
ht.Insert("melon", 2)
print("(s,8) 삽입 -> 교체")
ht.Insert("strawberry", 8)
print("strawberry 교체 확인")
print(ht.Search("strawberry"))
print("blackberry 개수 확인")
print(ht.Search("blackberry"))
print("s, 8 삭제")
ht.Delete("strawberry", 8)
print(ht.hash_table)
print("없는 과일 검색")
print(ht.Search("peach"))
print("없는 과일 검색")
print(ht.Search("strawberry"))
print("(s,7) 삽입")
ht.Insert("strawberry", 7)
print(ht.hash_table)
