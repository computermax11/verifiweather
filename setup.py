from setuptools import setup, find_packages

setup(name='verifiweather',
      version='0.1.3',
      description='Verifi Job Application Weather App',
      url='http://github.com/computermax11/verifiweather.git',
      author='Max Schulberg',
      author_email='computermax11@gmail.com',
      install_requires=['requests', 'ipaddr'],
      packages=find_packages(),
      entry_points = {
          'console_scripts': ['verifiweather = verifiweather.__main__:main'],
      },
      zip_safe=False)
