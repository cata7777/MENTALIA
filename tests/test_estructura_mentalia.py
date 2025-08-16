from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import os
from scripts.estructura_mentalia import clasificar, recorrer


def test_clasificar_mapeo():
    assert clasificar('multiverso') == '🌌 multiverso'
    assert clasificar('MENTALIZACION total') == '🧠 MENTALIZACION total'
    assert clasificar('Agentes especiales') == '💫 Agentes especiales'
    assert clasificar('sistemas operativos') == '🪐 sistemas operativos'
    assert clasificar('rri documentacion') == '🛡️ rri documentacion'


def test_clasificar_default():
    assert clasificar('otros') == '📁 otros'


def test_recorrer(tmp_path):
    sub = tmp_path / 'multiverso'
    sub.mkdir()
    (tmp_path / 'archivo.txt').write_text('hola')

    estructura = recorrer(tmp_path)

    root_entry = next(e for e in estructura if e['ruta'] == '.')
    assert '🌌 multiverso' in root_entry['carpetas']
    assert 'archivo.txt' in root_entry['archivos']

    sub_entry = next(e for e in estructura if e['ruta'] == 'multiverso')
    assert sub_entry['carpetas'] == []
    assert sub_entry['archivos'] == []
