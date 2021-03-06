from unittest import TestCase

from day10.dense_hash_processor import DenseHashProcessor


class TestDenseHashProcessor(TestCase):
    def testProcessBlock_exampleScenario(self):
        self.assertEqual(64, DenseHashProcessor.process_block([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]))

    def testProcessBlock_whenInputSizeIsNot16_ShouldRaise(self):
        self.assertRaises(Exception, DenseHashProcessor.process_block, [1, 2])

    def testInitialization_whenInputSizeIsNot256_ShouldRaise(self):
        self.assertRaises(Exception, DenseHashProcessor.__init__, [1, 2])

    def testInitialization_shouldComputeADenseHashOfLength16(self):
        dummy_sparse_hash = list(range(256))
        self.assertEqual(16, len(DenseHashProcessor(dummy_sparse_hash).get_hash()))

    def testInitialization_shouldAggregateProcessedBlocks(self):
        block = [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]
        sparse_hash = []
        for i in range(16):
            sparse_hash.extend(block)

        self.assertEqual(256, len(sparse_hash))

        expected_dense_hash = [64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64]
        self.assertEqual(expected_dense_hash, DenseHashProcessor(sparse_hash).get_hash())
