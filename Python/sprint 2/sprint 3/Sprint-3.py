import os
import random
## тут используем Dictionary для хранения всех глав ( Словарь all_kapiteln )
## где ключ — номер секции
## а значение — текст главы:
all_kapiteln = {
    1: """
EIN SCHATTEN ERWACHT 
"Argh! Mein Kopf... dieses Licht ... ist das der Tod?"
Dein Geist ist verwirrt und es fällt dir schwer, dich zu erheben. Nur verschwommen erkennst du einen spärlich erleuchteten Raum. Das geheiligte Symbol der Göttin Kar ist allgegenwärtig.Überall erblickst du die achtflammige Sonne: geschnitzt ins Holz des Betthimmels, gewoben in die Seide der Wandteppiche und gegossen in Gold der Kunstwerke. Du bist im großzügig ausgestatteten Schlafgemach eines Sonnenpriesters. Draußen tobt ein heftiges Unwetter. Schwerer Regen peitscht gegen das Bleiglas und für einen Augenblick wird das Zimmer in grelles Weiß getaucht. Da kracht das Fenster zurück. Die Kerzen des Kandelabers auf dem Nachttisch verlöschen.
"Da ist jemand ... ein Schatten!"
Du schnellst herum. Niemand. Dein Herz rast. Unerwartet stürzt du über etwas auf dem Boden und erblickst den alten Körper eines Menschen, gehüllt in die ausladende, gold gelbe Schlafkutte eines Kar-Priesters. Seine wirren, aschgrauen Haare auf dem Hinterkopf sind von Blut durchtränkt. Er regt sich nicht.
"Ist er etwa tot!?"
Ähnlich den Gewitterblitzen draußen zucken dir Gedanken durch den Kopf: Du hast weder eine Ahnung, wo du dich befindest, wer vor dir liegt, noch ...
"Wer bin ICH?"
Nur zögerlich und mit einer düsteren Vorahnung wandert dein Blick über das dunkle Gewand, das zerfetzt an deinem Körper herabhängt, und verharrt auf deinen zittrigen schwarzen Klauen: Blut! Das Blut des Mannes zu deinen Füßen!
"Oh, nein ... Was habe ich getan?"
Du willst nur fort von diesem Ort, fort von dieser Tat, als Schrittgeräusche an dein Ohr dringen.
""",

    3: """
Nur wenige Schritte zum Tempel. Ein kurzer, gehetzter Blick nach hinten: niemand. Doch du hörst, dass etliche Soldaten über die verschlungenen Kieswege auf dich zukommen. Das Netz der Verfolger wird enger.
Du drückst dich in den Schatten der Wand, da lähmt ein stechender Schmerz deinen linken Oberschenkel! Voller Pein schreist du auf und fällst vornüber.
"Erwischt!", vermeldet eine Männerstimme triumphierend. Zähnefletschend presst du die Wunde ab. Blut quillt über deine Klauen und du ertastest, dass der Bolzen tief im Fleisch steckt. Zu tief, um ihn auf die Schnelle herauszuziehen. Die Verfolger haben dich fast erreicht.
""",

    7: """
Du besiegst deine Angst, krallst deine blanken Füße in den Stein des Fenstersimses und springst gegen den Wind in die Dunkelheit, den Landepunkt am Baumstamm fest im Blick.
""",

    10: """
Ohne Mühe befreist du die enge Öffnung von Gestrüpp und Unkraut und du erkennst, dass ein Eisengitter den Schacht versperrt. Aber du bist zu weit gekommen, um aufzugeben! Mit letzter Kraft reißt du das verrostete Gitter aus der Verankerung und blickst erschöpft in die Dunkelheit.
Außer einem muffigen, erdigen Geruch nimmst du nichts wahr. Trotzdem kriechst du hinein, und schlängelst dich geschmeidig wie eine Vintaqnatter voran. Nach einigen Armzügen ertastest du schließlich eine Mauerkante. Bedacht lässt du dich herab und kannst wieder aufrecht stehen. Du bist blind ob der absoluten Schwärze.
""",

    11: """
Unter deinen Füßen knirscht der Kies, doch das Tosen von Wind und Regen verschluckt dieses verräterische Geräusch. Mit langen Schritten hältst du auf den Torbogen zu, musst zuvor jedoch am Kar-Tempel vorbei, der auf halbem Weg im Zentrum des Lustgartens steht.
Mittlerweile haben die Wachleute ihre Suche auf den Park ausgeweitet. Du hörst das bedrohliche Klacken von Armbrustwinden.
""",

    13: """
Obwohl nur vereinzelt Lichtstrahlen durch die schmalen Fugen der Steinplatte sowie den langen Luftschacht in dein Versteck fallen, kannst du doch erahnen, wie unbeugsam die Morgensonne an diesem Tage scheint. Der Gedanke daran lässt dich unwillkürlich erschaudern.
Trotz des spärlichen Lichts überblickst du die Krypta nun in Ganze, als habe jemand eine blutrote Laterne entzündet: In zehn gemauerten Nischen ruhen acht reich verzierte Steinsärge. Obwohl du nicht imstande bist, sie zu lesen, lassen gemeißelte Symbole darauf schließen, dass Vorfahren der Kar-Priesterschaft in den Sarkophagen liegen. In einer Ecke steht eine wuchtige Holztruhe. Du siehst kein Schloss.
""",

    15: """
Im letzten Moment rollst du dich in einen der dichten Rosensträucher hinein. Du hast Glück, dass das Gewächs eine Züchtung ohne wehrhafte Dornen ist. Du zwingst dich, den Atem anzuhalten, denn nur wenige Fuß von dir entfernt siehst du an den unteren Ranken vorbei die schweren Lederstiefel zweier Wachmänner der Priesterschaft.
"Verdammt, der Kerl muss hier doch irgendwo sein", flucht einer der beiden.
Ohne Vorwarnung stechen sie wahllos mit ihren Breitschwertern in die dicht gewachsene Hecke. Ein Hieb verfehlt deine Brust um Haaresbreite, als unverhofft ein Kratzen und Schaben ertönt. "War da was?, faucht einer der Soldaten.
"Komm, den schnappen wir uns!"
Du verharrst wie versteinert, bis die beiden Wachmänner wieder fort sind. Dennoch ist die Gefahr nicht gebannt: Immer mehr Palastbewohner laufen im Park umher.
Verzweifelt suchst du nach einem Ausweg und entdeckst das massive Steinfundament des Tempels mit einem zugewucherten Schacht, der womöglich in ein Gewölbe unterhalb des geweihten Kar-Hauses führt.
""",

    16: """
Geräuschlos schlüpfst du durch das über und über mit Schnitzereien verzierte Holzportal des Tempels.
Dunkelheit empfängt dich, als das schwere Eisenschloss hinter dir wieder zuschnappt. Einzig grelle Blitze erhellen von Zeit zu Zeit den Raum durch die hohen Bleiglasfenster.
Du bist allein. Nach einigen Schritten an Gebetsbänken vorbei stehst du vor einer großen Bodenplatte aus tiefschwarzem Basalt. Ringsherum separieren finstere Nischen den Raum. In ihnen wachen übergroße Heilige. Ihr unbeugsamer, in Marmor geschlagener Blick flößt dir Respekt ein.
Während du den Tempel untersuchst, hörst du ein Kratzen und Schaben über dir. Dreck rieselt vom Gebälk auf deinen kahlen Schädel und den Steinboden. Kein Zweifel: Jemand ist auf dem Dach! Schindeln lösen sich, rutschen die Schräge hinunter und zerschellen unweit entfernt. Durch das entstandene Loch fällt der Regen. Sicherheitshalber suchst du an einer Säule Deckung.
Ein Blitz! Und für einen flüchtigen Moment erscheint über dir ein diffuser Schatten. Du erstarrst.
"Wo ist er hin?"
Außerhalb des Tempels entsteht stimmgewaltiges Durcheinander. Deine Verfolger halten den Fremden auf dem Dach für den Attentäter. Du lauschst angestrengt, doch über dir ist es wieder still. Die Soldaten entfernen sich.
Du atmest auf und blickst dich in aller Ruhe um. Neben der Kirchenorgel, deren längste Pfeifen bis unter die Kuppel reichen, bemerkst du an einer der Säulen, direkt bei der schwarzen Bodenplatte, einen Hebel aus Messing, verziert mit Dutzenden Totenschädeln.
""",

    33: """
Die ganze Nacht hast du mit einem Bolzen im Oberschenkel verbracht. Zumindest glaubst du das. Als du die Verletzung begutachten willst, bemerkst du, dass an der Stelle, wo er im Fleisch stecken sollte, nichts ist. Das Eisengeschoss liegt unweit von dir entfernt auf dem Boden.
""",

    35: """
Du rennst um eine weitere Ecke des Flurs, da siehst du draußen einen Schatten durch das Fenster spähen. Erschreckt kommst du ins Stolpern und stürzt vornüber mit einem dumpfen Schlag gegen die Wand. Benommen rappelst du dich wieder auf. Die Gestalt ist verschwunden! Du setzt deine Flucht fort.
Kurze Zeit später schlägt hinter dir eine Tür zurück. "Halt! Stehen bleiben!", brüllt eine raue Männerstimme in zackigem Befehlston.
Zugleich vernimmst du das unheilvolle metallische Singen eines Schwertes, das aus seiner Scheide gezogen wird.
""",

    38: """
Obwohl dieser Ort eng und finster ist, fühlst du dich hier sicher. Die Nacht soll kommen! Stoisch legst du dich in eine der freien Nischen und sinnierst über deine Lage. Immer wieder stellst du dir dieselben Fragen.
"Wer bin ich? Warum bin ich hier? Was habe ich getan?"
Du hast keine Antworten. Vor Angst, den Verstand zu verlieren, schließt du die Augen.
Nach einer kurzen, unruhigen Ruhestarre wirst du von einem Schaben und Kratzen aufgeschreckt und hörst, wie die Bodenplatte zur Krypta aufschwingt!
Eine junge Frau mit gelockten, blonden Haaren tritt besonnen die Stufen hinab, indem sie die Kar-Kutte über die Knie ihrer bleichen Beine hebt. Während sie die Grabkammer in der Dunkelheit absucht, erstrahlen ihre goldenen Augen, wie die einer geblendeten Katze: "Bei der heiligen Mutter Kar, ist hier jemand?"
Du drückst dich tiefer in die Nische der Toten, um sich ihrem zauberhaften Blick zu entziehen. Dein Herz überschlägt sich. Welch gottgleiche Schönheit! Gebannt von der Anmut der Priesterin willst du hervortreten, als sie plötzlich auf der letzten Stufe - inmitten ihres Schrittes - verharrt. Es scheint, die Zeit sei auf ewig eingefroren.
"Was geschieht hier?"
Hinter ihr schält sich ein Schatten aus der Dunkelheit!
""",

    40: """
Mit eindringlichen Rufen versucht der Soldat, dich zum Stehenbleiben zu bewegen. Glücklicherweise bist du mit den Lumpen am Leib schneller als dein gerüsteter Verfolger.
Du hastest den Gang entlang und drängst dich durch eine Gruppe verdutzter Palastbewohner, geweckt vom Tumult. Allerdings trauen sie sich nicht, dich aufzuhalten. Da taucht ein schlaftrunkener Wächter auf und versperrt dir mit einer Lanze den Weg. Du möchtest umkehren, doch der alte Wachmann hat dich mittlerweile eingeholt und schneidet dir schnaufend den Rückweg ab. Du sitzt in der Falle.
""",

    42: """
Mit einem ansatzlosen, katzenhaften Satz springst du den Sonnen-Soldaten an. Verdutzt von dieser flinken Attacke verliert er das Gleichgewicht. Dabei rudert er mit den Armen, kracht gegen die Wand und rutscht ohnmächtig an ihr hinab. Den Helm ins Gesicht gerutscht, die Waffe entglitten, sitzt er vor dir.
""",

    46: """
Vorsichtig tapst du voran. Unter deinen nackten Sohlen fühlst du den feuchten, schroffen Steinboden eines Kellergewölbes. Die Kühle dieses Ortes lässt dich erschaudern. Doch du hoffst, dass du hier vor deinen Verfolgern, die weiterhin durch den Park streifen, in Sicherheit zu sein.
Nach und nach ertastest du die Umgebung und dir wird klar, dass du dich inmitten einer Krypta mit mehreren Steinsärgen befindest. Trotz der Angst, die Geister der Toten zu erzürnen, setzt du deine Suche fort und stolperst in einer abgelegenen Ecke über eine schwere Holztruhe mit Eisenbeschlägen. Ein Schloss gibt es nicht.
""",

    55: """
Ein ums andere Mal durchdringen heftige Blitze die Finsternis der Nacht, während du die Gänge des Palasts, an zahllosen Türen, Erkern und Durchgängen vorbei, auf nackten Füßen entlang hastest.
Hektisch schaust du dich um. Das grelle Flackern der Naturgewalten wirft die geisterhaften Schemen von knorrigen Bäumen an die Wand und es scheint, als griffen die sich windenden Äste nach dir. Du blickst durch die trüben Fenster in den Sturm hinaus. Wieder ein Blitz!
Erschreckt zuckst du zusammen. Inmitten des Kronenlaubs kauert ein Schatten! Fasziniert verharrst du und versuchst durch die Verzerrungen der Scheiben zu erkennen, wen oder was du in der Finsternis gesehen hast.
""",

    56: """
Im geduckten Sprint hetzt du durch den Regen. Unweit von dir entfernt ragt das steile Dach des Kar-Tempels durch die Baumkronen.
"Womöglich ein geeignetes Versteck!"
In Furcht eine Zielscheibe für die Armbrustschützen zu sein, rennst du durch Hecken, hechtest über Parkbänke und rollst dich auf dem aufgeweichten Rasen ab. Der Tempel ist nicht mehr fern! Trotz aller Akrobatik entgleitet dir dabei die Öllaterne, deren Petroleum sich in einem kleinen, heftigen Flächenbrand entzündet. Paralysiert blickst du in die Flammen. Eine Mischung aus Faszination und Angst steigt in dir auf. Erst die Schreie deiner Verfolger lassen dich wieder zur Besinnung kommen. Einige von ihnen sind aus den Fenstern der Parterres in den Park gesprungen. Deine Hoffnung auf Flucht schwindet.
""",

    58: """
Nach knapp einer Stunde nimmst du nichts Beunruhigendes mehr außerhalb des Tempels wahr.
""",

    60: """
Zielsicher schlägst du dich zwischen Büschen und Sträuchern voran, bis du den idyllischen Tempel erreichst. Das massive Gebäude mit seinem steilen Dach aus Tonziegeln liegt inmitten einer Gruppe von meisterlich gestutzten Bäumen. Ringsum zieren duftende Rosenhecken und kunstvolle Statuen den friedvollen Platz.
Du hast die Eingangstür fast erreicht, als gleichzeitig Donner und Blitz die Luft zum Knistern bringen. Im aufflackernden Licht siehst du, dass deine Verfolger dir bedrohlich nahegekommen sind. Seltsamerweise ist die klerikal verzierte Tür des Tempels bloß angelehnt.
""",

    65: """
Im Schutze des Raanbaumes lässt du nervös deinen Blick über den Palast des Priesterkaisers schweifen, der ringsum den Innenhof umgibt. Mittlerweile huschen Dutzende Soldaten und Bedienstete an den Fenstern vorbei oder blicken hinaus. Die Nachricht vom Tod des Hierarchen hat sich wie ein Lauffeuer herumgesprochen.
"Finden sie mich, werden sie mich hinrichten!"
Bei deiner verzweifelten Suche nach einem Fluchtweg erblickst du auf der gegenüberliegenden Seite des monumentalen Baus einen imposanten Torbogen und dahinter eine abschüssige Rampe. Offenbar die einzige Verbindung von der obersten Ebene der gigantischen Stufenpyramide nach unten.
Der Palasthof selbst ist ein verwinkelter, unübersichtlicher Park aus schmalen Kieswegen, flankiert von bunten Fruchtbäumen, kunstvoll gestutzten Sträuchern und Blumen. In seinem Zentrum steht ein glanzvoller Kar-Tempel.
""",

    71: """
Mit dem Mute der Verzweiflung springst du kopfüber durch das verschlossene Fenster mit seinen dicken Bleiglasscheiben auf das dichte Blätterwerk eines Raanbaums zu. Die spärlichen Fetzen Stoff, die einst deine Kleidung waren, schützen dich nicht vor den zahllosen messerscharfen Scherben, die sich dir dabei ins Fleisch bohren.
""",

    72: """
Hastig greifst du nach dem Türriegel aus poliertem Messing. Mit all dem Blut an deinen Klauen rutschst du zunächst etwas ab, doch mit dem zweiten Versuch gelingt es dir, die schwere Holztür zu öffnen. Flackerndes Licht scheint dir entgegen. Geschmeidig, fast katzenartig, drückst du dich durch den schmalen Spalt auf einen langen Gang. Prächtige Rüstungen sowie Porträts in Öl auf der einen und Dutzende Bleiglasfenster auf der anderen Seite flankieren den opulenten Flur.
""",

    76: """
Du drehst dich herum und siehst den fahlen Schein eines Kerzenleuchters. Im letzten Moment versteckst du dich hinter einer großen Bodenvase, als eine Dienerin um die Ecke tritt. Sie schleicht in deine Richtung, verharrt unweit vor dir an der Tür zum kaiserlichen Schlafgemach und presst ihr Ohr gegen das Holz. Zögerlich klopft sie und fragt: "Ist alles in Ordnung, mein Hierarch?"
Sie zögert. Da lässt ein klirrendes Geräusch sowohl die junge Frau als auch dich zusammenfahren.
"Mein Hierarch?!"
Die Dienerin öffnet die Tür und du nutzt die Gelegenheit, ebenfalls über ihre Schulter hinweg ins Halbdunkel des Zimmers zu blicken. Nach wenigen Schritten bemerkt sie die Leiche - ein langer, schriller Schrei, und der Leuchter entgleitet ihrer Hand. Die Kerzen kullern durch den Raum und entzünden den dünnen Stoff des Betthimmels.
""",

    77: """
Kaum hast du dich vom kurzen Kampf gegen den alten Recken erholt, hörst du die schweren Schritte eines weiteren Wachmanns. Aus Furcht, Verstärkung könnte eintreffen, entschließt du dich, aus dem nächsten Erker zu entkommen.
Geschickt öffnest du ein Fenster zum Innenhof. Die heftige Böe bläst dir die Scheiben scheppernd entgegen und gibt den Blick in die Tiefe frei. Zu hoch für dich! Aber die knorrigen Aste eines in voller Blüte stehenden Raanbaums sind in Sprungweite. Du packst dein Herz in beide Hände und nimmst Anlauf ...
""",

    88: """
Nach knapp einer Stunde hast du die Untersuchung der Katakombe abgeschlossen. Erschöpft und zitternd vor Kälte, kauerst du dich in einer freien Nische zusammen. Die Stille der Krypta überträgt sich auf deinen Atem. Mit dem Gefühl von Geborgenheit versuchst du Ruhe zu finden.
""",

    89: """
Zusammengekauert hinter einer der lebensechten Statuen, wartest du gespannt darauf, dass sich der Tumult auf dem Hof legt. Du zitterst. Mit den wenigen, völlig durchnässten Fetzen am Leib, bist du der Kühle des Tempels schutzlos ausgeliefert.
Immer wieder huschen Soldaten an den bunten Fenstern vorbei, doch keiner von ihnen macht Anstalten, im Tempel nachzusehen.
"Seltsam. Warum suchen sie nicht hier nach mir?"
In den letzten Minuten hat sich das Gewitter merklich abgeschwächt, und der silberblaue Schein des Vollmonds dringt vereinzelt durch die Wolken.
An der Stirnwand des Tempels glänzen die langen Flöten einer Orgel. Ein Laken bedeckt die Tastatur des Instruments.
""",

    90: """
Zielstrebig wie eine Wantor-Bergkatze auf Beutejagd segelst du im hohen Bogen durch die Luft. Laub raschelt, Aste brechen. Gleichwohl geht der Lärm deines Sturzes durch die dichte Krone des Raanbaums im allgemeinen Getöse des Sturmes unter. Im Angesicht des sicheren Absturzes versuchst du deine Krallen in den ächzenden Stamm zu treiben, doch du kratzt nur an der Rinde und stürzt ab.
Als du wieder erwachst, scheint etwas Zeit vergangen. Benommen starrst du auf deine klauenartigen Hände. Auf dem Rücken der Rechten erkennst du ein Symbol, ähnlich eines Brandmals. Deine Linke ist übersät von runzeligen Narben, grausam entstellt.
"Dieses Zeichen ... ist das Ugar? Der Mond? Was hat das alles bloß zu bedeuten?"
Dir wird wieder bewusst, in welcher Lage du dich befindest.
""",

    92: """
Orientierungslos rennst du durch den Rundgang um den Hof des Palasts. Deine Hoffnung schwindet, jemals aus diesem gigantischen Gebäude zu entfliehen, doch etwas tief in deinem Inneren treibt dich an.
""",

    97: """
Vor dir steht ein Hüne von einem Kerl. Über seiner schweren Rüstung glänzt der Goldene Greif, das Wappentier Rhenus. Der gestandene Soldat schaut dich trotz etwas verschlafener Augen finster an. In der Rechten hält er ein Schwert, in der Linken Öllaterne und Schwertscheide samt Gürtel. Er konnte seine komplette Ausrüstung wohl nicht mehr rechtzeitig anlegen. Laterne und Scheide legt er langsam - ohne dich aus den Augen zu lassen - neben sich auf den Boden.
""",

    100: """
Ehe du reagieren kannst, ist der Schatten auf dich zugehuscht und packt deine Kehle mit steinhartem Griff. Unbarmherzig zieht er dich heran.
Silbern glänzende, pupillenlose Augen durchdringen deinen Geist, deinen Verstand. Du spürst, wie todbringende Kälte in dich strömt. Dein Blut gefriert. Hilflos erstarrst du. Das Letzte, was du wahrnimmst, ist das siegessichere Grinsen auf den versteinerten Gesichtszügen dieses nachtschwarzen Überwesens.
Hast du in diesem Kapitel den 1. SCHICKSALSPUNKT gefunden? Wenn nicht, kannst du es erneut versuchen und tiefgehender die Geheimnisse der Ahnen erforschen bei deiner Flucht ...
""",

    101: """
Deine VITALITÄT ist normal. Trage dies nun auf dem Abenteuerblatt ein.
Pochender Schmerz lässt dich unsanft erwachen. Dein kahler Schädel brummt und fauliges Stroh klebt dir auf den Lippen. Sämtliche Muskeln brennen, als du dich vom Steinboden erhebst. Du bist in einer feuchten Kerkerzelle. Durch das Eisengitter tanzt spärlicher Fackelschein.
Allmählich kriechen die Geschehnisse der vergangenen Nacht wieder in deine Erinnerung: die Leiche des Hierarchen, deine Flucht in die idyllische Kapelle, der mysteriöse Schatten, der dich verfolgte, um dich hierher zu verschleppen, und natürlich die liebreizende Kar-Priesterin, die du erblicken durftest, bevor die Zeit einfror. Die Erinnerung an sie entflammt dein Herz.
Du musterst die schwarze Haut deines Körpers - den man in ein fleckiges Baumwollgewand gesteckt hat — auf Verletzungen oder sonstige Spuren, die einen Hinweis auf deine Entführung geben könnten, entdeckst aber nichts Außergewöhnliches.
Wie viele Stunden du ohnmächtig warst, kannst du nicht sagen. In diesem trostlosen Gefängnis gibt es keinen Hinweis darauf, ob der Mond strahlt oder die Sonne brennt. Gewissenhaft tastest du dich ab und durchwühlst das Stroh —- von deinen Habseligkeiten keine Spur.
Man hat dir deinen ganzen Besitz (Utensilien, Besondere Gegenstände, Waffen, Kleidung) abgenommen. Markiere daher alle verlorenen Gegenstände mit einem Kreuz im Speicherpunkt, es sei denn, er ist bereits markiert. Vielleicht bekommst du sie zu einem späteren Zeitpunkt wieder. Das Einzige, was du derzeit am Leibe trägst, ist ein Gefangenengewand (Kleidung, Umhang). Vermerke alle Änderungen jetzt auf dem Abenteuerblatt.
""",

    105: """
Vor lauter Anstrengung wird dir schwarz vor Augen, doch der Gedanke daran, in diesem Verlies zu verrotten, setzt übermenschliche Kraft in dir frei. Mit einem lauten Schlag zerspringen die Mauersteine und du hältst das Gitter samt Verankerung in Händen.
Dir ist klar, dass der ohrenbetäubende Lärm im ganzen Gefängnis zu hören war. Daher bereitest du dich auf ungebetenen Besuch vor.
""",

    256: """
Du fokusierst deine wahrhaft übermenschliche Kraft über deine Klauen auf das Metall. Beim dritten Ruck rieselt feiner Steinstaub an der Verankerung, bis schließlich Steine zu Boden poltern. Das Gitter liegt fre! Übereilte Schritte dringen in dein Ohr.
""",

    271: """
Du atmest tief ein und konzentrierst dich auf die Kraft deines Körpers. Dann zerrst du mit einem vor Anstrengung unterdrückten Schrei am Gitter.
""",

    292: """
Das Gitter zeigt deutliche Rostflecken, macht dennoch einen robusten Eindruck. Ohne nachzudenken packst du eine der Querstangen und rüttelst. Fest.
Nur eine Armlänge vom Gitter entfernt fließt Abwasser druch eine verkrustete Rinne im Steinboden. Auch aus deiner Zelle entspringt ein solches Rinnsal aus einem winzigen Loch.
""",

    'K1': """
Alsbald verpestet der typische Gestank eines Gartak die Luft. Die gedrungenen, stark behaarten Wesen sind eine dumpfe Kriegerrasse, gezüchtet in den Katakomben der Magierstadt Tul-Sar-Mar. Bedingungslos dienen sie ihren Echsenmeistern.
Während du dich in eine dunkle Ecke drückst, hörst du das Klirren eines Kettenhemds und das Schleifen von Ledersohlen. Ein schmieriger Gartak, bewaffnet mit einem verrosteten Kurzschwert, stapft die schmalen Stufen zum Verlies herunter. An seinem Gürtel klimpert ein großer Metallring mit zahlreichen Schlüsseln.
""",

    'K8': """
Die schwarzen Augen im wildschweinartigen Schädel des Gartak weiten sich, als du ihn zu einem offenen Zweikampf zwingst. Mach dich bereit zum Angriff auf den Gefängniswärter!
""",

    'K59': """
Mit nur einem Satz springst du dem Wärter in den Rücken. Der Gartak ist vollkommen überrascht und nicht in der Lage sich gekonnt zu verteidigen.
"""
}

