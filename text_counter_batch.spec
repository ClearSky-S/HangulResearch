# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_all

# 패키지 데이터 수집
datas = []
binaries = []
hiddenimports = []

# wordcloud 패키지 수집
tmp_ret = collect_all('wordcloud')
datas += tmp_ret[0]
binaries += tmp_ret[1]
hiddenimports += tmp_ret[2]

# matplotlib 패키지 수집
tmp_ret = collect_all('matplotlib')
datas += tmp_ret[0]
binaries += tmp_ret[1]

a = Analysis(
    ['text_counter_batch.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,  # collect_all()이 이미 모든 의존성을 수집함
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='text_counter_batch',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
