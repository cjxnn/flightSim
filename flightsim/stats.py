import math

def getSumOfX(values):
	if not len(values):
		raise Exception('values must contain at least one value!');
		
	result = 0;
	for value in values:
		result += value;
	return result;
	
def getSumOfX2(values):
	if not len(values):
		raise Exception('values must contain at least one value!');
		
	result = 0;
	for value in values:
		result += value**2;
	return result;

def getSumOfXY(xValues,yValues):
	if not len(xValues):
		raise Exception('xValues must contain at least one value!');
	if not len(yValues):
		raise Exception('yValues must contain at least one value!');
	if len(xValues) != len(yValues):
		raise Exception('xValues and yValues must have the same lenght!');
		
	result = 0;
	for (x,y) in zip(xValues,yValues):
		result += x*y;
	return result;

def getSXY(sumXY, avgX, avgY, n):
	return sumXY - n * avgX * avgY;

def getSXX(sumXX, avgX2, n):
	answer = sumXX - n * avgX2;
	if answer < 0:
		raise Exception('Inputs are invalid!');
	return answer;
	
def getR(sXX, sYY, sXY):
	if sXX <= 0:
		raise Exception('sXX are invalid!');
	if sYY <= 0:
		raise Exception('sYY are invalid!');
	return sXY / math.sqrt(sXX * sYY);
	
def calculateCorrelation(xValues, yValues):
	if not len(xValues):
		raise Exception('xValues must contain at least one value!');
	if not len(yValues):
		raise Exception('yValues must contain at least one value!');
	if len(xValues) != len(yValues):
		raise Exception('xValues and yValues must have the same lenght!');

	n = len(xValues);
	
	avgX = getSumOfX(xValues)/n;
	avgY = getSumOfX(yValues)/n;
	sumXX = getSumOfX2(xValues);
	sumYY = getSumOfX2(yValues);
	sumXY = getSumOfXY(xValues, yValues);
	
	sXY = getSXY(sumXY, avgX, avgY, n);
	sXX = getSXX(sumXX, avgX**2, n);
	sYY = getSXX(sumYY, avgY**2, n);
	
	try:
		answer = getR(sXX, sYY, sXY);
	except Exception:
		raise Exception('Inputs are invalid!');
	return answer;