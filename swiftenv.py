import os
if os.getenv('OUTLANG') == 'swift':
    genlang = 'swift4'
elif os.getenv('OUTLANG') == 'dart':
    genlang = 'dart-jaguar'
else:
    genlang = os.getenv('OUTLANG')

open('genlang', 'w').write(genlang)
