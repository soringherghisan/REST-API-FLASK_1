from models.store import StoreModel
from models.item import ItemModel
from tests.integration.integration_base_test import BaseTest


class StoreTest(BaseTest):
    # when we create a new store we want to make sure the 'items' class attr is empty
    # it's integration test because it depends on item model and on db
    def test_create_store_items_empty(self):
        store = StoreModel('test_store')
        self.assertListEqual(store.items.all(), [])

    # test json
    def test_json(self):
        store = StoreModel('test')
        expected = {
            'name': 'test',
            'items': []
        }

        self.assertDictEqual(store.json(), expected)

    # test saving and writing to db
    def test_crud(self):
        with self.app_context():
            store = StoreModel('test')
            self.assertIsNone(StoreModel.find_by_name('test'))

            store.save_to_db()
            self.assertIsNotNone(StoreModel.find_by_name('test'))

            store.delete_from_db()
            self.assertIsNone(StoreModel.find_by_name('test'))

    # test that adding item to store - items +1
    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test_item', 10, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, item.name)
