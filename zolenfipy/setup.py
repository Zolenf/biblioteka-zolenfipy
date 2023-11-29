from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='zolenfipy',
  version='1.0.0',
  description='the simple python basing programing language',
  long_description=open('README.rst').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Zolenf',
  author_email='olaf.zylowski@onet.pl',
  license='MIT', 
  classifiers=classifiers,
  keywords='language',
  packages=find_packages(),
  install_requires=['tkinter'] 
)
