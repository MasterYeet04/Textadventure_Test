#!/usr/bin/python3
# coding=utf-8

#Definiezion der Klasse Raum
class Room:
  def __init__(self, name="Zimmername", description="Beschreibung"):
    self.name = name
    self.description = description
    self.exits = {}

  def __str__(self):
    return self.name + "\n" + self.description

#Alle Räume
eigenes_Zimmer = Room(name="Dein Zimmer", description="Du stehst in deinem Zimmer es ist ein relativ kleiner Raum. Im Norden ist eine Tür die dich in den Hausflur führt.")
Hausflur = Room(name="Hausflur", description="Es ist ein langer Gang mit ein paar Regalen. Im Norden ist eine Tür, die in die Küche führt. Im Süden ist eine Tür die dich in dein Zimmer führt. Im Osten befindet sich die Tür zu Wohnzimmer")
Wohnzimmer = Room(description="Du kannst ein Sofa und einen Fernsehr sehen außerdem ist auch noch eine Zimmerpflanze zu sehen.", name="Wohnzimmer")
Küche = Room(name="Küche", description="Es ist eine Nicht besonderes Große Küche aber sie hat alles was mann zum Leben Braucht")

print(Wohnzimmer)

#Alle Richtungen
directions = ("norden","osten","süden","westen")

#Raum verbindungen
eigenes_Zimmer.exits["norden"] = Hausflur
Hausflur.exits["süden"] = eigenes_Zimmer
Hausflur.exits["osten"] = Wohnzimmer
Wohnzimmer.exits["westen"] = Hausflur
Hausflur.exits["norden"] = Küche
Küche.exits["süden"] = Hausflur
#Aktueller Raum
current_room = None

def enter_room(room):
  global current_room
  current_room = room
  describe_room()

def describe_room():
  emit()
  emit(current_room.name); emit()
  emit(current_room.description); emit()

def emit(s="", width=80):
  column = 0
  for word in str(s).split():
      column += len(word) + 1
      if column > width:
          column = len(word) + 1
          print()
      print(word, end=" ")
  print()

def play():
    enter_room(eigenes_Zimmer)
    while execute_command():
        pass

def help():
    emit("folgende befehle werden unterstützt:")
    emit("    gehe [nach] <richtung>")
    emit("    geh  [nach] <richtung>")
    emit("    schaue")
    emit("    schau")
    emit("    beschreibung")
    emit("    ende")
    emit("")
    emit("folgende richtungen werden unterstützt:")
    emit("norden")
    emit("osten")
    emit("süden")
    emit("westen")

def execute_command():
    words = read_command()
    if words:
        if "hilfe" in words:
            help()
        elif words[0] in ("gehe", "geh"):
            if len(words) > 2 and words[1] == "nach":
                execute_go(words[2])
            elif len(words) > 1:
                execute_go(words[1])
            else:
                emit("Wohin soll ich gehen?")
        elif words[0] in directions:
            execute_go(words[0])
        elif words[0] in ("schaue", "schau", "beschreibung"):
            describe_room()
        elif words[0] == "ende":
            return False
        else:
            emit("Ich verstehe '%s' nicht." % "".join(words))
            help()
    return True

def read_command():
    return [word.lower() for word in input("? ").rstrip(".?!").split()]

def execute_go(direction):
    room = current_room.exits.get(direction)
    if room:
        enter_room(room)
    else:
        emit("Du kannst nicht nach '%s' gehen." % direction)

play()
