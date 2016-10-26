# coding=utf-8
import os

# 1.check local path
local_path = os.path.abspath(".")
print(local_path)
print()

# 2.splice path
splice_path = os.path.join(local_path, "test.txt")
print(splice_path)
print()

# 3.create a dir
new_dir = os.path.join(local_path, "test_dir")
# os.mkdir(new_dir)
# os.rmdir(new_dir)

# 4. split path
dir_tuple = os.path.split(local_path)
print(dir_tuple[0], "   ", dir_tuple[1])
print()

# 5.get file suffix
file_tuple = os.path.splitext(splice_path)
print(file_tuple[0], "   ", file_tuple[1])

# 6.rename file
# os.rename("test.txt", "rename.txt")

# 7.delete file
#os.remove("rename.txt")

# 8.list all files in current dir
all_files = [x for x in os.listdir(".") if os.path.isfile(x)]
print(all_files)
