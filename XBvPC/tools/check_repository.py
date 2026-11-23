#!/usr/bin/env python3
"""Conservative pre-publish hygiene checks, NOT a complete secrets audit."""
import json
import re
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MAX_SIZE=1024*1024  # require manual review for any individual file >1 MiB
DISALLOWED_SUFFIXES={'.dll','.exe','.obj','.o','.pdb','.so','.dylib','.bin','.iso','.xex','.xvc','.pak','.key','.pem','.p12','.pfx','.zip','.7z','.rar'}
DISALLOWED_DIRS={'build','build-linux','build-windows','__pycache__','.venv','.cache'}
TOKEN_MARKERS=[
    re.compile(rb'gh[pousr]_[A-Za-z0-9_]{20,}'),
    re.compile(rb'github_pat_[A-Za-z0-9_]{20,}'),
    re.compile(rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    re.compile(rb'AKIA[0-9A-Z]{16}')
]

def list_candidates():
    if (ROOT/'.git').exists():
        completed=subprocess.run(['git','-C',str(ROOT),'ls-files','-z'],capture_output=True,check=True)
        return [ROOT/x.decode('utf-8','surrogateescape') for x in completed.stdout.split(b'\0') if x]
    return [x for x in ROOT.rglob('*') if x.is_file()]

def check():
    errors=[]
    for p in list_candidates():
        if not p.is_file():
            errors.append('tracked file missing: '+str(p))
            continue
        rel=p.relative_to(ROOT)
        if any(part in DISALLOWED_DIRS or part.startswith('run-20') for part in rel.parts):
            errors.append('generated tree forbidden: '+str(rel))
        if p.suffix.lower() in DISALLOWED_SUFFIXES:
            errors.append('binary/secret suffix forbidden: '+str(rel))
        if p.name.startswith('.env') and p.name!='.env.example':
            errors.append('environment secrets forbidden: '+str(rel))
        if p.stat().st_size>MAX_SIZE:
            errors.append('file requires manual review (>1 MiB): '+str(rel))
            continue
        contents=p.read_bytes()
        for pattern in TOKEN_MARKERS:
            if pattern.search(contents):
                errors.append('potential secret marker: '+str(rel))
                break
    data=json.loads((ROOT/'data'/'milestones.json').read_text(encoding='utf-8'))
    verified=[x['id'] for x in data['milestones'] if x['status']=='verified_local']
    pending=[x['id'] for x in data['milestones'] if x['status']=='pending']
    if not verified or verified[-1]!=data['latest_certified']:
        errors.append('latest_certified does not match the last verified local milestone')
    for m in data['milestones']:
        if m['status'] not in ('verified_local','pending'):
            errors.append('invalid milestone status: '+m['id'])
        if m['status']=='pending' and m['checks'] is not None:
            errors.append('pending milestone has test claim: '+m['id'])
    if errors:
        for error in errors:
            print('PREFLIGHT_FAIL='+error)
        raise SystemExit(1)
    print('PREFLIGHT=PASS')
    print('LAST_VERIFIED='+data['latest_certified'])
    print('WARNING=Static checks do not replace manual rights/secrets review')
if __name__=='__main__':
    check()
