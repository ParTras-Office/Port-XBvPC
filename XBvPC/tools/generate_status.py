#!/usr/bin/env python3
"""Render the public research milestone summary from reviewed metadata."""
import argparse
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'/'milestones.json'
OUTPUT=ROOT/'docs'/'STATUS.md'

def render(data):
    lines=[
        '# Project status — evidence from local research logs',
        '',
        '**As of:** '+data['updated_utc'],
        '',
        '**Latest certified milestone:** `'+data['latest_certified']+'`',
        '',
        '> This table summarizes user-supplied local operator logs. It is not a GitHub CI or independent audit.',
        '',
        '| Milestone | Status | Tests | Verified research scope |',
        '|---|---|---|---|'
    ]
    for row in data['milestones']:
        status='Local PASS' if row['status']=='verified_local' else 'PENDING / not certified'
        lines.append('| '+row['id']+' | '+status+' | '+(row['checks'] or '—')+' | '+row['summary']+' |')
    lines+=['','No real commercial Xbox title has been booted or tested in this research lab. This is **not** a working Xbox emulator.','',
            'Source/fixture hashes and full gate logs should be retained in a private provenance archive and redacted before selective publication.','']
    return '\n'.join(lines)

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--check',action='store_true')
    args=p.parse_args()
    actual=render(json.loads(DATA.read_text(encoding='utf-8')))
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding='utf-8')!=actual:
            raise SystemExit('STATUS.md out of date: run python3 tools/generate_status.py')
        print('STATUS_SYNC=PASS')
    else:
        OUTPUT.write_text(actual,encoding='utf-8')
        print('STATUS_WRITTEN='+str(OUTPUT))
if __name__=='__main__':
    main()
