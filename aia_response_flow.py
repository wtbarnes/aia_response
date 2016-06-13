"""
Build flowchart that describes calculation done in aia_get_response.pro
"""

from graphviz import Digraph


#Create graph and set some attributes
f = Digraph('t_rsp_flow',filename='aia_response_flow',format='png')
f.body.extend(['rankdir=LR'])

#Start adding nodes
f.node('aia_get_response',shape='square')
f.node('if emiss keyword is set',shape='diamond')
f.edge('aia_get_response','if emiss keyword is set')
f.node('read in a "full_emiss" .save file',shape='circle')

#View
f.view()

