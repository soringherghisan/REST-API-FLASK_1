from models.item import ItemModel
from models.store import StoreModel
from tests.integration.integration_base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            # if we want to use some other db - such as mySQL or postgreSQL, we need to write:
            StoreModel('test').save_to_db()
            item = ItemModel('test', 19.99, 1)  # we don't have a store with id 1, but it's ok with sqlite

            self.assertIsNone(ItemModel.find_by_name('test'),
                              "Found an item with name {}, but expected not to.".format(item.name))

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('test'))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test_store')
            item = ItemModel('test', 19, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(item.store.name, 'test_store')

