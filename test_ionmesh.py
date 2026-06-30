# test_ionmesh.py
"""
Tests for IonMesh module.
"""

import unittest
from ionmesh import IonMesh

class TestIonMesh(unittest.TestCase):
    """Test cases for IonMesh class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = IonMesh()
        self.assertIsInstance(instance, IonMesh)
        
    def test_run_method(self):
        """Test the run method."""
        instance = IonMesh()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
