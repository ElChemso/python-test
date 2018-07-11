from setuptools import setup, find_packages
version = 1.0

setup(name='cyber_python_test',
      version=version,
      description='test',
      license='MIT',
      packages=find_packages(),
      setup_requires=[],
      test_suite='nose.collector',
      tests_require=['coverage',
                     'requests-mock',
                     'mockito',
                     'pyhamcrest'],
      zip_safe=False,
      entry_points={
          'console_scripts': [],
      },)

