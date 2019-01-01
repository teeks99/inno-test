import tarfile
import shutil
try:
    from urllib.request import urlretrieve
except ImportError: # Python 2
    from urllib import urlretrieve

print("Getting Source")
src_url = "https://boost.teeks99.com/lib/1.69.0/boost_1_69_0.tar.bz2"
src_file = "boost_1_69_0.tar.bz2"
urlretrieve(src_url, src_file)
t = tarfile.open(src_file)
t.extractall()
t.close()

print("Getting Binaries")
bin_url = "https://boost.teeks99.com/misc/inno_test/boost-bin-msvc14.1-all.tar.xz"
bin_file = "boost-bin-msvc14.1-all.tar.xz"
urlretrieve(bin_url, bin_file)
t = tarfile.open(bin_file)
t.extractall()
t.close()

print("Making combined")
shutil.copytree("boost_1_69_0", "boost_combined")
shutil.copytree("boost-bin-msvc14.1-all/lib32-msvc-14.1", "boost_combined/lib32-msvc-14.1")
shutil.copytree("boost-bin-msvc14.1-all/lib64-msvc-14.1", "boost_combined/lib64-msvc-14.1")
