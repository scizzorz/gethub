from setuptools import setup

setup(
	name='gethub',
	version='0.1.0',
	install_requires=[
		'githubpy',
		],
	description='Clone all of your GitHub repositories',
	long_description=open('README.rst').read(),
	url='http://github.com/scizzorz/gethub',
	license='MIT',
	author='John Weachock',
	author_email='jweachock@gmail.com',
	py_modules=['gethub'],
	include_package_data=True,
	scripts=['bin/gethub'],
)