sektionen = {
    # --- 1 ---
    1:  {"kapitel": 1, 
         "next": [72]
        },
    72: {"kapitel": 72, 
         "next": [76]
         },
    76: {"kapitel": 76, 
         "next": [55]
         },
    55: {"kapitel": 55, 
         "next": [92]
         },
    92: {"kapitel": 92, 
         "next": [35]
         },

    # --- 35 (ветвление: бой или бегство) ---
    35: {
        "kapitel": 35,
        "wahl": {
            "kämpfen": 97,
            "fliehen": 40
        }
    },

    # --- 97 (выбор между атакой, прыжком, бегством) ---
    97: {
        "kapitel": 97,
        "wahl": {
            "attackieren": 42,
            "springen": 71,
            "rennen": 40
        }
    },

    40: {"kapitel": 40,
         "next": [71]
         },
    71: {"kapitel": 71,
         "next": [90]
         },

    # --- 42 (выбор предметов) ---
    42: {
        "kapitel": 42,
        "item_auswahl": [
            {"name": "Schwert", 
             "effekt": {"Angriff": +3}
             },
            {"name": "Öllaterne"}
        ],
        "next": [77]
    },

    77: {"kapitel": 77, 
         "next": [7]
         },
    7: {"kapitel": 7, 
        "next": [90]
        },
    90: {"kapitel": 90, 
         "next": [65]
         },
    65: {"kapitel": 65, 
         "next": [11]
         },

    # --- 11 (ветвление в зависимости от инвентаря) ---
    11: {
        "kapitel": 11,
        "inventar_wahl": {
            "item": "Öllaterne",
            "hat": 56,
            "nicht": 60
        }
    },

    56: {"kapitel": 56, 
         "next": [3]
         },
    60: {"kapitel": 60, 
         "next": [16]
         },
    16: {"kapitel": 16, 
         "next": [89]
         },
    89: {"kapitel": 89, 
         "next": [58]
         },
    58: {"kapitel": 58, 
         "next": [33]
         },
    33: {"kapitel": 33, 
         "next": [13]
         },
    13: {"kapitel": 13, 
         "next": [38]
         },
    38: {"kapitel": 38, 
         "next": [100]
         },

    # --- 100 (решение: сыграть заново или продолжить) ---
    100: {"kapitel": 100, 
          "restart_frage": True, 
          "next": [101]
          },

    # --- 56 / 3 / 15 / 10 / 46 / 88 / — побочная ветка ---
    46: {"kapitel": 46, 
         "next": [88]
         },
    88: {"kapitel": 88, 
         "next": [33]
         },
    10: {"kapitel": 10, 
         "next": [46]
         },
    15: {"kapitel": 15, 
         "next": [10]
         },
    3: {"kapitel": 3, 
        "effekt": {"Vitalität": -1}, 
        "next": [15]
        },

    # --- 101 (начало второй главы, плен) ---
    101: {
        "kapitel": 101,
        "aktionen": [{"typ": "verlust", 
                      "wert": "Inventar"
                      }],
        "inventar_reset": ["Gefangenengewand"],
        "next": [292]
    },

    292: {"kapitel": 292, 
          "next": [271]
          },

    271: {
        "kapitel": 271,
        "test": {
            "attribut": "Stärke",
            "gegen": 14,
            "erfolg": 256,
            "fehlschlag": 105
        }
    },

    256: {"kapitel": 256, 
          "next": [101]
          },
    105: {"kapitel": 105, 
          "effekt": {"Vitalität": -1}, 
          "next": [101]
          },

    # --- Бой с Гартаком ---
    "K1": {
        "kapitel": "K1",
        "kampf": "Gartak",
        "wahl": {
            "hinterrücks": "K59",
            "offen": "K8"
        }
    },
    "K59": {
        "kapitel": "K59",
        "kampf": "Gartak_Überrascht",
        "next": [256]
    },
    "K8": {
        "kapitel": "K8",
        "kampf": "Gartak",
        "next": [256]
    }
}

