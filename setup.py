from distutils.core import setup
setup(
  name = 'commanderline',
  packages = ['commanderline'], 
  version = '0.1.1',
  install_requires=[
        "sys",
        "getopt",
        "inspect"
    ],
  description = 'Easily expose any function to the command line',
  author = 'Tomaz Berisa',
  author_email = 'tomaz.berisa@gmail.com',
  url = 'https://bitbucket.org/tomazberisa/commanderline', 
  download_url = 'https://bitbucket.org/tomazberisa/commanderline/get/0.1.1.tar.gz', 
  keywords = ['command-line'], 
  classifiers = [],
)
