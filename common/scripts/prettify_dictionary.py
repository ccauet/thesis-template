import re

replace_dict = {
  re.escape("\it{K}_{\kern[-0.3]{S}}^{0}") : "\KS",
  re.escape("\it{J/\kern[-0.3]{\psi}}") : "\jpsi",
  re.escape("\it{t}") : "\dtime",
  "{Candidates / (.*)};" : "{$\\\\text{Candidates} / \\1$};",
  re.escape("$Candidates") : "$\\\\text{Candidates}",
  re.escape("{-5}") : "{$-5$}",
  re.escape("{-0.5}") : "{$-0.5$}",
  re.escape("MeV/\it{c}^{2}") : "\si{\MeVcc}",
  "([0-9.]+) ps" : "\SI{\\1}{\pico\second}",
  "([0-9.]+) \\\\si{\\\\MeVcc}" : "\SI{\\1}{\MeVcc}",
  re.escape("{DD}") : "{\\\\text{\catdd}}",
  re.escape("{LL}") : "{\\\\text{\catll}}",
  "scale=([0-9.]+), color=c, rotate=0]{\\$\\\\genfrac{}{}{0pt}{}{LHCb}{(.*)}\\$};" : "scale=2.18511, color=c, rotate=0, align=left]{LHCb\\\\\\\\{\\2}};",
  re.escape("(ps)") : "(\si{\pico\second})",
  re.escape("scale=2.83039") : "scale=2.18511",
  re.escape("scale=2.58211") : "scale=2.38229",
  re.escape("scale=2.33383") : "scale=2.18377",
  re.escape("scale=2.33383") : "scale=1.98647",
}
