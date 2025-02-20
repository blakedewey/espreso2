from setuptools import setup

version = '0.3.1'

with open('README.md') as readme:
    long_desc = readme.read()

setup(name='espreso2',
      description='An algorithm to estimate an MR slice profiles by learning '
                  'to match internal patch distributions',
      author='Shuo Han',
      author_email='shan50@jhu.edu',
      version=version,
      packages=['espreso2'],
      license='GPLv3',
      python_requires='>=3.7.10',
      scripts=['scripts/train.py', 'scripts/calc_fwhm.py'],
      long_description=long_desc,
      install_requires=[
          'torch>=1.8.1',
          'numpy',
          'scipy',
          'nibabel',
          'matplotlib',
          'ptxl@git+https://gitlab.com/shan-deep-networks/ptxl.git@0.3.1',
          'sssrlib@git+https://github.com/shuohan/sssrlib@0.3.0'
      ],
      long_description_content_type='text/markdown',
      url='https://github.com/shuohan/espreso2.git',
      classifiers=[
          'Programming Language :: Python :: 3',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Operating System :: OS Independent'
      ]
     )
