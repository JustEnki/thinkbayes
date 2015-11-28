class BayesTheorem(object):
  """This class describes Bayes' Theorem."""

  #class variables

  #initialize
  def __init__(self, prior, likelihood, norm_constant):
    self.prior = prior                                    #p(H) - the probability of the hypothesis before we see the data
    self.likelihood = likelihood                          #p(D|H) - the probability of the data under the hypothesis
    self.norm_constant = norm_constant                    #p(D) - the probability of the data under any hypothesis

  #class methods
  def calc_posterior(self):                               #p(H|D) - the probability of the hypothesis after we see the data
    self.posterior = (float(self.prior) * float(self.likelihood)) / self.norm_constant  #calculation is: p(H|D) = (p(H) * p(D|H)) / p(D)