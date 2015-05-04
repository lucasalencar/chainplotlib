try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Wrapper for Matplotlib with chainable methods.',
    'author': 'Lucas Andr\'e de Alencar',
    'url': 'https://github.com/lucasandre/chainplotlib',
    'author_email': 'alencar.lucas.a@gmail.com',
    'version': '0.0.0',
    'install_requires': ['nose', 'matplotlib', 'numpy'],
    'packages': ['chainplotlib'],
    'scripts': [],
    'name': 'chainplotlib'
}

setup(**config)
