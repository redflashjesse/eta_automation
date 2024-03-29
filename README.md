# eta_pelletsheizung
 Das Projekt ermöglicht es Benutzern, sich auf der ETA Webseite mit Benutzername und Passwort anzumelden, um regelmäßig Daten der ETA Pelletsheizung abzurufen. 
 Diese Daten werden in einem CSV-Format gespeichert und können für die Analyse der Leistung über einen Zeitraum verwendet werden. 
 Die Analyseergebnisse werden grafisch dargestellt, um Benutzern einen einfachen Überblick über die Leistungsentwicklung ihrer Heizung zu bieten. 
 Die Anzeige wird aktuell mit plotly realisiert. Für die Anwendung wird ein ETA-Benutzerkonto benötigt. 
 Für die Nutzung der Anwendung sind folgende Punkte zu beachten: eine .env-Datei muss im Hauptverzeichnis des Projekts erstellt werden, 
 die die folgenden Variablen enthält: USERNAME=username und PASSWORD=password, als interpreter wird Python 3.12 verwendet. Die Anwendung kann in der Datei `main.py` gestartet werden. 
 Mit den Variablen datacollection und dataanalysis kann gesteuert werden, ob die Daten gesammelt oder in Diagram ausgegeben werden sollen. 
 Die Zeit für die Datenabfrage kann in eta_datacollection.py mit der Variablen 'DATA_CALL_INTERVAL' gesteuert werden. 
 Die Zeit für die Datenabfrage kann in eta_datacollection.py mit der Variablen 'DATA_CALL_INTERVAL' eingestellt werden, dies ist die Wartezeit der Funktion, um den nächsten Datenabruf zu starten. 
 Sie wird in Sekunden angegeben. 
 Anwendungshinweise: Es wird Firefox als Browser verwendet. Dieser wird bei jedem Datenabruf geöffnet, es ist möglich die Schritte zuverfolgen, zum Schluss wird der Browser geschlossen. 
 Er kann jenach Belieben geändert werden, es sollte die Remote Funktion für Entwickler zugelassen sein.
 
link zu github: https://github.com/redflashjesse/eta_automation