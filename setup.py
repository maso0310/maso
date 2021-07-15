from setuptools import setup

setup(
    name='maso',
    version='1.0',
    description='Make any image file to ascii art format.',
    url='https://github.com/Henry0526/ascii_image',
    author='Maso',
    author_email='balimon@hotmail.com',
    install_requires=["opencv-python", "numpy"],
    license='MIT',
    packages=['maso'],
    zip_safe=False,
    keywords=['maso'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)