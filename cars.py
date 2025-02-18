class cars:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

  def __str__(self):
    return f"{self.make} {self.model} {self.year}"
  
  def display(self):
    print(self.make, self.model, self.year)

bmer = cars("BMW", "328i", 2015)
explorer = cars("Ford", "Explorer", 2015)
tesla = cars("Tesla", "Model S", 2021)

#bmer.display()
print('My cars:', bmer, explorer, tesla, sep="\n\t")