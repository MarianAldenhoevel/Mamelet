https://marian-aldenhoevel.de/mamelet
___

Das MAMElet ist die funktionstüchtige verkleinerte Ausgabe eines Arcade-Spielautomaten. Während das Gehäuse etwa nur ein Viertel der Originalgröße hat, sind die Steuerelemente originalgroß geblieben. Das verleiht dem Gerät optisch ein wenig Kindchenschema. Das Gehäuse ist freihändig aus Sperrholz gesägt, verleimt und lackiert. Die Centipede-Sideart habe ich aus einem Foto extrahiert, lasergedruckt und mit Leim und Lack auf die Seiten auflaminiert.

Die Innereien bestehen aus geborgenen Originalteilen: Joystick, Münzeinwurf und die Starttasten stammen aus einem toten Automaten.

Dazu kommt Hardware aus der Grabbelkiste: Als Bildschirm dient ein Industrie-TFT im VGA-Format mit 640x480 Pixeln, das hochkant eingebaut ist. Alte PC-Aktivboxen spendeten Audio-Verstärker und Lautsprecher. Eine USB-LED-Leselampe beleuchtet das Banner mit dem MAME-Logo und ein USB-Hub ist verbaut damit weitere Steuerelemente wie Tastatur, Maus oder Gamepad angeschlossen werden können. Von allen diesen Teilen sind auch die Netzteile mit ins Gehäuse gestopft. Als Nebeneffekt wird das Gehäuse dadurch schön schwer und bleibt sicher stehen.

Lediglich die CPU ist neu: Ein Raspberry-Pi 3 unter Raspbian führt AdvMenu/AdvMAME  aus.

Die Steuerelemente werden von einem Python-Skript mit GPIO in Tastendrücke umgesetzt, so daß Frontend und Emulator unverändert geblieben sind. Das Ergebnis dieser Komponente ist MAMElet_keys.py, eine allgemeine Kapselung der Aufgabe mit Entprellung. Bei der Verdrahtung hat sich gezeigt, daß einer der Mikroschalter des alten Joysticks nicht mehr schließen will, der öffnende Kontakt ist aber einwandfrei. Deshalb kann das Python-Programm active-low und active-high gleichermaßen verarbeiten.

Der originale Münzprüfer war leider zu einem soliden Klotz korrodiert und noch für DM konfiguriert. Außerdem wäre er zu hoch gewesen, Ich habe deshalb nur die Frontplattenelemente behalten, sie näher aneinander montiert und eine IR-Lichtschranke als Münzsensor eingebaut. Das MAMElet akzeptiert damit nun alle möglichen Münzen, Beilagscheiben und Knöpfe. und das gesammelte Fremdkleingeld der Familie wohnt jetzt in seinem Münzfach.

Als MAME-Maschine kann das MAMElet fast 3000 verschiedene klassische Spielautomaten emulieren. Manche besser, manche schlechter. Mein Ziel war die goldene Ära, es sollten Asteroids, Pac-Man, Donkey-Kong, Galaga, Gyruss, und dergleichen präsentabel wiedergegeben werden können. Das hat zu der Entscheidung geführt den Bildschirm auf Kosten der vertikal orientierten Spiele hochkant einzubauen. Diese haben nun nur noch eine horizontale Auflösung von 480 Pixel zur Verfügung.

Elemente und Layout der Steuerung sind bestimmt durch die zur Verfügung stehenden Originalteile und den begrenzten Platz. Es gibt also nur einen 8-Wege-Joystick und zwei Knöpfe. Die gewünschten klassischen Spiele lassen sich damit gut bedienen, wenn auch nicht immer exakt vorbildtreu. Mehr und andere Controls werden extern an den USB-Hub in der Frontplatte angeschlossen.

MAME ist ein Emulator. Das bedeutet die Spiele wurden nicht nachprogrammiert, sondern es handelt sich um die Originalprogramme die auf in Software nachgeahmter Hardware laufen. Heutige Maschinen, auch der zigarettenschachtelgroße Raspberry-Pi sind leistungsfähig genug um dabei nicht ins Schwitzen zu geraten. Mir gefällt der Gedanke, daß Pac-Man und seine Kollegen gar nicht merken, daß sie nicht auf der zeitgenössischen Hardware ausgeführt werden sondern in einem modernen Computer.

Das Python-Skript für die Behandlung der Tastendrücke und ein paar andere kleinere Bestandteile sind auf GitHub zugänglich.
