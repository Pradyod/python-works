"""
shallow copy - copies top level obejcts, share refernce of need object
deepcopy - copies both top level object and nested object

"""

from copy import copy,deepcopy

m_fvt_foods=[
    ["meals","sambar"],
    ["biriyani","lime"],
    ["burger","lime"]
]
n_fvt_foods=deepcopy(m_fvt_foods)
n_fvt_foods[0][0]="dosa"

print(m_fvt_foods)
print(n_fvt_foods)