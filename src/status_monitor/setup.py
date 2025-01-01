from setuptools import setup

package_name = 'status_monitor'

setup(
    name=package_name,
    version='0.0.0',
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='fatiznd',
    maintainer_email='janamajda15@gmail.com',
    description='Package for monitoring the robot status',
    license='apache license 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'status_publisher = status_monitor.status_publisher:main',
            'error_handler = status_monitor.error_handler:main',
        ],
    },
)
