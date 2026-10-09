from setuptools import setup
from glob import glob
from pathlib import Path
import os

package_name = 'stararm102_description'
package_dir = Path(__file__).resolve().parent
resource_dir = package_dir

def model_files(folder):
    files = sorted((resource_dir / folder).glob('*'))
    if not files:
        raise RuntimeError('Missing URDF or mesh resources in stararm102_description.')
    return [os.path.relpath(path, package_dir) for path in files if path.is_file() and path.suffix != '.md']


setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name+'/launch/', glob('launch/*.py')),
        ('share/' + package_name+'/urdf/', model_files('urdf')),
        ('share/' + package_name+'/rviz/', glob('rviz/*')),
        ('share/' + package_name+'/meshes', model_files('meshes')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nyancos',
    maintainer_email='12461360+nyancos@user.noreply.gitee.com',
    description='URDF Description package for StarArm 102 robot',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
