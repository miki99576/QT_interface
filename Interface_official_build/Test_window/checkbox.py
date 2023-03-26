import PySimpleGUI as psg
"""
psg.set_options(font=("Arial Bold",14))
l1=psg.Text("Enter Name")
l2=psg.Text("Faculty")
l3=psg.Text("Subjects")
l4=psg.Text("Category")
l5=psg.Multiline(" ", expand_x=True, key='-OUT-', expand_y=True,justification='left')
t1=psg.Input("", key='-NM-')
rb=[]
rb.append(psg.Radio("Arts", "faculty", key='arts', enable_events=True,default=True))
rb.append(psg.Radio("Commerce", "faculty", key='comm', enable_events=True))
rb.append(psg.Radio("Science", "faculty", key='sci',enable_events=True))
cb=[]
cb.append(psg.Checkbox("History", key='s1'))
cb.append(psg.Checkbox("Sociology", key='s2'))
cb.append(psg.Checkbox("Economics", key='s3'))
b1=psg.Button("OK")
b2=psg.Button("Exit")
layout=[[l1, t1],[rb],[cb],[b1, l5, b2]]
window = psg.Window('Checkbox Example', layout, size=(715,250))
while True:
   event, values = window.read()
   print (event, values)
   if event in (psg.WIN_CLOSED, 'Exit'): break
   if values['comm']==True:
         window['s1'].update(text="Accounting")
         window['s2'].update(text="Business Studies")
         window['s3'].update(text="Statistics")
   if values['sci']==True:
         window['s1'].update(text="Physics")
         window['s2'].update(text="Mathematics")
         window['s3'].update(text="Biology")
   if values['arts']==True:
         window['s1'].update(text="History")
         window['s2'].update(text="Sociology")
         window['s3'].update(text="Economics")
   if event=='OK':
         subs=[x.Text for x in cb if x.get()==True]
         fac=[x.Text for x in rb if x.get()==True]
         out=
Name={}
Faculty: {}
Subjects: {}
.format(values['-NM-'], fac[0], " ".join(subs))
   window['-OUT-'].update(out)
window.close()
"""
layout = [[psg.Checkbox("History", key='s1'),psg.Checkbox("Math", key='sZ')]] 
window = psg.Window('Checkbox Example', layout,)
while True:
   event, values = window.read()
   
