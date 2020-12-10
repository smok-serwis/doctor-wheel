from setuptools import setup, find_packages

from doctor_wheel import __version__

setup(keywords=['wheel', 'strip', 'size', 'reduction'],
      packages=find_packages(include=['doctor_wheel']),
      version=__version__,
      install_requires=['satella'],
      python_requires='!=2.7.*,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
      entry_points={
            "console_scripts": [
                  "doctor-wheel = doctor_wheel.run:run",
            ]
      }
      )
