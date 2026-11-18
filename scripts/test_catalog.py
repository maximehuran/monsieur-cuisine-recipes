import copy
import json
import tempfile
import unittest
from pathlib import Path
from build_catalog import ROOT, build, validate


class CatalogTest(unittest.TestCase):
    def setUp(self):
        self.recipe = json.loads((ROOT / 'recipes/nettoyage-doux-du-bol.json').read_text())

    def test_cleaning_recipe_limits_and_explicit_review(self):
        validate(self.recipe)
        steps = [s for s in self.recipe['steps'] if 'machine' in s]
        for step in steps:
            self.assertTrue(step['needsReview'])
            machine = step['machine']
            if machine['tempC'] == 0:
                self.assertEqual((30, 5), (machine['seconds'], machine['speed']))
            else:
                self.assertEqual(37, machine['tempC'])
                self.assertEqual(1, machine['speed'])
                self.assertLessEqual(machine['seconds'], 120)
        self.assertEqual(4, len(steps))
        self.assertEqual(37, steps[-1]['machine']['tempC'])

    def test_reject_unsafe_and_unreviewed_settings(self):
        for key, value in [('speed', 11), ('tempC', 80), ('seconds', -1), ('seconds', True)]:
            recipe = copy.deepcopy(self.recipe)
            next(s for s in recipe['steps'] if 'machine' in s)['machine'][key] = value
            with self.assertRaises(ValueError):
                validate(recipe)
        recipe = copy.deepcopy(self.recipe)
        next(s for s in recipe['steps'] if 'machine' in s)['needsReview'] = False
        with self.assertRaises(ValueError):
            validate(recipe)

    def test_stable_revision_and_unique_ids(self):
        self.assertEqual(build(), build())
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)
            for name in ['a', 'b']:
                (path / f'{name}.json').write_text(json.dumps(self.recipe))
            with self.assertRaises(ValueError):
                build(path)

    def test_ids_are_accepted_by_the_android_client(self):
        for value in ['web-123', 'perso-éponge', 'perso-', 'perso-A', 'perso-' + 'a' * 97]:
            recipe = copy.deepcopy(self.recipe)
            recipe['id'] = value
            with self.assertRaises(ValueError):
                validate(recipe)


if __name__ == '__main__':
    unittest.main()
