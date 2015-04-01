class node:
	def __init__(self):
		self.edge 	= {}


class auto:
	def __init__(self, motif, error=1):
		self.motif 	= motif
		self.allow 	= {"A":"A", "T": "T", "G":"G", "C":"C"}
		self.tple 	= list()
		self.error 	= error
		assert self.build_layer(), "motif must contain only A,T,G,C symbols"
		self.makeDFA()
	def build_layer(self):
		i 	= 0
		N 	= len(self.motif)
		while i < N:
		 	letter 	= self.motif[i]
			if letter == "[":
				j 	= i
				while i < N and self.motif[i]!="]":
					i+=1
				n 				= node()
				transitions 	= [l for l in self.motif[j+1:i].split(",")]
				assert len([1 for l in self.motif[j+1:i].split(",") if len(l) >1]) ==0, "incorrect motif format, bracket,[, found but no corresponding closing, ] "
			else:
				transitions 	= [letter]
			self.tple.append(transitions)
			i+=1
		return True
	def makeDFA(self):
		#the NFA consists of three things, an insertion, a deletion and a SNP (so to speak...)
		#we want to make the powerset 
		N 	= len(self.tple)
		i 	= 0
		while i < N:
			#want to make a copy of the possible states
			#so we make a list of a collection of possible states for this i position
			NFA 	= [(self.tple[i], 0)]

			for e,j in enumerate(range(i,i+self.error)):
				#go ahead two (insertion or SNP) and stay one (deletion)
				NFA.append((self.tple[j], e+1 ))
			i+=1
			print NFA



if __name__ == "__main__":
	motif 	= "[A,T]GCC[A,T]"
	auto(motif)


