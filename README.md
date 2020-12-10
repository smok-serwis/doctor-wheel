doctor_wheel
============

[![PyPI](https://img.shields.io/pypi/pyversions/doctor-wheel.svg)](https://pypi.python.org/pypi/doctor-wheel)
[![PyPI version](https://badge.fury.io/py/doctor-wheel.svg)](https://badge.fury.io/py/doctor-wheel)
[![PyPI](https://img.shields.io/pypi/implementation/doctor-wheel.svg)](https://pypi.python.org/pypi/doctor-wheel)
[![Maintainability](https://api.codeclimate.com/v1/badges/657b03d115f6e001633c/maintainability)](https://codeclimate.com/github/smok-serwis/doctor-wheel/maintainability)
[![Build status](https://circleci.com/gh/smok-serwis/doctor-wheel.svg?style=shield)](https://app.circleci.com/pipelines/github/smok-serwis/doctor-wheel)

`doctor-wheel` is an utility to reduce the size of your binary wheels
by stripping their .so extensions.

It requires GNU strip to be available.

It will alter your file in-place.

Usage:

```
doctor-wheel name-of-your-wheel-file.whl name-of-second-wheel-file.whl ...
```
