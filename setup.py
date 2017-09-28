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
      'argparse',
      'logging',
      'sys',
      'datetime',
      'subprocess',
      'time',
      'psutil'      
      ],
      url='https://github.com/mattjegan/howlong',
      version='0.0.2'
)
