"""Flatten the Marketeer bundle so it fits claude.ai skill upload limits.

Usage: python3 -I build.py <src_marketeer_dir> <out_marketeer_dir>
Each tool folder becomes one Markdown file (guide + references + text assets as code blocks).
Folders listed in KEEP_TREE keep their data/scripts as real files (only their .md are merged).
"""
import os, re, sys, shutil

SRC, OUT = sys.argv[1], sys.argv[2]
TEXT_EXT = {'md', 'js', 'mjs', 'cjs', 'json', 'csv', 'html', 'css', 'py', 'txt', 'svg', 'sh', 'ts'}
BIN_EXT = {'png', 'jpg', 'jpeg', 'webp', 'gif', 'ttf', 'otf', 'woff', 'woff2', 'coverage'}
KEEP_TREE = {'design/ui-ux-pro-max'}          # runnable search engine: keep data/ + scripts/
SLIM = {'design/taste-skill': {'assets/system.css', 'assets/system.js', 'assets/starter.html'}}
LANG = {'js': 'js', 'mjs': 'js', 'cjs': 'js', 'json': 'json', 'csv': 'csv', 'html': 'html',
        'css': 'css', 'py': 'python', 'sh': 'bash', 'ts': 'ts', 'svg': 'xml', 'txt': 'text'}
UPSTREAM = {'marketing': 'https://github.com/coreyhaines31/marketingskills/tree/96798cf/skills/',
            'redes': 'https://github.com/charlie947/social-media-skills/tree/10ca79c/skills/',
            'financas': 'https://github.com/anthropics/knowledge-work-plugins/tree/ab4cb1c/finance/skills/',
            'juridico': 'https://github.com/anthropics/knowledge-work-plugins/tree/ab4cb1c/legal/skills/',
            'design/taste-skill': 'https://github.com/Leonxlnx/taste-skill/tree/9b4bf93/skills/taste-skill',
            'design/frontend-design': 'https://github.com/anthropics/skills/tree/ca45fc4/skills/frontend-design',
            'design': 'https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/b7d5353/.claude/skills/'}


def frontmatter_to_text(t):
    m = re.match(r'^---\n(.*?)\n---\n', t, re.S)
    if not m:
        return t
    fm = m.group(1)
    d = re.search(r'^description:\s*(.*?)(?=^\S[\w-]*:|\Z)', fm, re.M | re.S)
    desc = ' '.join(d.group(1).replace('>-', '').replace('>', '').split()).strip('"\'') if d else ''
    return (f'*Quando usar:* {desc}\n\n' if desc else '') + t[m.end():]


def fence(text):
    n = max([3] + [len(x) for x in re.findall(r'`{3,}', text)]) + 1
    return '`' * n


def upstream(key, name):
    if key in UPSTREAM:
        return UPSTREAM[key] + ('' if key.startswith('design/') else name)
    top = key.split('/')[0]
    return UPSTREAM.get(top, '') + name


def merge_tool(folder, rel_key, name, keep_tree=False, slim=None):
    guide = os.path.join(folder, 'GUIA.md')
    parts = [f'# {name}\n', f'Original: {upstream(rel_key, name)}\n',
             'Referências citadas como `references/x.md`, `assets/...` ou `scripts/...` estão mais abaixo neste '
             'ficheiro, numa secção com esse caminho. Para correr um script, copiar o bloco de código para um '
             'ficheiro com esse nome.\n']
    if os.path.exists(guide):
        parts.append(frontmatter_to_text(open(guide, encoding='utf-8').read()))
    skipped = []
    for root, dirs, files in os.walk(folder):
        dirs.sort()
        for f in sorted(files):
            p = os.path.join(root, f)
            rel = os.path.relpath(p, folder)
            if rel == 'GUIA.md':
                continue
            ext = f.rsplit('.', 1)[-1].lower() if '.' in f else ''
            if keep_tree and not rel.endswith('.md'):
                continue  # copied as real file
            if slim is not None and not rel.endswith('.md') and rel not in slim:
                skipped.append(rel)
                continue
            if ext in BIN_EXT or ext not in TEXT_EXT:
                skipped.append(rel)
                continue
            body = open(p, encoding='utf-8', errors='replace').read()
            if ext == 'md':
                parts.append(f'\n\n---\n\n## `{rel}`\n\n' + frontmatter_to_text(body))
            else:
                fz = fence(body)
                parts.append(f'\n\n---\n\n## `{rel}`\n\n{fz}{LANG.get(ext, "")}\n{body.rstrip()}\n{fz}\n')
    if skipped:
        parts.insert(3, f'Ficheiros não incluídos (binários, imagens ou demos; ver o original no link acima): '
                        f'{len(skipped)}.\n')
    return '\n'.join(parts)


os.makedirs(OUT)
for f in ('SKILL.md',):
    shutil.copy(os.path.join(SRC, f), os.path.join(OUT, f))
FT_IN, FT_OUT = os.path.join(SRC, 'ferramentas'), os.path.join(OUT, 'ferramentas')
os.makedirs(FT_OUT)
shutil.copy(os.path.join(FT_IN, 'INDICE.md'), os.path.join(FT_OUT, 'INDICE.md'))
# licences -> one file
lic = ['# Licenças das ferramentas\n']
for f in sorted(os.listdir(os.path.join(FT_IN, 'licencas'))):
    lic.append(f'\n\n---\n\n## {f}\n\n```text\n' + open(os.path.join(FT_IN, 'licencas', f)).read().rstrip() + '\n```\n')
open(os.path.join(FT_OUT, 'LICENCAS.md'), 'w').write(''.join(lic))

for dept in ('marketing', 'redes', 'financas', 'juridico', 'design'):
    din, dout = os.path.join(FT_IN, dept), os.path.join(FT_OUT, dept)
    os.makedirs(dout)
    for entry in sorted(os.listdir(din)):
        p = os.path.join(din, entry)
        if os.path.isfile(p):  # dept-level guide / README / CONNECTORS
            if entry == 'GUIA.md':
                shutil.copy(p, os.path.join(dout, '_LER-PRIMEIRO.md'))
            elif entry == 'CONNECTORS.md':
                shutil.copy(p, os.path.join(dout, '_CONNECTORS.md'))
            continue  # README.md of upstream plugin dropped (covered by _LER-PRIMEIRO)
        key = f'{dept}/{entry}'
        if key in KEEP_TREE:
            tdir = os.path.join(dout, entry)
            shutil.copytree(p, tdir, ignore=shutil.ignore_patterns('*.md', '__pycache__', 'tests'))
            open(os.path.join(tdir, 'GUIA.md'), 'w').write(merge_tool(p, key, entry, keep_tree=True))
        else:
            open(os.path.join(dout, entry + '.md'), 'w').write(
                merge_tool(p, key, entry, slim=SLIM.get(key)))
