from setuptools import setup

setup(name='gh-auth-gradient',
      version='0.0.1',
      description='Gradient Health Auth',
      url='http://github.com/gradienthealth/gh-auth',
      author='Joshua Miller',
      author_email='josh@gradienthealth.io',
      license='MIT',
      packages=['gh_auth'],
      zip_safe=False,
      install_requires=['requests']
)
