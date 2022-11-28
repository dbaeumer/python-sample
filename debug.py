import pdb

dbgin = open('/$debug/input', 'r', -1, 'utf-8')
dbgout = open('/$debug/output', 'w', -1, 'utf-8')

debugger = pdb.Pdb(stdin=dbgin, stdout=dbgout)
debugger.prompt = ''

debugger.run('import app')