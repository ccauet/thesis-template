import re

replace_dict = {
  re.escape("\it{K}_{\kern[-0.3]{S}}^{0}") : "\KS",
  re.escape("\it{J/\kern[-0.3]{\psi}}") : "\jpsi",
  "{Candidates / (.*)};" : "{$\\\\text{Candidates} / \\1$};",
  re.escape("$Candidates") : "$\\\\text{Candidates}",
  re.escape("{-5}") : "{$-5$}",
  re.escape("{-0.5}") : "{$-0.5$}",
  re.escape("MeV/\it{c}^{2}") : "\si{\MeVcc}",
  "([0-9.]+) ps" : "\SI{\\1}{\pico\second}",
  "([0-9.]+) \\\\si{\\\\MeVcc}" : "\SI{\\1}{\MeVcc}",
  re.escape("{DD}") : "{\\\\text{\catdd}}",
  re.escape("{LL}") : "{\\\\text{\catll}}",
  re.escape("(ps)") : "(\si{\pico\second})",
}
