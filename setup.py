# TO DO:
#   * Upload to GitHub and put down the url 
#   * Check Licenses

from setuptools import setup

setup(
    name='SOcial ANalysis',
    url='',
    author='Maarten Grootendorst',
    author_email='maartengrootendorst@gmail.com',
    packages=['soan'],
    description='Used to analyze whatsapp data',
    long_description=open('README.txt').read(),
    install_requires=['numpy', 'pillow', 'scipy', 'sklearn', 'regex', 'emoji', 'seaborn',
                     'datetime', 'pandas', 'operator', 'requests',
                      'wordcloud', 'palettable'],
    license='MIT',
)
