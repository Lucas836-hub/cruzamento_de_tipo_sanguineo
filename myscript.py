# Criado por : Lucas gabriel
# github : https://github.com/Lucas836-hub/
# instagram : @lucas_git

# Ia Ib Iab i
# Ia+ Ib+ Iab+ i+ # Ia- Ib- Iab- i-
import os
import update_file # CHAMANDO O ATUALIZADOR

class run:
	def __init__(self):

		# VERIFICANDO ATUALIZACOES
		try:
			if update_file.check_atualizacao("https://github.com/Lucas836-hub/cruzamento_de_tipo_sanguineo"):
				# ATUALIZANDO O SCRIPT LOCAL
				print("\033[93mATENÇÃO ATUALIZAÇÃO DETECTADA\033[m".center(60))
				
				while True:
					sn=input("Você deseja atualizar ? S/N : ").strip().lower().replace("sim", "s").replace("ss", "s").replace(
			"nao", "n").replace("não", "n").replace("nn", "n")
					if sn =="n" or sn == "s":
						break
					else:
						print("resposta invalida !!!")
				if sn == "s":		
					update_file.atualizar("https://github.com/Lucas836-hub/cruzamento_de_tipo_sanguineo")
					update_file.instalador_biblioteca()
		except:
			pass

		self.limp()

		q=["Da mãe :","Do filho : ","Do pai : "]
		quem=None # de quem sera o resultado d teste
		self.tip = [] # genomas que serao cruzados
		self.matriz_resposta=[] #resposta final em formato de matriz
		self.porc_tip=[] # porccentagem de cada genoma
		c_ativo = False
		self.pimt = False

		todos_tipos=[[["Ia", "Ia"],[ "Ia", "Ii"]] \
		,[["Ib", "Ib"], ["Ib", "Ii"]] \
		,[["Ia", "Ib"]]\
		,[["Ii", "Ii"]]]

		rh=[[["R","r"],["R","R"]],[[],["r","r"]]]
		rh_resp=[]
		# cromossomos dos tipos sanguineos

		for c in range(0,3):
			print(f"Qual tipo sanguineo \033[94m{q[c]}\033[m")
			print("Digite :\n        1 - A\n        2 - B\n        3 - AB\n        4 - O\n",end="",flush=True)
			
			if quem == None:
				print("        5 - Quero saber")
				t=self.opcao(1,5)
			else:
				t=self.opcao(1,4)

			if t == 5 or t == 4 or t == 3:
				g=1
			else:
				print("\033[94mDigite :\n        1 - para homozigoto (alelos iguais)\n        2 - para heterozigoto (alelos diferentes)\n        3 - para não sei\033[m")
				g=self.opcao(1,3)
			if t == 5:
				quem=c
			else:
				if g == 3:
					c_ativo=True
					self.tip.append(todos_tipos[t - 1])
					#print("todos ",todos_tipos[t - 1])
				else:
					tem=[""]
					tem.append(todos_tipos[t-1][g-1])
					self.tip.append(tem)
				#	print("todos ",todos_tipos[t-1][g-1])
					
					
	#	print(f"tip {self.tip} \n len {len(self.tip)} 0 {self.tip[0]} 1 {self.tip[1]} \n 00 {self.tip[0][0]} {len(self.tip[0][0])} 10 {self.tip[1][0]}")
		self.limp()
		for pa in range(0,len(self.tip[0])):
			if self.tip[0][pa] == "":
				continue
			else:
				if quem == None:
					u=2
				else:
					u=1
				for pb in range(0,len(self.tip[u])):
					if self.tip[u][pb] == "":
						continue
					cz=self.cruzamento(self.tip[0][pa],self.tip[u][pb]) 
					
				list_temp=[]
				if quem ==1:
						print("\033[94mRESULTADO\033[m".center(60))
						print(f"\nMãe tipo sanguineo : {self.tipo_de_sangue(self.tip[0][pa][0]+self.tip[0][pa][1])} Alelos : {self.tip[0][pa][0]}{self.tip[0][pa][1]}")
						print(f"Pai tipo sanguineo : {self.tipo_de_sangue(self.tip[1][pb][0]+self.tip[1][pb][1])} Alelos : {self.tip[1][pb][0]}{self.tip[1][pb][1]}\n")
						print("POSSIVEIS TIPOS SANGUINEOS DO FILHO :\n")
				
				if quem ==2:
						print("\033[94mRESULTADO\033[m".center(60))
						print(f"\nMãe tipo sanguineo : {self.tipo_de_sangue(self.tip[0][pa][0]+self.tip[0][pa][1])} Alelos : {self.tip[0][pa][0]}{self.tip[0][pa][1]}")
						print(f"Filho tipo sanguineo : {self.tipo_de_sangue(self.tip[1][pb][0]+self.tip[1][pb][1])} Alelos : {self.tip[1][pb][0]}{self.tip[1][pb][1]}\n")
						print("POSSIVEIS TIPOS SANGUINEOS DO PAI :\n")
						
				if quem ==None:
						print("\033[94mRESULTADO\033[m".center(60))
						print(f"\n\033[96mMãe tipo sanguineo : {self.tipo_de_sangue(self.tip[0][pa][0]+self.tip[0][pa][1])} Alelos : {self.tip[0][pa][0]}{self.tip[0][pa][1]}")
						print(f"Filho tipo sanguineo : {self.tipo_de_sangue(self.tip[1][pb][0]+self.tip[1][pb][1])} Alelos : {self.tip[1][pb][0]}{self.tip[1][pb][1]}")
						print(f"Pai tipo sanguineo : {self.tipo_de_sangue(self.tip[2][pb][0]+self.tip[2][pb][1])} Alelos : {self.tip[2][pb][0]}{self.tip[2][pb][1]}\033[m\n")
						
						print("POSSIVEIS TIPOS SANGUINEOS DO Filho :\n")
						
				for hj in range(0,len(cz)):
					
				#	print(hj)
				#	print(f"\033[31mresultado do cruzamento {cz}\033[m")
					if not self.tipo_de_sangue(cz[hj]) in list_temp:
						print(f"Alelos {cz[hj]} = Tipo {self.tipo_de_sangue(cz[hj])} com provabilidade de {self.porcento(cz,cz[hj])}%")
						list_temp.append(self.tipo_de_sangue(cz[hj]))
				
				# DIZ SE E O PAI	
				if quem == None:
					dfg=False
					try:
						if str(self.tip[1][1][0]+self.tip[1][1][1]) in cz :
							dfg=True
					except:
						pass
					try:
						if str(self.tip[1][0][0]+self.tip[1][0][1]) in cz :
							dfg=True
					except:
						pass
						
					if dfg:
						print("\n\033[92mHá provabilidade do pai ser o pai dele\033[m")
					else :
						print("\n\033[93mNão há provabilidade do pai ser o pai dele\033[m")
						#print(cz)
						#print(self.tip[1][0])
						#print(self.tip[1][1])
						
		

	def tipo_de_sangue(self,par):

		if par == "IaIi" or par == "IiIa" :
			return "A (HOMOZIGOTO) "
		if par == "IaIa":
			return "A (HETEROZIGOTO) "

		if par == "IiIb" or par ==  "IbIi" :
			return "B (HOMOZIGOTO) "
		if par == "IbIb" :
			return "B (HETEROZIGOTO) "

		if par == "IiIi" :
			return "O"

		if par == "IaIb" or par == "IbIa" :
			return "AB"


	def plataforma(self):
		import platform
		return platform.system()
		
	def limp(self):
		s=self.plataforma()
		
		if s == "Linux" :
			os.system("clear")
			
		if s == "Windows" :
			os.system("cls")
			
		if s == "Darwin" :
			os.system("clear")

	def txt_p(self,txt):
		if self.pimt :
			print(txt)
			
			
	def cruzamento(self,a=[],b=[]):
		m_cruzadas=[]
		
	#	print(f"\033[33m{a} |  {b}  lista recebida\033[m")

		for c in range(0,len(a)):
			for d in range(0,len(b)):
				ctpm=str(f"{a[c]}{b[d]}")
				m_cruzadas.append(ctpm)
			#	print(f"\033[35m   {a[c]} + {b[d]} alelos ctpm {ctpm}\033[m")
	
	#	print(f"\033[33mresul cruzada {m_cruzadas} \033[m")		
		return m_cruzadas
		
	def porcento(self,lis,q):
		#recebe a lista e uma vareavel e retorna em porcentagem a sua incidencia
		c=0
		kl=list(q)
		lk=kl[2]+kl[3]+kl[0]+kl[1]
		for m in range(0,len(lis)):
			if lis[m]==q or lis[m]==lk:
				c+=1				
		try:
			g=c*100/4
		except ZeroDivisionError:
			g=0
		return g



	def opcao(self,m,M):# m valor minimo de opcoes M valor maximo de opcoes
		while True:
			n = input("Digite sua resposta : ")
			try:
				if(int(n) >= m and int(n) <= M):
					break
				else:
					print("\033[31mERRO RESPOSTA INVÁLIDA\033[m")
			except:
				print("\033[31mERRO CARACTERE INVÁLIDO\033[m")
		return int(n)

run()
	
