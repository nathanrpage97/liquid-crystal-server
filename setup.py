from setuptools import setup, find_packages


setup(name='liquid_crystal_server', version='0.0.3', author="Nathan Page", author_email='nathanrpage97@gmail.com',
      description='Pure python REST server to control an I2C LCD', license='MIT',
      url='https://github.com/nathanrpage97/liquid-crystal', keywords='LCD display I2C server',
      packages=find_packages(),
      install_requires=['aiohttp', 'dataclasses-json', 'aiohttp-cors', 'aiojobs',
                        'liquid-crystal @ https://github.com/nathanrpage97/liquid-crystal/archive/v0.1.0.zip'],)