START_SPIELER = {
    "Name": "Unbekannter",
    "Vitalität": 10,
    "Stärke": 8,
    "Angriff": 11,
    "Verteidigung": 10,
    "Resistenz": 2,
    "Inventar": []
}
spieler = {
    "Name": START_SPIELER["Name"],
    "Vitalität": START_SPIELER["Vitalität"],
    "Stärke": START_SPIELER["Stärke"],
    "Angriff": START_SPIELER["Angriff"],
    "Verteidigung": START_SPIELER["Verteidigung"],
    "Resistenz": START_SPIELER["Resistenz"],
    "Inventar": list(START_SPIELER["Inventar"])
}

GEGNER_STATS = {
    "Gartak": {
        "Angriff": 11,
        "Verteidigung": 10,
        "Resistenz": 2,
        "Vitalität": 8
    },
    "Gartak_Überrascht": {
        "Angriff": 10,
        "Verteidigung": 10,
        "Resistenz": 2,
        "Vitalität": 8
    }
}

## Функция для отображения текста главы
def show_kapitel(num):
    print()
    print(f'--- Kapitel {num} ---')
    print(all_kapiteln[num])
    print('------------------\n')

## Функция для получения выбора пользователя из доступных опций
def user_choice(options: dict):
    keys = list(options.keys())
    while True:
        print("\nDeine Optionen:")
        for index, key in enumerate(keys, start=1):
            print(f"{index}. {key}")

        wahl = input(">> ").strip()
        if wahl.lower() in ("s", "stats", "status"):
            zeige_stats()
            continue
        if wahl.isdigit():
            pos = int(wahl) - 1
            if 0 <= pos < len(keys):
                return options[keys[pos]]
        print("❌ Ungültige Eingabe! Bitte eine Zahl wählen.")

