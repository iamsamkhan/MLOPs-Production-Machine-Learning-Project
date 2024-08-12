from setuptools import setup, find_packages

setup(
    name="us_visa",
    version="0.0.0",
    author="shamshad ahmed",
    author_email="smshad0001@.com",
    url='https://github.com/iamsamkhan/MLOPs-Production-Machine-Learning-Project.git',
    python_requires='>=3.12',
    install_requires=_get_requirements('requirements.txt'),
    include_package_data=True,
    packages=find_packages()
)