"""CI checks only metadata integrity, not emulator functionality."""
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class MilestoneMetadataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads((ROOT/'data'/'milestones.json').read_text(encoding='utf-8'))

    def test_unique_milestone_identifiers(self):
        ids=[x['id'] for x in self.data['milestones']]
        self.assertEqual(len(ids),len(set(ids)))

    def test_pending_milestones_have_no_claimed_checks(self):
        for m in self.data['milestones']:
            if m['status']=='pending':
                self.assertIsNone(m['checks'])

    def test_verified_counts(self):
        for x in self.data['milestones']:
            if x['status']=='verified_local':
                left,right=map(int,x['checks'].split('/'))
                self.assertEqual(left,right)

    def test_documentation_present(self):
        self.assertTrue((ROOT/'README.md').is_file())
        self.assertTrue((ROOT/'docs'/'EVIDENCE.md').is_file())

if __name__=='__main__':
    unittest.main()
