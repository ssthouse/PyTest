# coding=utf-8
import pickle

# pickle a dict
# the function dumps accept one argument(the object to pickle)
# the function dump accept two argument(the object to pickle , the file-like-thing to save bytes)
dic = dict(name="Jack", age=21)
pickle_byte = pickle.dumps(dict)

f = open("pickle.text", "wb")
f.write(pickle_byte)
f.close()


# unpickle a dict
restore_dic_file = open("pickle.text", "rb")
restore_dic = pickle.load(restore_dic_file)
restore_dic_file.close()
print(restore_dic)
# print(restore_dic["name"])
# print(restore_dic["age"])

