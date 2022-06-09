'''
REPO: pyckathon

PREMESSA:
L’esercizio serve ad allontanare le paure che ci possono affliggere all’idea di dover imparare da zero un nuovo linguaggio.
Se non ve ne siete accorti, negli ultimi mesi ne abbiamo imparati già due. Oggi però farete tutto da soli.

SCOPO DEL GIOCO:
Sicuramente avrete già giocato al gioco dell’impiccato sui banchi di scuola, nei momenti morti di alcune lezioni con il vostro vicino.
Uno dei giocatori pensa una parola e aggiunge su un foglio un numero di trattini pari al numero di lettere che la compongono.
L’altro giocatore dovrà indovinare la parola tentando di indovinare le lettere che la compongono.
Ogni tentativo sbagliato verrà contato come errore.

TECNOLOGIE:
Oggi si lavora con Python, per questo motivo dovete concentrarvi solo sul file YOUR_SOLUTION.py, non curatevi degli altri file.
Se volete poi dopo le 18.00 potrete sbirciare il resto del codice.
Ma l’escamotage che abbiamo usato per farvi lavorare tranquilli è solo un modo semplice e comodo per permettervi di lavorare senza distrazioni

CONSEGNA:
I giocatori sono l'utente e il computer.
Il computer sceglie casualmente una parola e l'utente la dovrà indovinare.
Ha a disposizione 5 tentativi.

L'utente potrà provare ad indovinare una sola lettera per volta.
Ad ogni inserimento (sia che avvenga tramite tasto INVIO oppure tramite CLICK su apposito pulsante) il computer deve controllare
se quella lettera è presente nella parola da indovinare.

Se la lettera è presente, deve apparire al posto giusto, sostituendo il trattino (o i trattini) corrispondente.
Se la lettera non è presente, l'utente deve essere avvisato dell'errore con un messaggio che mostra anche quanti tentativi sono rimasti.
Se la lettera è già stata usata, l'utente deve essere avvisato con un messaggio, ma i tentativi a disposizione non devono diminuire.

Nella parte sottostante il campo di input saranno mostrate tutte le lettere già utilizzate dall'utente (sia quelle corrette che quelle errate).

Il gioco termina quando l'utente esaurisce i tentativi a disposizione oppure se indovina la parola.
In entrambi i casi si deve mostrare un messaggio adatto alla situazione.
'''

# CONSIGLI:
# - occhio alla indentazione

#------------------------------------------LIBRERIE-------------------------------------------------------

import random   #libreria per usare un valore casuale
import pyodide  #libreria per pyscript
import js       #libreria per javascript
from utils import Utils #libreria per utilizzare funzioni JS

custom_utils = Utils(pyodide, js) #istanza della libreria - ripensate all'esercizio di PHP con Movie ;)

#---------------------------------------ELEMENTI DAL DOM------------------------------------------------------

# questi elementi sono già stati catturati per te, 
# ti serviranno per prendere il valore inserito e catturare l'evento di invio

user_letter = custom_utils.getHtmlElement("user-letter")
add_letter_btn = custom_utils.getHtmlElement("add-letter-btn")

# questo elemento conterrà il testo segnaposto per la parola da indovinare
word_html_container = custom_utils.getHtmlElement('word')
errors = custom_utils.getHtmlElement("errors")
used_letters = custom_utils.getHtmlElement("used-letters")
result = custom_utils.getHtmlElement("result")
solution = custom_utils.getHtmlElement("solution")

#----------------------------------------------------------------------------------------------------
def main():
    #le variabili sono definite come esempi, non siete obbligati ad utilizzarle tutte o solo queste
    global words
    global count
    global length
    global word
    global display
    global already_guessed
    global limit
    global lettera_user
    global user_letters
    global count
    global letters
    count = 5
    errors = 0
    display = ""
    lettera_user = ""
    user_letters = []
    already_guessed = []
   

    
    words = ['matto', 'gatto', 'pazzo'] # array con le parole da indovinare

    word = random.choice(words)
    letters = list(word)

    for letter in letters:
        display += "_"
    custom_utils.writeToHtmlElement(word_html_container, '%s' % (display))
    custom_utils.addOnClickEventToHtmlElement(add_letter_btn, checkLetter)
    custom_utils.addKeyupEventToHtmlElement(add_letter_btn, checkLetter)
    # inserisco la stringa segnaposto dentro il contenitore HTML
    #display = "___" # da modificare
    # custom_utils.writeToHtmlElement(word_html_container, '%s' % (display))
def checkLetter(e):
    global count
    lettera_user = getattr(user_letter, 'value').lower()
    if(lettera_user in user_letters):
            custom_utils.writeToHtmlElement(errors, 'Attenzione! Hai già usato questa lettera, hai ancora %s tentativi' % (count))
            return
    user_letters.append(lettera_user)
    custom_utils.writeToConsole(count)
    if(lettera_user in letters):
        display = ""
        already_guessed.append(lettera_user)
        if(lettera_user in already_guessed):
            for letter in letters:
                if(letter in already_guessed):
                    display += letter
                else:
                    display += "_"
        custom_utils.writeToHtmlElement(word_html_container, '%s' % (display))
    #Check dei tentativi rimasti
    else:
        count -= 1
        custom_utils.writeToHtmlElement(errors, 'Hai sbagliato! Hai ancora %s tentativi' % (count))
    #Trasforma l'array di lettere in stringa
    string = ' - '.join(user_letters).upper()
    #Stampa delle lettere totali inserite
    custom_utils.writeToHtmlElement(used_letters, '%s' % (string))
    check = all(item in already_guessed for item in letters)
    if(check == True):
        custom_utils.writeToConsole("HAI VINTOOOOOO!")
        custom_utils.writeToHtmlElement(result, 'Complimenti! Hai vinto!')
        custom_utils.removeOnClickEventFromHtmlElement (add_letter_btn)
        return
    if(count == 0):
        custom_utils.writeToConsole("HAI PERSOOOOOO!")
        custom_utils.writeToHtmlElement(result, 'Che peccato! Hai perso!')
        custom_utils.removeOnClickEventFromHtmlElement (add_letter_btn)
        return
main()