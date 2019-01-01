import tarfile
import shutil
try:
    from urllib.request import urlretrieve
except ImportError: # Python 2
    from urllib import urlretrieve

src_url = "https://boost.teeks99.com/lib/1.69.0/boost_1_69_0.tar.bz2"
srcfile, headers = urlretrieve(src_url)
t = tarfile.open(srcfile)
t.extractall()
t.close()

bin_url = "https://boost.teeks99.com/misc/inno_test/boost-bin-msvc14.1-all.tar.xz"
binfile, headers = urlretrieve(bin_url)
t = tarfile.open(binfile)
t.extractall()
t.close()

shutil.copytree("boost_1_69_0", "boost_combined")
shutil.copytree("boost-bin-msvc14.1-all/lib32-msvc-14.1", "boost_combined/lib32-msvc-14.1")
shutil.copytree("boost-bin-msvc14.1-all/lib64-msvc-14.1", "boost_combined/lib64-msvc-14.1")
