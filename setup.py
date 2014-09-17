# -*- coding: utf-8 -*-
__author__ = 'wxie'

from distutils.core import setup
import sys
import py2exe

sys.path.append('C:/Program Files (x86)/Microsoft Visual Studio 9.0/VC/redist/x86/Microsoft.VC90.CRT')


image_format = [('imageformats', [
                    'C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats\qjpeg4.dll',
                    #'C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats\qgif4.dll',
                    #'C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats\qico4.dll',
                    #'C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats\qmng4.dll',
                    #'C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats\qsvg4.dll',
                    #'C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats\qtga4.dll',
                    #'C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats\qtiff4.dll',
                ])]


setup(windows=[{"script": "HtmlToImage.pyw"}],
      options={"py2exe": {"includes": ["sip"]}},
      data_files=image_format)
