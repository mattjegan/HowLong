from setuptools import setup, find_packages

setup(author='Matthew Egan',
      description='A simple timing utility for long running processes',
      name='howlong',
      py_modules=[
          'HowLong.HowLong',
      ],
      packages=find_packages(),
      entry_points={
            'console_scripts': [
                  'howlong = HowLong.HowLong:howlong'
            ]
      },
      install_requires=[
      'psutil>=5.0.1',
      'termcolor>=1.1.0',
      'colorama>=0.3.9'      
      ],
      url='https://github.com/mattjegan/howlong',
      version='0.0.2'
)
