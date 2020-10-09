= Asciidoc preview Auto Reload

Questo script python permette di convertire in `.html` e ricaricare in firefox il documento asciidoc che si sta scrivendo.

== Avvio tramite file `.bat`

Modificare nel file `.bat`:

* la path completa del file `.adoc` che si sta scivendo (-f)
* la path completa del convertitore asciidoc to html (-c) in questo caso 'asciidoc-py3'

.Esempio
----
python asciidocreload.py -f c:\Users\myuser\Desktop\asciidoc-auto-reload\README.adoc -c c:\Users\myuser\Desktop\asciidoc-py3-master\asciidoc.py
----

== Prerequisiti

* driver per caricare la pagina tramite firefox: `geckodriver`

TIP: inserirlo nella cartella di esecuzione dello script o cambiare nel file `asciidocreload.py`

.asciidocreload.py
[source,python,numbered]
----
include::asciidocreload.py[lines=41]
----

ok!
