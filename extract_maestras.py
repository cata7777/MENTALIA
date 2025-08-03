import os
import json
import re
import zipfile
from pathlib import Path

def detect_maestra_zips(base_path: Path):
    pattern = re.compile(r"(\d+).*maestra", re.IGNORECASE)
    zips = []
    for p in base_path.glob("*.zip"):
        if pattern.search(p.name):
            zips.append(p)
    return zips

def extract_and_merge(zip_path: Path, output_dir: Path):
    with zipfile.ZipFile(zip_path, 'r') as z:
        members = [m for m in z.namelist() if m.endswith('.json')]
        if members:
            output_dir.mkdir(parents=True, exist_ok=True)
            parts = []
            for m in sorted(members):
                with z.open(m) as f:
                    try:
                        data = json.load(f)
                        parts.append(data)
                    except json.JSONDecodeError:
                        continue
            if parts:
                # merge dictionaries - later parts overwrite earlier ones
                merged = {}
                for part in parts:
                    merged.update(part)
                with open(output_dir / 'tesis_maestra.json', 'w') as out:
                    json.dump(merged, out, indent=2)
                return 'json', merged
        # fallback: extract all
        z.extractall(output_dir)
        return 'files', None

def main():
    base = Path('.')
    zips = detect_maestra_zips(base)
    summary = []
    out_root = base / 'extracted_maestras'
    out_root.mkdir(exist_ok=True)
    keep = os.environ.get('KEEP_FILES') == '1'
    for zp in zips:
        match = re.search(r"(\d+)", zp.stem)
        number = match.group(1) if match else 'unknown'
        thesis_dir = out_root / f"tesis_{number}"
        form, data = extract_and_merge(zp, thesis_dir)
        theme = ', '.join(list(data.keys())[:3]) if data else 'N/A'
        summary.append({'number': number, 'form': form, 'theme': theme})
        if not keep:
            # remove extracted files to avoid large repo size
            if thesis_dir.exists():
                for item in thesis_dir.glob('*'):
                    item.unlink()
                thesis_dir.rmdir()
    with open(out_root / 'SUMMARY.json', 'w') as f:
        json.dump(summary, f, indent=2)

if __name__ == '__main__':
    main()
