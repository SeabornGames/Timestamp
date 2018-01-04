from setuptools import setup

setup(
    name='seaborn-timestamp',
    version='1.0.0',
    description='SeabornTimingProfile collects, records, and reports timing'
                'data on code implementing a number of different execution'
                'strategies"',
    long_description='',
    author='Ben Christenson',
    author_email='Python@BenChristenson.com',
    url='https://github.com/SeabornGames/Timestamp',
    install_requires=[
        'psycopg2',
    ],
    extras_require={
    },
    packages=['seaborn.time_profile',
                'seaborn.timestamp'],
    license='MIT License',
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5'),
    entry_points='''
        [console_scripts]
        timestamp = seaborn.timestamp
        time_profile = seaborn.time_profile
    ''',
)
