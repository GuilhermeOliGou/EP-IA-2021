f <- function(net){
	return(1/(1+exp(-net)))
}

df_dnet <- function(f_net){
	return (f_net * (1 - f_net))
}

mlp.architecture <- function (input.lenght=2,
			hidden.lenght=2,
			output.lenght=1,
			activation.function=f,
			d_activation.function=df_dnet){
			
	model = list()
	model$input.lenght = input.lenght
	model$hidden.lenght = hidden.lenght
	model$output.lenght = output.lenght
	model$f = activation.function
	model$df_dnet = d_activation.function
	
	#matriz de pesos da camada escondida:
	#cada linha i da matriz representa o neuronio i da camada oculta,
	#cada coluna j indica o neuronio j da camada anterior,
	#a ultima coluna de cada linha indica o valor de theta,
	#a posicao (i,j) da matriz indica o peso da ligacao entre o neuronio
	#i da camada oculta com o neuronio j da camada anterior:
	#
	#		1		2		Theta
	#  1	w_11	w_12	theta_1
	#  2	w_21	w_22	theta_2
	
	model$hidden = matrix(runif(min=-0.5, max=0.5, hidden.lenght*(input.lenght+1)),
		nrow=hidden.lenght,ncol=(input.lenght+1))
		
	#Agora sera criada uma nova matriz para a camada de sai­da
	
	model$output = matrix(runif(min=-0.5, max=0.5,output.lenght*(hidden.lenght+1)),
		nrow=output.lenght,ncol=(hidden.lenght+1))
		
	return (model)
}

mlp.forward <- function(model,entrada){
	net_hidden_p = model$hidden %*% c(entrada,1)
	f_net_hidden_p = model$f(net_hidden_p)

	net_output_p = model$output %*% c(as.numeric(f_net_hidden_p),1)
	f_net_output_p = model$f(net_output_p)

	resp = list()

	resp$net_hidden_p = net_hidden_p
	resp$f_net_hidden_p = f_net_hidden_p
	resp$net_output_p = net_output_p
	resp$f_net_output_p = f_net_output_p

	return (resp)

}

mlp.backpropagation <- function(model,dataset,eta=0.1,threshold=1e-3){

	squaredError = 2*threshold
	counter = 0
	while (squaredError > threshold){
		squaredError = 0

		for(p in 1:nrow(dataset)){
			Xp = as.numeric(dataset[p,1:model$input.lenght])
			Yp = as.numeric(dataset[p,(model$input.lenght+1):ncol(dataset)])

			results = mlp.forward(model,Xp)
			
			Op = results$f_net_output_p
			error = Yp - Op
			squaredError = squaredError + sum(error^2)

			delta_output_p = error * model$df_dnet(results$f_net_output_p)

			w_output_kj = model$output[,1:model$hidden.lenght]
			delta_hidden_p = as.numeric(model$df_dnet(results$f_net_hidden_p))*
				(as.numeric(delta_output_p) %*% w_output_kj)

			model$output = model$output + 
				eta*(delta_output_p %*% 
				as.vector(c(results$f_net_hidden_p,1)))
			model$hidden = model$hidden +
				eta*(t(delta_hidden_p) %*%
				as.vector(c(Xp,1)))
		}
		
		squaredError = squaredError/nrow(dataset)
		cat("Erro quadrático médio: ", squaredError, "\n")
		counter = counter+1
	}
	
	ret = list()
	ret$model = model
	ret$counter = counter

	return(ret)
}