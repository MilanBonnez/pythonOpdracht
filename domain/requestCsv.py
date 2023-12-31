import pandas as pd


class fileGenerator:

	def generateCsv(data, fileName):
		try:
			df = pd.DataFrame(data)
		except Exception as e:
			print("Kon de data niet vinden", e)
		try:
			df.to_csv(fileName)
		except Exception as e:
			print("Deze file kon niet aangemaakt worden",e)

