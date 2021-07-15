fitness <- function(subject, subjectSize, distances){
  sum = 0
  for (i in 1:(subjectSize-1)){
    sum = sum + distances[subject[i], subject[i+1]]
  }
  sum = sum + distances[subject[subjectSize], subject[1]]
  return (1/sum)
}

third.model <- function(distances, k=5, popsize=100, ngenerations=100){
  
  #Gerar população inicial e calcular o fitness
  
  output = NULL
  ncities = nrow(distances)
  population = NULL
  population.fitness = rep(0, popsize)
  for (i in 1:popsize) {
    subject = sample(1:ncities)
    population = rbind(population, subject)
    population.fitness[i] = fitness(subject = subject, subjectSize = ncities, distances = distances)
  }
  
  #Iniciar processo evolutivo ao longo das gerações
  
  for (i in 1:ngenerations) {
    
    #Gerar e mutar os filhos
    
    children = NULL
    children.fitness = rep(0,popsize)
    for (j in 1:popsize) {
      new = population[j,]
      position = sample(1:ncities, size = 1)
      value = sample(1:ncities, size = 1)
      new = replace(new, new == value, -1)
      if(value == 1) new = c(value,new)
      else if(value == ncities) new = c(new,value)
      else new = c(new[1:(position-1)],value,new[position:ncities])
      new = new[new != -1]
      
      #aux = new[selected[1]]
      #new[selected[1]] = new[selected[2]]
      #new[selected[2]] = aux
      
      children = rbind(children,new)
      children.fitness[j] = fitness(subject = new, subjectSize = ncities, distances = distances)
    }
    
    #Junção de populações e seleção de fitness
    
    single.population = rbind(population, children)
    single.fitness = c(population.fitness, children.fitness)
    
    ids = sort.list(single.fitness, decreasing = TRUE)[1:popsize]
    population = single.population[ids,]
    population.fitness = single.fitness[ids]
    
    output = rbind(output, cbind(i, mean(population.fitness), sd(population.fitness)))
    
  }
  return(output)
}