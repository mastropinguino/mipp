from setuptools import setup, Extension

ext = Extension('mipp/xrit/_convert', ['mipp/xrit/convert/wrap_convert.c',
                                       'mipp/xrit/convert/10216.c'],
                extra_compile_args = ['-std=c99', '-O9'])


setup(name = 'mipp',
      version = '0.5',
      package_dir = {'mipp':'mipp', 
                     'mipp/xrit': 'mipp/xrit'},
      packages = ['mipp', 'mipp/xrit'],
      ext_modules = [ext,],
      zip_safe = False,
      )
