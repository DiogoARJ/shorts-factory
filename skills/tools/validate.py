"""Check a skill zip against claude.ai upload limits seen in the UI.

Usage: python3 -I validate.py <zip>
Limits: <=200 files, <=30 MB uncompressed (checked against 30*10^6 to be safe),
<skill>/SKILL.md at top level with YAML name + description (name == folder, desc <= 1024).
"""
import re, sys, zipfile

z = zipfile.ZipFile(sys.argv[1])
infos = z.infolist()
files = [i for i in infos if not i.is_dir()]
dirs = [i for i in infos if i.is_dir()]
size = sum(i.file_size for i in files)
tops = {i.filename.split('/')[0] for i in infos}
ok = True

def check(cond, msg):
    global ok
    print(('OK   ' if cond else 'FAIL ') + msg)
    ok &= cond

check(len(infos) <= 200, f'entries {len(infos)} (files {len(files)}, dirs {len(dirs)}) <= 200')
check(size <= 30_000_000, f'uncompressed {size/1e6:.2f} MB <= 30 MB')
check(len(tops) == 1, f'single top-level folder: {sorted(tops)}')
top = sorted(tops)[0]
try:
    sk = z.read(f'{top}/SKILL.md').decode()
    m = re.match(r'^---\n(.*?)\n---\n', sk, re.S)
    check(bool(m), 'SKILL.md has YAML frontmatter')
    fm = m.group(1) if m else ''
    name = re.search(r'^name:\s*"?([^"\n]+)"?', fm, re.M)
    desc = re.search(r'^description:\s*"?(.*?)"?\s*$', fm, re.M)
    check(bool(name) and name.group(1) == top, f'name matches folder ({name.group(1) if name else None})')
    check(bool(desc) and 0 < len(desc.group(1)) <= 1024, f'description length {len(desc.group(1)) if desc else 0} <= 1024')
    check(len(sk.splitlines()) <= 500, f'SKILL.md lines {len(sk.splitlines())} <= 500')
except KeyError:
    check(False, f'{top}/SKILL.md present')
nested = [i.filename for i in files if i.filename.endswith('/SKILL.md') and i.filename != f'{top}/SKILL.md']
check(not nested, f'no nested SKILL.md ({len(nested)})')
big = sorted(files, key=lambda i: -i.file_size)[:5]
print('largest:', ', '.join(f'{i.filename.split("/")[-1]} {i.file_size/1e6:.2f}MB' for i in big))
sys.exit(0 if ok else 1)
