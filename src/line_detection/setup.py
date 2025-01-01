from setuptools import setup

package_name = 'line_detection'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='fatiznd',
    maintainer_email='janamajda15@gmail.com',
    description=' Package for line detection',
    license='Tapache license 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'camera_reader = line_detection.camera_reader:main',
            'line_analyser = line_detection.line_analyser:main',
        ],
    },
)
