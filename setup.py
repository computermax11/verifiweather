from setuptools import setup, find_packages

setup(name='verifiweather',
      version='0.2',
      description='Verifi Job Applicant Weather Script',
      url='http://github.com/computermax11/verifiweather.git',
      author='Max Schulberg',
      author_email='computermax11@gmail.com',
      packages=find_packages(),
      install_requires=['requests'],
      scripts=['verifiweather/verifiweather.py'],
      zip_safe=False)
