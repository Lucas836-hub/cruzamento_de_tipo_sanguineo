# Criado por : Lucas gabriel
# github : https://github.com/Lucas836-hub/
# instagram : @lucas_git

# Ia Ib Iab i
# Ia+ Ib+ Iab+ i+ # Ia- Ib- Iab- i-
import os

class run:
	def __init__(self):
		self.limp()

		q=["Da mãe :","Do filho : ","Do pai : "]
		quem=0 # de quem sera o resultado d teste
		self.tip = [] # genomas que serao cruzados
		self.matriz_resposta=[] #resposta final em formato de matriz
		self.porc_tip=[] # porccentagem de cada genoma
		c_ativo = False

		todos_tipos=[[["Ia", "Ia"],[ "Ia", "Ii"]],[["Ib", "Ib"], ["Ib", "Ii"]],[["Ia", "Ib"], ["Ib", "Ia"]],[["Ii", "Ii"], ["Ii", "Ii"]]]
		# cromossomos dos tipos sanguineos

		for c in range(0,3):
			print(f"Qual tipo sanguineo \033[34m{q[c]}\033[m")
			print("Digite :\n        1 - A\n        2 - B\n        3 - AB\n        4 - O\n        5 - Quero saber")
			t=self.opcao(1,5)

			if t == 5 or t == 4 or t == 3:
				g=1
			else:
				print("\033[34mDigite :\n        1 - para homozigoto (alelos iguais)\n        2 - para heterozigoto (alelos diferentes)\n        3 - para não sei\033[m")
				g=self.opcao(1,3)
			if t == 5:
				quem=c
			else:
				if g == 3:
					c_ativo=True
					self.tip.append(todos_tipos[t - 1][0])
				else:
					self.tip.append(todos_tipos[t-1][g-1])
		self.cruzamento()
		print("-+"*40)

		print(f"  |  {self.tip[0][0]}  |  {self.tip[0][1]}  |\n"
			  f"{self.tip[1][0]}| {self.matriz_resposta[0]} | {self.matriz_resposta[2]} |\n"
			  f"{self.tip[1][1]}| {self.matriz_resposta[1]} | {self.matriz_resposta[3]} |")

		for pr in self.porc_tip :
			print(f"\nTipo {self.tipo_de_sangue(pr[0])}, Alelos = {pr[0]} , Provabilidade de = {pr[1]} % ")

		if c_ativo:

			self.tip.append(todos_tipos[t - 1][1])

			print("-+" * 40)

			print(f"  |  {self.tip[0][0]}  |  {self.tip[0][1]}  |\n"
				  f"{self.tip[1][0]}| {self.matriz_resposta[0]} | {self.matriz_resposta[2]} |\n"
				  f"{self.tip[1][1]}| {self.matriz_resposta[1]} | {self.matriz_resposta[3]} |")

			for pr in self.porc_tip:
				print(f"\nTipo {self.tipo_de_sangue(pr[0])}, Alelos = {pr[0]} , Provabilidade de = {pr[1]} % ")

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


	def limp(self):
		try:
			os.system("clear")
		except:
			os.system("cls")


	def cruzamento(self):
		m_cruzadas=[]
		porc = ["IaIa", "IaIb", "IaIi", "IbIi", "IbIb", "IiIi"]#"IbIa","IiIa","IiIb"]
		nm=[0,0,0,0,0,0,0,0,0]

		for a in self.tip[0]: # monta a matriz resposta
			for b in self.tip[1]:
				ctpm=a+b

				if ctpm == "IbIa":
					ctpm = "IaIb"
				if ctpm == "IiIa":
					ctpm = "IaIi"
				if ctpm == "IiIb":
					ctpm = "IbIi"
				#ctpm.replace("IbIa","IaIb")
				#ctpm.replace("IaIi","IiIa")
				#ctpm.replace("IiIb","IbIi")
				m_cruzadas.append(ctpm)
				self.matriz_resposta.append(a+b)
				l=int(porc.index(ctpm))
				nm[l]+=1

		for m in range(0,len(nm)):# m,n in nm,porc:# monta os resultados
			if nm[m] == 0:
				pass
			else:
				fgh=(1/(4/nm[m]))*100
				self.porc_tip.append([porc[m],fgh])



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
	
