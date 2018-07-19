import logging
import time
import unittest
from hashmap import HashMap, OptimizedHashMap


class TestHashMap(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestHashMap, self).__init__(*args, **kwargs)
        logging.basicConfig(level=logging.DEBUG)

    def test_1(self):

        value_a='Value A'
        key_a='a'
        hashmap = HashMap()
        hashmap.put(key_a, value_a)
        self.assertEqual(value_a, hashmap.get(key_a))
        # logging.basicConfig(level=logging.DEBUG)
        logging.info('Got %s', hashmap.get(key_a))


    def test_2(self):
        value_a='Value A'
        key_a='a'
        value_b='Value B'
        key_b='b'

        hashmap = HashMap()
        hashmap.put(key_a, value_a)
        hashmap.put(key_b, value_b)

        self.assertEqual(value_a, hashmap.get(key_a))
        # logging.basicConfig(level=logging.DEBUG)
        logging.info('Got %s', hashmap.get(key_a))



    def test_overwrite_value(self):
        value_a='Value A'
        key_a='a'
        value_b='Value B'
        key_b='a'

        hashmap = HashMap()
        hashmap.put(key_a, value_a)
        hashmap.put(key_b, value_b)

        self.assertEqual(value_b, hashmap.get(key_a))
        # logging.basicConfig(level=logging.DEBUG)
        logging.info('Got %s', hashmap.get(key_a))

# TestHashMap()

class TestOptimizedHashMap(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestOptimizedHashMap, self).__init__(*args, **kwargs)
        logging.basicConfig(level=logging.DEBUG)

    def test_1(self):
        value_a='Value A'
        key_a='a'
        hashmap = OptimizedHashMap()
        hashmap.put(key_a, value_a)
        self.assertEqual(value_a, hashmap.get(key_a))

        logging.info('Got %s', hashmap.get(key_a))


    def test_2(self):
        value_a='Value A'
        key_a='a'
        value_b='Value B'
        key_b='b'

        hashmap = OptimizedHashMap()
        hashmap.put(key_a, value_a)
        hashmap.put(key_b, value_b)

        self.assertEqual(value_a, hashmap.get(key_a))
        # logging.basicConfig(level=logging.DEBUG)
        logging.info('Got %s', hashmap.get(key_a))



    def test_overwrite_value(self):
        value_a='Value A'
        key_a='a'
        value_b='Value B'
        key_b='a'

        hashmap = OptimizedHashMap()
        hashmap.put(key_a, value_a)
        hashmap.put(key_b, value_b)

        self.assertEqual(value_b, hashmap.get(key_a))
        # logging.basicConfig(level=logging.DEBUG)
        logging.info('Got %s', hashmap.get(key_a))


    def test_large_nb(self):
        '''

        OptimizedHashMap
        INFO:root:10000 put done in 0.261 secs
        INFO:root:10000 get done in 0.225 secs

        HashMap:
        INFO:root:10000 put done in 2.579 secs
        INFO:root:10000 get done in 2.366 secs

        :return:
        '''
        hashmap = HashMap()
        # hashmap = OptimizedHashMap()

        nb=10000
        start=time.time()
        for i in range(nb):
            value_a='Value {}'.format(i)
            key_a='a_{}'.format(i)
            hashmap.put(key_a, value_a)
        logging.info('%s put done in %.3f secs', nb, time.time()-start)
        # hashmap.put(key_b, value_b)

        # self.assertEqual(value_b, hashmap.get(key_a))
        logging.basicConfig(level=logging.DEBUG)
        mid = time.time()
        for i in range(nb):
            hashmap.get('a_{}'.format(i))
        logging.info('%s get done in %.3f secs', nb, time.time()-mid)

        logging.info('Got %s', hashmap.get('a_0'))



if __name__ == '__main__':
    unittest.main()