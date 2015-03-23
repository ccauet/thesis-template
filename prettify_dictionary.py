import re

replace_dict = {
  re.escape("\it{K}_{\kern[-0.3]{S}}^{0}") : "\KS",
  re.escape("\it{J/\kern[-0.3]{\psi}}") : "\jpsi",
  re.escape("$Candidates") : "$\\\\text{Candidates}",
}