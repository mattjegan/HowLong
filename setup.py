from setuptools import setup

setup(author='Matthew Egan',
      description='A simple timing utility for long running processes',
      name='howlong',
      py_modules=[
          'HowLong.HowLong',
      ],
      entry_points={
            'console_scripts': [
                  'howlong = HowLong.HowLong:howlong'
            ]
      },
      url='https://github.com/mattjegan/howlong',
      version='0.0.2'
)
