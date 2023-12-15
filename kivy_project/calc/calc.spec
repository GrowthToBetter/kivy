# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew
from PyInstaller.utils.hooks import collect_data_files

a = Analysis(['calc.py'],
             pathex=[('D:\\study-coding\\kivy+git\\kivy\\kivy_project\\calc\\')],
             binaries=[],
             datas=collect_data_files('kivy'),
             hiddenimports=[
                 'kivy.core.text._text_sdl2',
                 'kivy.core.image.img_sdl2',
                 'kivy.core.audio.audio_sdl2',
                
             ],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             noarchive=False)

pyz = PYZ(a.pure)

a.datas += [('calc\\calc.kv','D:\\study-coding\\kivy+git\\kivy\\kivy_project\\calc\ ','DATA')]
a.datas += [('calc\\bg.jpg','D:\\study-coding\\kivy+git\\kivy\\kivy_project\\calc\ ','DATA')]

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.datas,
          [],
          **{
              'name': 'calc',
              'debug': True,
              'bootloader_ignore_signals': True,
              'strip': False,
              'upx': True,
              'upx_exclude': [],
              'console': True
          })

coll = COLLECT(exe,
               Tree('D:\\study-coding\\kivy+git\\kivy\\kivy_project\\calc\\'),
               a.binaries,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=True,
               upx=True,
               upx_exclude=[],
               name='calc')
