from setuptools import setup, find_packages

setup(name='verifiweather',
      version='0.1.4',
      description='Verifi Job Application Weather App',
      url='http://github.com/computermax11/verifiweather.git',
      author='Max Schulberg',
      author_email='computermax11@gmail.com',
      install_requires=[
          'requests',
          'ipaddress',
          'easygui'   # 'easygui;platform_system=="Windows"'
      ],  
      packages=find_packages(),
      entry_points = {
          'console_scripts': ['verifiweather = verifiweather.__main__:main'],
          'gui_scripts': ['vwgui = verifiweather.__gui__:start_func']  
      },
      zip_safe=False)