## Функция для применения эффектов на игрока
def apply_effekt(effekt: dict):
    for stat, value in effekt.items():
        if stat not in spieler:
            continue
        vorher = spieler[stat]
        if stat == "Vitalität" and value == 0:
            spieler[stat] = 0
        else:
            spieler[stat] = vorher + value
        print(f"⚡ {stat} verändert sich: {vorher} -> {spieler[stat]}")

## Функция для обработки полученных предметов
def handle_aktionen(aktionen):
    for ak in aktionen:
        typ = ak.get("typ")
        wert = ak.get("wert")
        if typ == "item" and wert:
            spieler["Inventar"].append(wert)
            print(f"👜 Du hast erhalten: {wert}")

            # применить бонус оружия
            if "effekt" in ak:
                apply_effekt(ak["effekt"])
        elif typ == "verlust" and wert == "Inventar":
            spieler["Inventar"].clear()
            print("🗑️ Dein Inventar ist jetzt leer.")

def zeige_stats():
    print("\n📊 Deine Werte:")
    print(f"- Name: {spieler['Name']}")
    print(f"- Vitalität: {spieler['Vitalität']}")
    print(f"- Stärke: {spieler['Stärke']}")
    print(f"- Angriff: {spieler['Angriff']}")
    print(f"- Verteidigung: {spieler['Verteidigung']}")
    print(f"- Resistenz: {spieler['Resistenz']}")
    inv = spieler["Inventar"]
    print("- Inventar:", ", ".join(inv) if inv else "leer")

