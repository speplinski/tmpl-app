from setuptools import setup, find_packages

setup(
    name="tmpl_app",
    version="1.0.0",
    packages=find_packages(),
    py_modules=['main'],
    install_requires=[
        'av>=10.0.0',
        'numpy>=1.24.0',
        'Pillow>=10.0.0',
        'pysdl2>=0.9.16',
        'pysdl2-dll>=2.28.0'
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'tmpl-app=main:main',
        ],
    }
)