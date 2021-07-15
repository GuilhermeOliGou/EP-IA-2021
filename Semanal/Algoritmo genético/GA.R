fitness <- function(subject, subjectSize, distances){
  sum = 0
  for (i in 1:(subjectSize-1)){
    sum = sum + distances[subject[i], subject[i+1]]
  }
  sum = sum + distances[subject[subjectSize], subject[1]]
  return (1/sum)
}

mutation <- function(chield, ncities, mutation.prob){
  if(runif(min = 0, max = 1, n=1) < mutation.prob){
    position = sample(1:ncities, size = 1)
    value = sample(1:ncities, size = 1)
    chield = replace(chield, chield == value, -1)
    if(position == 1) chield = c(value,chield)
    else if(position == ncities) chield = c(chield,value)
    else chield = c(chield[1:(position-1)],value,chield[position:ncities])
    chield = chield[chield != -1]
  }
}

ga.model <- function(distances, k=5, popsize=100, ngenerations=1000, mutation.prob=0.01){
  
  #Gerar população inicial
  
  output = NULL
  ncities = nrow(distances)
  population = NULL
  population.fitness = rep(0, popsize)
  for (i in 1:popsize) {
    subject = sample(1:ncities)
    population = rbind(population, subject)
  }
  
  #Iniciar processo evolutivo ao longo das gerações
  
  for (i in 1:ngenerations) {
    
    #Calcular fitness, gerar filhos e realizar mutações
    
    for (j in 1:popsize) {
      population.fitness[j] = fitness(subject = population[j,], subjectSize = ncities, distances = distances)
    }
    
    children = NULL
    
    for (j in 1:(popsize/2)) {
      
      #A recombinação uniforme foi abstraída da seguinte forma:
      #Ao invés da string binária, foi criado um vetor de indices de tamanho aleatório
      #Esse vetor de indices representa os genes AUSENTES do pai 1
      
      parentIds = sample(1:popsize, prob = population.fitness/sum(population.fitness), size = 2)
      
      parent1 = parentIds[1]
      parent2 = parentIds[2]
      
      qtd_genes_p1 = sample(0:ncities, size = 1)
      indices_p1 = sample(parent1, size = qtd_genes_p1)
      chield1 = replace(parent1, indices_p1, -1)
      
      genes_p1 = chield1[chield1 != -1]
      genes_p2 = replace(parent2, parent2 %in% genes_p1, -1)[parent2 != -1]
      
      for (k in 1:(ncities - qtd_genes_p1)) {
        chield1[chield1 == -1][1] = genes_p2[k]
      }
      
      chield2 = replace(parent1, parent1 %in% genes_p1, -1)
      genes_p1 = chield2[chield2 != -1]
      genes_p2 = replace(parent2, parent2 %in% genes_p1, -1)[parent2 != -1]
      
      for (k in 1:(qtd_genes_p1)) {
        chield2[chield2 == -1][1] = genes_p2[k]
      }
      
      chield1 = mutation(chield = chield1, ncities = ncities, mutation.prob = mutation.prob)
      chield2 = mutation(chield = chield2, ncities = ncities, mutation.prob = mutation.prob)
      
      children = rbind(children,chield1)
      children = rbind(children,chield2)
      
    }
    
    population = children
    
  }
  return(output)
}