def item_auswahl(optionen):
    print("\nWähle einen Gegenstand aus:")
    for index, opt in enumerate(optionen, start=1):
        print(f"{index}. {opt['name']}")

    ausgewaehlt = None
    while True:
        wahl = input(">> ").strip()
        if wahl.lower() in ("s", "stats", "status"):
            zeige_stats()
            continue
        if wahl.isdigit():
            pos = int(wahl) - 1
            if 0 <= pos < len(optionen):
                ausgewaehlt = optionen[pos]
                break
        print("❌ Ungültige Eingabe! Bitte eine Zahl wählen.")

    item = ausgewaehlt
    name = item["name"]
    spieler["Inventar"].append(name)
    print(f"👜 Du hast aufgenommen: {name}")
    if "effekt" in item:
        apply_effekt(item["effekt"])

## Функция для проведения теста атрибута
def test_attribute(attribut, gegen):
    wurf = random.randint(1, 20)
    wert = spieler[attribut]
    print(f"\n🎲 Teste {attribut} gegen {gegen}: Wurf={wurf}, Wert={wert}")

    return (wurf + wert) >= gegen

## Функция для проведения боя
def kampf_start(gegner_name):
    print(f"\n⚔️ Kampf gegen: {gegner_name}")
    enemy = GEGNER_STATS[gegner_name].copy()

    while spieler["Vitalität"] > 0 and enemy["Vitalität"] > 0:
        spieler_angriff = spieler["Angriff"] + random.randint(1, 6)
        if spieler_angriff > enemy["Verteidigung"]:
            schaden = spieler_angriff - enemy["Verteidigung"] - enemy["Resistenz"]
            if schaden > 0:
                enemy["Vitalität"] -= schaden
                print(f"🎯 Du triffst! Schaden: {schaden}")
            else:
                print("🛡️ Der Gegner absorbiert den Schaden!")
        else:
            print("❌ Dein Angriff verfehlt!")

        if enemy["Vitalität"] <= 0:
            print("🏆 Du besiegst den Gartak!")
            return True

        gegner_angriff = enemy["Angriff"] + random.randint(1, 6)
        if gegner_angriff > spieler["Verteidigung"]:
            schaden = gegner_angriff - spieler["Verteidigung"] - spieler["Resistenz"]
            if schaden > 0:
                spieler["Vitalität"] -= schaden
                print(f"💥 Der Gartak trifft dich! Schaden: {schaden}")
            else:
                print("✨ Du absorbierst den Schaden!")
        else:
            print("⚡ Der Angriff des Gartaks verfehlt!")

        print(f"❤️ Deine Vitalität: {spieler['Vitalität']}")
        print(f"💀 Gartak Vitalität: {enemy['Vitalität']}")

        if spieler["Vitalität"] <= 0:
            print("💀 Du wurdest besiegt!")
            return False

    return True


