def main(args):

	from DAH import PCF8574
	import numpy as np
	import pylab as pl
	import pygame, time, math
	from scipy import signal
	
	#specify the address for the chip expander as more than one can be used at the same time
	pcf = PCF8574(address = 0x38)
		
	#constants
	global outputRate
	global maxAmplitude

	outputRate = 44100
	maxAmplitude = np.iinfo(np.int16).max
	nLen = 0.4
	
	#pure note frequencies
	c4 = 261.65
	d4 = 293.65
	e4 = 329.62
	f4 = 349.23
	g4 = 391.99
	a4 = 440.00
	b4 = 493.88
	c5 = 523.25
	
	
	#generates different types of waveforms
	def SineWave(p,v,d):
		global outputRate 
		global maxAmplitude
		
		totalSamples = int(outputRate*d)
		outputBuffer = np.zeros((totalSamples,2), dtype = np.int16)
		amplitude = int(maxAmplitude * v)
		waveStep = float(p/outputRate)*2*math.pi
		
		for i in range(totalSamples):
			#left channel
			outputBuffer[i][0] = amplitude * np.sin(i*waveStep)
			
			#right channel
			outputBuffer[i][1] = amplitude * np.sin(i*waveStep)
			
		print("DONE")
		return outputBuffer
		
	def SquareWave(p,v,d):
		
		global outputRate 
		global maxAmplitude
		
		totalSamples = int(outputRate*d)
		outputBuffer = np.zeros((totalSamples,2), dtype = np.int16)
		amplitude = int(maxAmplitude * v)
		waveStep = float(p/outputRate)*2*math.pi
		
		for i in range(totalSamples):
			#left channel
			outputBuffer[i][0] = amplitude * np.round(np.sin(i*waveStep))
			
			#right channel
			outputBuffer[i][1] = amplitude * np.round(np.sin(i*waveStep))
			
		print("DONE")
		return outputBuffer

	def QuadraticFourier(x):
		f = (math.pi**2)/3
		
		for n in range(1,10):
			f += 4*((-1)**n)/(n*n)*np.cos(n*x)
			
		return f	
	
	def QuadWave(p,v,d):
		
		global outputRate 
		global maxAmplitude
		
		totalSamples = int(outputRate*d)
		outputBuffer = np.zeros((totalSamples,2), dtype = np.int16)
		amplitude = int(maxAmplitude * v)
		waveStep = float(p/outputRate)*2*math.pi
		
		for i in range(totalSamples):
			#left channel
			outputBuffer[i][0] = amplitude * QuadraticFourier(i*waveStep)
			
			#right channel
			outputBuffer[i][1] = amplitude * QuadraticFourier(i*waveStep)
			
		print("DONE")
		return outputBuffer
	
	def TriangleWave(p,v,d):
		global outputRate 
		global maxAmplitude
		
		totalSamples = int(outputRate*d)
		outputBuffer = np.zeros((totalSamples,2), dtype = np.int16)
		amplitude = int(maxAmplitude * v)
		waveStep = float(p/outputRate)*2*math.pi
			
		t = np.linspace(0,d, totalSamples)
		Tri = signal.sawtooth(2*math.pi*p*t) 
		
		for i in range(totalSamples):
			#left channel
			outputBuffer[i][0] = amplitude * Tri[i]
			
			#right channel
			outputBuffer[i][1] = amplitude * Tri[i]
			
		print("DONE")
		return outputBuffer
	
	#set up audio
	waveForm = input("Select waveform: ")	
	pygame.mixer.init(frequency = outputRate, channels = 2, size = -16)
	
	#create notes of the right waveform depending on user input
	if waveForm == "Sine":
		C4 = SineWave(c4,1,nLen)
		D4 = SineWave(d4,1,nLen)
		E4 = SineWave(e4,1,nLen)
		F4 = SineWave(f4,1,nLen)
		G4 = SineWave(g4,1,nLen)
		A4 = SineWave(a4,1,nLen)
		B4 = SineWave(b4,1,nLen)
		C5 = SineWave(c5,1,nLen)
		
		noteC4 = pygame.mixer.Sound(buffer = C4)
		noteD4 = pygame.mixer.Sound(buffer = D4)
		noteE4 = pygame.mixer.Sound(buffer = E4) 
		noteF4 = pygame.mixer.Sound(buffer = F4)
		noteG4 = pygame.mixer.Sound(buffer = G4)
		noteA4 = pygame.mixer.Sound(buffer = A4)
		noteB4 = pygame.mixer.Sound(buffer = B4)
		noteC5 = pygame.mixer.Sound(buffer = C5)	
			
	elif waveForm == "Square":
		C4 = SquareWave(c4,1,nLen)
		D4 = SquareWave(d4,1,nLen)
		E4 = SquareWave(e4,1,nLen)
		F4 = SquareWave(f4,1,nLen)
		G4 = SquareWave(g4,1,nLen)
		A4 = SquareWave(a4,1,nLen)
		B4 = SquareWave(b4,1,nLen)
		C5 = SquareWave(c5,1,nLen)
		
		noteC4 = pygame.mixer.Sound(buffer = C4)
		noteD4 = pygame.mixer.Sound(buffer = D4)
		noteE4 = pygame.mixer.Sound(buffer = E4) 
		noteF4 = pygame.mixer.Sound(buffer = F4)
		noteG4 = pygame.mixer.Sound(buffer = G4)
		noteA4 = pygame.mixer.Sound(buffer = A4)
		noteB4 = pygame.mixer.Sound(buffer = B4)
		noteC5 = pygame.mixer.Sound(buffer = C5)	
			
	elif waveForm == "Triangle":
		C4 = TriangleWave(c4,1,nLen)
		D4 = TriangleWave(d4,1,nLen)
		E4 = TriangleWave(e4,1,nLen)
		F4 = TriangleWave(f4,1,nLen)
		G4 = TriangleWave(g4,1,nLen)
		A4 = TriangleWave(a4,1,nLen)
		B4 = TriangleWave(b4,1,nLen)
		C5 = TriangleWave(c5,1,nLen)
		
		noteC4 = pygame.mixer.Sound(buffer = C4)
		noteD4 = pygame.mixer.Sound(buffer = D4)
		noteE4 = pygame.mixer.Sound(buffer = E4) 
		noteF4 = pygame.mixer.Sound(buffer = F4)
		noteG4 = pygame.mixer.Sound(buffer = G4)
		noteA4 = pygame.mixer.Sound(buffer = A4)
		noteB4 = pygame.mixer.Sound(buffer = B4)
		noteC5 = pygame.mixer.Sound(buffer = C5)	
		
	elif waveForm == "Quadratic":
		C4 = QuadWave(c4,1,nLen)
		D4 = QuadWave(d4,1,nLen)
		E4 = QuadWave(e4,1,nLen)
		F4 = QuadWave(f4,1,nLen)
		G4 = QuadWave(g4,1,nLen)
		A4 = QuadWave(a4,1,nLen)
		B4 = QuadWave(b4,1,nLen)
		C5 = QuadWave(c5,1,nLen)
		
		noteC4 = pygame.mixer.Sound(buffer = C4)
		noteD4 = pygame.mixer.Sound(buffer = D4)
		noteE4 = pygame.mixer.Sound(buffer = E4) 
		noteF4 = pygame.mixer.Sound(buffer = F4)
		noteG4 = pygame.mixer.Sound(buffer = G4)
		noteA4 = pygame.mixer.Sound(buffer = A4)
		noteB4 = pygame.mixer.Sound(buffer = B4)
		noteC5 = pygame.mixer.Sound(buffer = C5)
		
	elif waveForm == "Piano":
	
		noteC4 = pygame.mixer.Sound("Notes/C4-49-96.wav")
		noteD4 = pygame.mixer.Sound("Notes/D4-49-96.wav")
		noteE4 = pygame.mixer.Sound("Notes/E4-49-96.wav") 
		noteF4 = pygame.mixer.Sound("Notes/F4-49-96.wav")
		noteG4 = pygame.mixer.Sound("Notes/G4-49-96.wav")
		noteA4 = pygame.mixer.Sound("Notes/A4-49-96.wav")
		noteB4 = pygame.mixer.Sound("Notes/B4-49-96.wav")
		noteC5 = pygame.mixer.Sound("Notes/C5-49-96.wav")	

	#key detection and populating channels with notes	
	while True:
		if (pcf.digitalRead(0) == True):
			noteC4.play(maxtime = int(nLen*1000))
		if (pcf.digitalRead(1) == True):
			noteD4.play(maxtime = int(nLen*1000))
		if (pcf.digitalRead(2) == True):
			noteE4.play(maxtime = int(nLen*1000))
		if (pcf.digitalRead(3) == True):
			noteF4.play(maxtime = int(nLen*1000))
		if (pcf.digitalRead(4) == True):
			noteG4.play(maxtime = int(nLen*1000))
		if (pcf.digitalRead(5) == True):
			noteA4.play(maxtime = int(nLen*1000))
		if (pcf.digitalRead(6) == True):
			noteB4.play(maxtime = int(nLen*1000))
		if (pcf.digitalRead(7) == True):
			noteC5.play(maxtime = int(nLen*1000))
			
	return 0
	
	
if __name__ == "__main__":
	import sys
	sys.exit(main(sys.argv))
