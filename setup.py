from distutils.core import setup

setup(
    name='Specto',
    packages=['Specto'],
    version='0.1',
    license='MIT',
    description='Converts WAV files to spectograms (.png) and the other way. Inspired by the ARSS',
    author='Subhash Saravanan',
    author_email='subhashve4@gmail.com',
    url='https://github.com/pi3123/Specto',
    download_url='https://github.com/pi3123/Specto/archive/refs/tags/0.1.tar.gz',  # I explain this later on
    keywords=['Audio Analysis', 'Spectograms', 'Audio', 'WAVs', 'Sounds'],  # Keywords that define your package best
    install_requires=[  # I get to this in a second
        'Pillow',
        'numba',
        'numpy'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
