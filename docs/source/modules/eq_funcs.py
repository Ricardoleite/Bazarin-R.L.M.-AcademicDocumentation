import sympy as sp
from IPython.display import display, Math

def display_broken_equation(equation, terms_per_line=4):
    lhs = sp.latex(equation.lhs)

    rhs_terms = sp.Add.make_args(equation.rhs)

    lines = []

    for i in range(0, len(rhs_terms), terms_per_line):
        group = rhs_terms[i:i + terms_per_line]
        expression = sp.Add(*group)

        latex_group = sp.latex(expression)

        if i == 0:
            lines.append(rf"{lhs} &= {latex_group}")
        else:
            lines.append(rf"&\quad {latex_group}")

    latex_output = (
        r"\begin{aligned}"
        + r" \\ ".join(lines)
        + r"\end{aligned}"
    )

    display(Math(latex_output))

def brokeq(equation, terms_per_line=4):
    lhs = sp.latex(equation.lhs)
    rhs_terms = list(sp.Add.make_args(equation.rhs))

    lines = []
    for i in range(0, len(rhs_terms), terms_per_line):
        group = rhs_terms[i:i + terms_per_line]

        # Build the latex for this group manually so we control signs
        terms_latex = []
        for j, term in enumerate(group):
            coeff, rest = term.as_coeff_Mul()
            sign = "-" if coeff < 0 else "+"
            # strip sign from latex
            term_latex = sp.latex(abs(coeff) * rest) if coeff != 1 and coeff != -1 \
                         else sp.latex(rest)
            terms_latex.append((sign, term_latex))

        # First term of the whole RHS has no leading + / -
        first_sign, first_tex = terms_latex[0]
        if i == 0:
            head = first_tex if first_sign == "+" else f"- {first_tex}"
            line = rf"{lhs} &= {head}"
        else:
            head = first_tex if first_sign == "+" else f"- {first_tex}"
            prefix = "+ " if first_sign == "+" else ""
            # Actually for continuation we want the sign explicit:
            line = rf"&\quad {first_sign} {first_tex}"

        # Remaining terms in the group
        for sign, tex in terms_latex[1:]:
            line += rf" {sign} {tex}"

        lines.append(line)

    return r"\begin{aligned}" + r" \\ ".join(lines) + r"\end{aligned}"