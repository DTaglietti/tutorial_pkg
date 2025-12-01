from setuptools import setup

package_name = 'tutorial_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='danibuntu',
    maintainer_email='taglietti.daniele3@gmail.com',
    description='Tutorial ROS 2 package',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'minimal_publisher = tutorial_pkg.minimal_publisher:main',
            'minimal_subscriber = tutorial_pkg.minimal_subscriber:main',
        ],
    },
)
