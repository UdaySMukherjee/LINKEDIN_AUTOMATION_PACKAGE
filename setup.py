from setuptools import setup

setup(
    name='linkedin_automation_package',
    version='1.0',
    install_requires=[
        'selenium',
        'pyautogui',
    ],
    author='Uday Sankar Mukherjee',
    author_email='udaysankar2003@gmail.com',
    description='LinkedIn automation script',
    py_modules=['linkedin_automation'],
)