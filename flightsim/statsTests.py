import math
import unittest

from stats import *

class StatsTestCase(unittest.TestCase):
	# Tests for getSumOfX
	def test_getSumOfX_noValues(self):
		with self.assertRaises(Exception) as context:
			getSumOfX([]);

		self.assertTrue('values must contain at least one value!' in str(context.exception));
	
	def test_getSumOfX_singleValue(self):
		self.assertAlmostEqual(0.1, getSumOfX([0.1]));
		
	def test_getSumOfX_multipleValues(self):
		self.assertAlmostEqual(0.2, getSumOfX([0.1,0.1]));
	
	# Tests for getSumOfX2
	def test_getSumOfX2_noValues(self):
		with self.assertRaises(Exception) as context:
			getSumOfX2([]);

		self.assertTrue('values must contain at least one value!' in str(context.exception));
	
	def test_getSumOfX2_singleValue(self):
		self.assertAlmostEqual(0.01, getSumOfX2([0.1]));
		
	def test_getSumOfX2_multipleValues(self):
		self.assertAlmostEqual(0.02, getSumOfX2([0.1,0.1]));
	
	# Tests for getSumOfXY
	def test_getSumOfXY_noXValues(self):
		with self.assertRaises(Exception) as context:
			getSumOfXY([],[1]);

		self.assertTrue('xValues must contain at least one value!' in str(context.exception));
	
	def test_getSumOfXY_noYValues(self):
		with self.assertRaises(Exception) as context:
			getSumOfXY([1],[]);

		self.assertTrue('yValues must contain at least one value!' in str(context.exception));
	
	def test_getSumOfXY_differentLengths(self):
		with self.assertRaises(Exception) as context:
			getSumOfXY([1],[2,3]);

		self.assertTrue('xValues and yValues must have the same lenght!' in str(context.exception));
	
	def test_getSumOfXY_singleValue(self):
		self.assertAlmostEqual(0.01, getSumOfXY([0.1],[0.1]));
		
	def test_getSumOfXY_multipleValues(self):
		self.assertAlmostEqual(0.02, getSumOfXY([0.1,0.1],[0.1,0.1]));
	
	# Tests for getSXY
	def test_getSXY_positiveValue(self):
		self.assertAlmostEqual(7.1, getSXY(9.8, 0.3, 4.5, 2));
		
	def test_getSXY_negativeValue(self):
		self.assertAlmostEqual(-48.8, getSXY( 4.0, 4.4, 2.4, 5));
	
	# Tests for getSXX
	def test_getSXX_positiveValue(self):
		self.assertAlmostEqual(0.5, getSXX(13, 6.25, 2));
		
	def test_getSXX_negativeValue(self):
		with self.assertRaises(Exception) as context:
			getSXX(4.0, 2.4, 5);

		self.assertTrue('Inputs are invalid!' in str(context.exception));
	
	# Tests for getR
	def test_getR_negativeSXX(self):
		with self.assertRaises(Exception) as context:
			getR(-4.0, 2.4, 5);

		self.assertTrue('sXX are invalid!' in str(context.exception));
	
	def test_getR_negativeSYY(self):
		with self.assertRaises(Exception) as context:
			getR(4.0, -2.4, 5);

		self.assertTrue('sYY are invalid!' in str(context.exception));
	
	def test_getR_zeroSXX(self):
		with self.assertRaises(Exception) as context:
			getR(-4.0, 0, 5);

		self.assertTrue('sXX are invalid!' in str(context.exception));
	
	def test_getR_zeroSYY(self):
		with self.assertRaises(Exception) as context:
			getR(4.0, -2.4, 0);

		self.assertTrue('sYY are invalid!' in str(context.exception));
	
	def test_getR_validValue(self):
		self.assertAlmostEqual(5.2, getR(0.5, 12.5,13));
		
	# Tests for getSumOfXY
	def test_getSumOfXY_noXValues(self):
		with self.assertRaises(Exception) as context:
			getSumOfXY([],[1]);

		self.assertTrue('xValues must contain at least one value!' in str(context.exception));
	
	# Tests for calculateCorrelation
	def test_calculateCorrelation_noXValues(self):
		with self.assertRaises(Exception) as context:
			calculateCorrelation([],[1]);

		self.assertTrue('xValues must contain at least one value!' in str(context.exception));
		
	def test_calculateCorrelation_noYValues(self):
		with self.assertRaises(Exception) as context:
			calculateCorrelation([1],[]);

		self.assertTrue('yValues must contain at least one value!' in str(context.exception));
	
	def test_calculateCorrelation_differentLengths(self):
		with self.assertRaises(Exception) as context:
			calculateCorrelation([1],[2,3]);

		self.assertTrue('xValues and yValues must have the same lenght!' in str(context.exception));
	
	def test_calculateCorrelation_invalidSingleValue(self):
		with self.assertRaises(Exception) as context:
			calculateCorrelation([0.1],[0.1]);

		self.assertTrue('Inputs are invalid!' in str(context.exception));
		
	def test_calculateCorrelation_multipleValues(self):
		self.assertAlmostEqual(-1, calculateCorrelation([0.1,0.2],[0.2,0.1]));

if __name__ == '__main__':
	unittest.main()