from setuptools import setup, find_packages

setup(name='verifiweather',
      version='0.1',
      description='Verifi Job Application Weather App',
      url='http://github.com/computermax11/verifiweather.git',
      author='Max Schulberg',
      author_email='computermax11@gmail.com',
      install_requires=['requests'],
      packages=find_packages(),
      scripts=['verifiweather/verifiweather.py'],
      entry_points = {
          'console_scripts': ['veriweather=verifiweather.command_line:main'],
      },
      zip_safe=False)
