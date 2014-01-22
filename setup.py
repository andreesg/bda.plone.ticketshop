import os
from setuptools import (
    setup,
    find_packages,
)


version = '1.0dev'
shortdesc = "Sell tickets for events"
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'CHANGES.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'LICENSE.rst')).read()


setup(
    name='bda.plone.ticketshop',
    version=version,
    description=shortdesc,
    long_description=longdesc,
    classifiers=[
        'Environment :: Web Environment',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    author='BlueDynamics Alliance',
    author_email='dev@bluedynamics.com',
    license='GNU General Public Licence',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['bda', 'bda.plone'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Plone',
        'plone.app.event[archetypes,ploneintegration]',
        'collective.folderishtypes',
        'bda.plone.shop',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.app.contenttypes',
            'Products.ATContentTypes',
            'bda.plone.ticketshop',
          ]
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
