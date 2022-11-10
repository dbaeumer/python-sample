import cmd
import pdb

debugIn = open('/$debug/input', 'r', -1, 'utf-8')
debugOut = open('/$debug/output', 'w', -1, 'utf-8')

cmdline = cmd.Cmd(None, debugIn, debugOut)
cmdline.use_rawinput = False

debugger = pdb.Pdb(cmdline)

debugger.run('import app')