def inventar_setzen(neue_gegenstaende):
    spieler["Inventar"] = list(neue_gegenstaende)
    if spieler["Inventar"]:
        print("🎒 Neues Inventar:", ", ".join(spieler["Inventar"]))
    else:
        print("🎒 Dein Inventar ist leer.")


def hole_next(sektion):
    ziel = sektion.get("next")
    if isinstance(ziel, list):
        return ziel[0] if ziel else None
    return ziel


def warte_auf_enter_oder_stats():
    while True:
        antwort = input("🔸 Weiter mit Enter ...").strip()
        if antwort == "":
            return
        if antwort.lower() in ("s", "stats", "status"):
            zeige_stats()
            continue
        print("Bitte Enter drücken oder 's' / 'stats' eingeben.")


def reset_spieler():
    spieler["Name"] = START_SPIELER["Name"]
    spieler["Vitalität"] = START_SPIELER["Vitalität"]
    spieler["Stärke"] = START_SPIELER["Stärke"]
    spieler["Angriff"] = START_SPIELER["Angriff"]
    spieler["Verteidigung"] = START_SPIELER["Verteidigung"]
    spieler["Resistenz"] = START_SPIELER["Resistenz"]
    spieler["Inventar"] = list(START_SPIELER["Inventar"])


### Основная функция для прохождения игры
def spiele_ab():
    aktuelle = 1  # начало
    while True:
        sek = sektionen.get(aktuelle)
        if sek is None:
            print(f"Für Kapitel {aktuelle} gibt es noch keinen Programmteil.")
            break
        
        os.system('cls' if os.name == 'nt' else 'clear')
        show_kapitel(aktuelle)
        warte_auf_enter_oder_stats()

        if "aktionen" in sek:
            handle_aktionen(sek["aktionen"])

        if "item_auswahl" in sek:
            item_auswahl(sek["item_auswahl"])

        if "inventar_reset" in sek:
            inventar_setzen(sek["inventar_reset"])

        effekt = sek.get("effekt")
        if effekt:
            if effekt.get("Vitalität") == 0:
                print("\n💀 Du bist gestorben.")
                break
            apply_effekt(effekt)
            if spieler["Vitalität"] <= 0:
                print("\n💀 Du bist gestorben.")
                break

        if "test" in sek:
            t = sek["test"]
            if test_attribute(t["attribut"], t["gegen"]):
                aktuelle = t["erfolg"]
            else:
                aktuelle = t["fehlschlag"]
            continue

        if "kampf" in sek:
            kampf_start(sek["kampf"])

        if spieler["Vitalität"] <= 0:
            print("\n💀 Du bist gestorben. Spiel Ende.")
            antwort = input("Neues Spiel? (j/n): ").strip().lower()
            if antwort.startswith("j"):
                reset_spieler()
                aktuelle = 1
                continue
            break

        if "inventar_wahl" in sek:
            info = sek["inventar_wahl"]
            ziel = info["hat"] if info["item"] in spieler["Inventar"] else info["nicht"]
            aktuelle = ziel
            continue

        if sek.get("restart_frage"):
            antwort = input("Nochmal von vorne starten? (j/n) ").strip().lower()
            if antwort in ("s", "stats", "status"):
                zeige_stats()
                continue
            if antwort.startswith("j") or spieler["Vitalität"] < 1:
                reset_spieler()
                aktuelle = 1
            else:
                aktuelle = hole_next(sek) or 101
            continue

        if "wahl" in sek:
            aktuelle = user_choice(sek["wahl"])
            continue

        naechster = hole_next(sek)
        if naechster:
            aktuelle = naechster
            continue

        print("\n🎉 ENDE DES SPIELS")
        break


if __name__ == "__main__":
    spiele_ab()
