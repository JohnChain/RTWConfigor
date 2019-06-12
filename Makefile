UIPREFIX = TumConf
SRC = mainUI.py
all:
	pyuic5 $(UIPREFIX).ui -o $(UIPREFIX).py

clean:
	rm -rf __pycache__