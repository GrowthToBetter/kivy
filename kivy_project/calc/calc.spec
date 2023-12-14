# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew
from PyInstaller.utils.hooks import collect_data_files

a = Analysis(['calc.py', 'calc.kv', 'bg.jpg'],
             pathex=['D:\\study-coding\\kivy+git\\kivy\\kivy_project\\calc'],
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

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.datas,
          [],
          **{
              'name': 'calc',
              'debug': False,
              'bootloader_ignore_signals': False,
              'strip': False,
              'upx': True,
              'upx_exclude': [],
              'console': False
          })

coll = COLLECT(exe,
               Tree('D:\\study-coding\\kivy+git\\kivy\\kivy_project\\calc\\'),
               a.binaries,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='calc')
