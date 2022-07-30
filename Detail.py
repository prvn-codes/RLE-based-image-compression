'''
Created on 07 Apr 2021

@author: Praveen
'''

class Detail(object):
	'''
	classdocs
	'''


	def __init__(self, compressed, hist, width, height, mode, scanning , palette = None):
		'''
		Constructor
		'''
		self.compressed = compressed
		self.hist = hist
		self.height = height
		self.width = width
		self.mode = mode
		self.scanning = scanning
		self.palette = palette
