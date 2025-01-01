from setuptools import setup

package_name = 'motion_control'

setup(
    name=package_name,
    version='0.0.0',
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='fatiznd',
    maintainer_email='janamajda15@gmail.com',
    description='package for motion control of the robot',
    license='Apache license 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'motion_controller = motion_control.motion_controller:main',
        'line_recovery =motion_control.line_recovery:main',
        ],
    },
)
