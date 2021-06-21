naive.bayes <- function(dataset,query,min.prob = 1e-7) {
  
  #Normalizacao da variavel temperatura para o dataset e para a query
  
  aux = as.numeric(dataset[,1])
  dataset[,1] = as.matrix(discretize(aux,method = "fixed", breaks = c(-Inf, 36, 38, Inf), labels = c("baixa", "normal", "alta")))
  
  aux = as.numeric(query[,1])
  query[,1] = as.matrix(discretize(aux,method = "fixed", breaks = c(-Inf, 36, 38, Inf), labels = c("baixa", "normal", "alta")))
  
  #Esse loop chama a funcao Naive Bayes para cada linha da query
  resultado = NULL
  
  for(i in 1:nrow(query)){
    aux = as.matrix(query[i,1:ncol(query)-1])
    resp = naive.activation(dataset = dataset,query = aux,min.prob = min.prob)
    print(resp$probabilidades)
    #resultado = rbind(resultado, resp$probabilidades)
  }
  
}

naive.activation <- function(dataset,query,min.prob = 1e-7) {

	#Inicializacao das variaveis utilizadas
	
	classId = ncol(dataset)
	classes = as.matrix(unique(dataset[,classId]))

	probabilidades = rep(0,ncol(classes))

	#Este loop vai determinar a probabilidade de
	#cada uma das classes possiveis, em funcao dos 
	#valores de atributos passados na query,
	#isto eh, preencher os valores do vetor probabilidades

	for(i in 1:ncol(classes)){

		#Calculo da probabilidade basica de cada classe (usando log)
	
		P_classe = sum(dataset[,classId] == classes[i]) / nrow(dataset)
		probabilidades[i] = probabilidades[i]+log(P_classe)

		for (j in 1:nrow(query)){

			#Para cada atributo j do modelo,
			#eh contada a quantidade de ocorrencias
			#da classe i onde o parametro j
			#assume o valor passado na query,
			#isto eh, P(j = j_query|i = i_classe) 

			Attr_j = query[j]
			if(Attr_j != "?"){
				P_Attr_j_classe = sum(dataset[,j] == Attr_j &
						dataset[,classId] == classes[i]) /
						sum(dataset[,classId] == classes[i])
				if(P_Attr_j_classe == 0){
					P_Attr_j_classe = min.prob
				}
				probabilidades[i] = probabilidades[i]+
						log(P_Attr_j_classe)
			}
		}
	
	}

	#Remocao dos logaritmos

	probabilidades = exp(probabilidades)

	#Criacao e incializacao da lista de resposta

	ret = list()
	ret$classes = classes
	ret$probabilidades = probabilidades / sum(probabilidades)

	return(ret)
}