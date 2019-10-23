# tkinter ir jāimportē
import tkinter
# jāizveido galvenais logs, izmnatojot metodi Tk()
logs = tkinter.Tk()
# uz loga var likt visus parastos elementu pogas, uzrakstus, radiopogas utt.
# izveido uzraksta elementu (Label), norādot kam tas piederēs un kāds būs teksts
uzraksts = tkinter.Label(logs, text="START(IT)")
# metode pack pielāgo uzraksta izmērus teksta lielumam
uzraksts.pack()
# lai logs parādītos, tas ir jāpalaiž mūžīgajā notikumu gaidīšanas ciklā
logs.mainloop()
# notikumu gaidīšanas cikls turpināsies līdz loga aizvēršanai
